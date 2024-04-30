import socket

import threading
from .connection import WebSocketConnection

class WebSocketServer:
    '''
        Main Server class which starts a TCP server to Listen to Sockets
    '''
    def __init__(self, host="localhost", port=8910):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []
        self.message_received_callback = None
        self.client_connected_callback = None
        self.client_closed_callback = None

    def start(self):
        '''
            Constantly Listen for connections on the specified host and Port 
            Once the connection is established 
            Spawn another thread to handle websocket handshake 
            And listen for websocket frames on that Socket
        '''
        try:
            self.server_socket.bind((self.host, self.port))
            self.server_socket.listen(10)
            print(f"WebSocket server listening on {self.host}:{self.port}")
            while True:
                client_socket, addr = self.server_socket.accept()
                ws_conn = WebSocketConnection(client_socket, addr, self.message_received_callback, self.client_closed_callback)
                if self.client_connected_callback:
                    self.client_connected_callback(ws_conn)
                self.clients.append(ws_conn)
                threading.Thread(target=self.handle_client, args=(ws_conn,), daemon=True).start()
        except KeyboardInterrupt:
            print("Stopping the server")
            self.stop()


    def stop(self):
        '''
            Send Close Frames to all the sockets before stopping the server 
        '''
        for ws_conn in self.clients:
            ws_conn.close()
        self.server_socket.close()

    def handle_client(self, ws_conn):
        '''
            Complete WebSocket handshake and Listen for WebSocket Frames
        '''
        ws_conn.handle_handshake()
        while True:
            try:
                ws_conn.handle_message()
            except Exception as e:
                print("Error:", e)
                ws_conn.close()
                self.clients.remove(ws_conn)
                break

    def set_message_received_callback(self, callback):
        self.message_received_callback = callback

    def set_client_connected_callback(self, callback):
        self.client_connected_callback = callback
    
    def set_client_closed_callback(self, callback):
        self.client_closed_callback = callback