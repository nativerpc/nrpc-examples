import nrpc_py
import time

@nrpc_py.rpcclass({'query_x': 1})
class QueryService:
    def query_x(self, req):
        pass


class Application:
    def start(self):
        sock = nrpc_py.RoutingSocket(
            type=nrpc_py.SocketType.CONNECT,
            types=[QueryService, self]
        )
        sock.connect(port=9001)
        print(f'Client up, #{sock.client_id} port=9000')
        while sock.is_alive:
            time.sleep(1)
            client = sock.cast(QueryService)
            res = client.query_x({'data': 'hello world'})
            print(f'Client response: #{sock.client_id}, query_x, {res}')


if __name__ == '__main__':
    nrpc_py.init()
    Application().start()