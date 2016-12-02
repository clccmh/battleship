#!/usr/bin/python

import socketserver

class TCPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        self.data = self.request.recv(1024).strip()
        print("{} wrote: ".format(self.client_address[0]))
        print(self.data)
        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    server = socketserver.TCPServer(('localhost', 1337), TCPHandler)
    server.serve_forever()
