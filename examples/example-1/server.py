import time
import nrpc_py


@nrpc_py.rpcclass({'doQuery': 1})
class QueryService:
    def doQuery(self, request):
        pass


class Application:
    def start(self):
        sock = nrpc_py.RoutingSocket(
            type=nrpc_py.SocketType.BIND,
            types=[QueryService, self],
            caller='server'
        )
        sock.bind(port=9001)
        print(f'Server up: ip={sock.ip_address} port={sock.port}')
        time.sleep(1000000)
        
    def doQuery(self, request):
        print(f'doQuery request on server: {request}')
        return {
            'my_output': 'world welcomes',
            'orig_request': request
        }
    

if __name__ == '__main__':
    nrpc_py.init()
    Application().start()

# print(f'Server up: port=9001')
# time.sleep(1000000)
