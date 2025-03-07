import time
import nrpc_py

@nrpc_py.rpcclass({'query_x': 1})
class QueryService:
    def query_x(self, req):
        pass


class Application:
    def start(self):
        print('Server up, port=9001')
        sock = nrpc_py.RoutingSocket(
            type=nrpc_py.SocketType.BIND,
            types=[QueryService, self]
        )
        sock.bind(port=9001)

    def query_x(self, req):
        print(f'Server call: query_x, {req}')
        return {'result': 123}
    
if __name__ == '__main__':
    nrpc_py.init()
    Application().start()