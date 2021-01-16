from socket import socket, AF_INET, SOCK_STREAM, SHUT_RDWR, timeout, SOCK_DGRAM ,error,gethostname,gethostbyname


class MultiConnectionServer:

    def __init__(self, host, port):
        # initiate a default selector to handle multiple connections
        self.host = host
        self.port = port
        self.sel = selectors.DefaultSelector()
        self.chatLoop()

    def accept_wrapper(self, sock):
        conn, addr = sock.accept()  # Should be ready to read
        print("accepted connection from", addr)
        conn.setblocking(False)
        data = types.SimpleNamespace(addr=addr, inb=b"", outb=b"")
        events = selectors.EVENT_READ | selectors.EVENT_WRITE
        self.sel.register(conn, events, data=data)

    def service_connection(self, key, mask):
        sock = key.fileobj
        data = key.data
        if mask & selectors.EVENT_READ:
            recv_data = sock.recv(1024)  # Should be ready to read
            if recv_data:
                data.outb += recv_data
            else:
                print("closing connection to", data.addr)
                self.sel.unregister(sock)
                sock.close()
        if mask & selectors.EVENT_WRITE:
            if data.outb:
                print("echoing", repr(data.outb), "to", data.addr)
                sent = sock.send(data.outb)  # Should be ready to write
                data.outb = data.outb[sent:]

    def chatLoop(self, host=None, port=None):
        if host == None:
            host = self.host
        if port == None:
            port = self.port

        lsock = socket(AF_INET, SOCK_STREAM)
        lsock.bind((host, port))
        lsock.listen()
        print("listening on", (host, port))
        lsock.setblocking(False)
        self.sel.register(lsock, selectors.EVENT_READ, data=None)

        try:
            while True:
                events = self.sel.select(timeout=None)
                for key, mask in events:
                    if key.data is None:
                        self.accept_wrapper(key.fileobj)
                    else:
                        self.service_connection(key, mask)
        except KeyboardInterrupt:
            print("caught keyboard interrupt, exiting")
        finally:
            self.sel.close()


if __name__ == "__main__":

    # ------------------------ multiple connection server ------------------------ #
    # print(f'ip : {get_local_IP()}')
    # host, port = (get_local_IP(), 22225)
    # MultiServer = MultiConnectionServer(host, port)
# ---------------------------------------------------------------------------- #
