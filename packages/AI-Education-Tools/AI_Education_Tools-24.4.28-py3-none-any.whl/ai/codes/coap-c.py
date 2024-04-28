import asyncio
from aiocoap import Context, Message, GET

async def main():
    host = "localhost"  # Replace "server_ip" with the actual IP address of the CoAP server
    path = "hello/"

    protocol = await Context.create_client_context()

    request = Message(code=GET, uri=f"coap://{host}/{path}")
    try:
        response = await protocol.request(request).response
        print("Received response from server:", response.payload.decode())
    except Exception as e:
        print("Failed to fetch resource:", e)

if __name__ == '__main__':
    asyncio.run(main())
