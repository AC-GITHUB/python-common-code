import socketserver


class MyTCPHandler(socketserver.BaseRequestHandler):

    def setup(self):
        print("开始")

    def finish(self):
        print("结束")

    def handle(self):
        # self.request is the TCP socket connected to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        # just send back the same data, but upper-cased
        self.request.sendall(self.data.upper())


def serverstart():
    host = 'localhost'
    port = 34567
    server = socketserver.TCPServer((host, port),
                                    socketserver.BaseRequestHandler)
    server.serve_forever()


serverstart()
