import hashlib
import base64

class WebSocketConnection:
    def __init__(self, socket, address, message_received_callback, client_closed_callback):
        self.socket = socket
        self.client_key = None
        self.address = address
        self.message_received_callback = message_received_callback
        self.client_closed_callback = client_closed_callback

    def handle_handshake(self):
        '''
            Sends the WebSocket Upgrade response
        '''
        request = self.socket.recv(1024)
        headers = self.parse_headers(request)
        self.client_key = headers.get('Sec-WebSocket-Key', None)
        if self.client_key:
            accept_key = self.get_accept_key(self.client_key)
            response = self.get_handshake_response(accept_key)
            self.socket.send(response.encode())

    def parse_headers(self, data):
        '''
            Parse HTTP request headers received in this format
            "Content-Type : application/json\r\n"
        '''
        headers = {}
        lines = data.split(b'\r\n')
        for line in lines:
            parts = line.split(b':')
            # Ignore the first line which is request line 
            if len(parts) == 2:
                headers[parts[0].strip().decode()] = parts[1].strip().decode()
        return headers

    def get_accept_key(self, client_key):
        '''
            Generates accept key 
        '''
        client_key = client_key + '258EAFA5-E914-47DA-95CA-C5AB0DC85B11'
        hash = hashlib.sha1(client_key.encode())
        return base64.b64encode(hash.digest()).decode()

    def get_handshake_response(self, accept_key):
        '''
            Template HTTP response to WebSocket Upgrade Request
        '''
        return (
            f"HTTP/1.1 101 Switching Protocols\r\n"
            f"Upgrade: websocket\r\n"
            f"Connection: Upgrade\r\n"
            f"Sec-WebSocket-Accept: {accept_key}\r\n\r\n"
        )

    def handle_message(self):
        '''
            Parses WebSocket Frames and Invokes Message Receved Calback Function with Parsed Message

            WebSocket Frame (https://datatracker.ietf.org/doc/html/rfc6455)

            0                   1                   2                   3
            0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
            +-+-+-+-+-------+-+-------------+-------------------------------+
            |F|R|R|R| opcode|M| Payload len |    Extended payload length    |
            |I|S|S|S|  (4)  |A|     (7)     |             (16/64)           |
            |N|V|V|V|       |S|             |   (if payload len==126/127)   |
            | |1|2|3|       |K|             |                               |
            +-+-+-+-+-------+-+-------------+ - - - - - - - - - - - - - - - +
            |     Extended payload length continued, if payload len == 127  |
            + - - - - - - - - - - - - - - - +-------------------------------+
            |                               |Masking-key, if MASK set to 1  |
            +-------------------------------+-------------------------------+
            | Masking-key (continued)       |          Payload Data         |
            +-------------------------------- - - - - - - - - - - - - - - - +
            :                     Payload Data continued ...                :
            + - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - +
            |                     Payload Data continued ...                |
            +---------------------------------------------------------------+

        '''
        while True:
            header = self.socket.recv(2)
            if not header:
                break
            # This checks if first byte's most significant bit is 1. 
            # That bit represents whether this is the final frame or not
            # Not used as fragmentation is not supported yet
            fin = (header[0] & 0b10000000) != 0

            # By using bitwise and with 0b00001111 we are getting the value of 
            # last 4 bits of the first byte of the frame
            # as 0 & 1 = 0 and 1 & 1 = 1 
            opcode = header[0] & 0b00001111
            masked = (header[1] & 0b10000000) != 0
            payload_length = header[1] & 0b01111111

            if payload_length == 126:
                length_bytes = self.socket.recv(2)
                # TCP/IP uses big endian byteorder 
                payload_length = int.from_bytes(bytearray(length_bytes), byteorder='big')
            elif payload_length == 127:
                length_bytes = self.socket.recv(8)
                payload_length = int.from_bytes(bytearray(length_bytes), byteorder='big')

            if masked:
                mask = self.socket.recv(4)

            payload = bytearray()
            while len(payload) < payload_length:
                chunk = self.socket.recv(payload_length - len(payload))
                payload.extend(chunk)

            if masked:
                # By default WebSocket payloads sent by the client
                # Should be masked with a masking key
                for i in range(len(payload)):
                    payload[i] = payload[i] ^ mask[i % 4]

            # Hex Code Represents close frame as defined in the RFC
            if opcode == 0x8: 
                self.handle_close(payload)

            # Opcode of Text Frame
            elif opcode == 0x1: 
                if self.message_received_callback:
                    self.message_received_callback(payload.decode(), self)
            
    def send_message(self, message):
        '''
            Send a Text Frame 
        '''
        # 0x1 - 0b00000001
        self.send_frame(0x1, message)
    
    def send_frame(self, opcode, payload):
        # 0x80 - 0b10000000 
        fin_bit = 0x80 
    
        # This implementation does not support any extension as of now
        rsv_bits = 0x000

        # Shifting RSV to make space for Opcode 
        opcode_byte = fin_bit | (rsv_bits << 4) | opcode
        payload_length = len(payload)

        header_bytes = bytes([opcode_byte])

        if payload_length < 126:
            header_bytes += bytes([payload_length])
        elif payload_length <= 65535:
            header_bytes += bytes([126])
            header_bytes += (payload_length).to_bytes(2, byteorder='big')
        else:
            header_bytes += bytes([127]) 
            header_bytes += (payload_length).to_bytes(8, byteorder='big')

        self.socket.send(header_bytes)
        self.socket.send(payload)

    def send_close_frame(self, status_code=1000, reason=""):
        status_code_bytes = status_code.to_bytes(2, byteorder='big')
        reason_bytes = reason.encode()
        payload = status_code_bytes + reason_bytes
        # 0x8 - 0b00001000
        self.send_frame(0x8, payload)

    def handle_close(self, data):
        self.client_closed_callback(self, data)
    
    def close(self):
        self.send_close_frame()
