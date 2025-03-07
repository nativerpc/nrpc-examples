import time
import nrpc_py
from nrpc_py import rpcclass


@rpcclass({'doQuery': 1})
class QueryService:
    def doQuery(self, request):
        pass


class Application:
    def start(self):
        sock = nrpc_py.RoutingSocket(
            type=nrpc_py.SocketType.CONNECT,
            types=[QueryService],
            caller='client'
        )
        sock.connect(port=9001)
        print(f'Client up: id=#{sock.client_id} port=9001')

        while sock.is_alive:
            client = sock.cast(QueryService)
            response = client.doQuery({
                'my_input': 'hello world'
            })
            print(f'doQuery response on client: id=#{sock.client_id}, response={response}')
            time.sleep(1)


if __name__ == '__main__':
    nrpc_py.init()
    Application().start()
