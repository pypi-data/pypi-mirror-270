from coapthon.server.coap import CoAP
from coapthon.resources.resource import Resource

class HelloWorldResource(Resource):
    def __init__(self, name="HelloWorld", coap_server=None):
        super(HelloWorldResource, self).__init__(name, coap_server, visible=True,
                                                 observable=True, allow_children=True)
        self.payload = "Hello, World!"

    def render_GET(self, request):
        return self

    def render_PUT(self, request):
        self.payload = request.payload
        return self

class CoAPServer(CoAP):
    def __init__(self, host, port):
        super(CoAPServer, self).__init__((host, port))
        self.add_resource('hello/', HelloWorldResource())

def main():
    server = CoAPServer("localhost", 5683)
    print("CoAP server started on {}:{}".format("localhost", 5683))
    try:
        server.listen(10)
    except KeyboardInterrupt:
        print("Server Shutdown")
        server.close()
        print("Exiting...")

if __name__ == '__main__':
    main()
