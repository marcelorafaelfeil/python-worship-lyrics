import socket


class NetworkUtils:
    @staticmethod
    def getIPAddress():
        if socket.gethostname() is not None:
            return socket.gethostbyname(socket.gethostname())

        return None
