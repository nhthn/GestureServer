import argparse
import json
import pythonosc.udp_client
import asyncio
import websockets
import common

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-o", "--osc-host", default="127.0.0.1")
    parser.add_argument("-p", "--osc-port", type=int, default=57120)
    args = parser.parse_args()

    osc_client = pythonosc.udp_client.SimpleUDPClient(args.osc_host, args.osc_port)

    async def handler(websocket):
        async for message in websocket:
            state = [float(x) for x in message.split(",")]
            osc_client.send_message("/state", state)

    async def main():
        async with websockets.serve(handler, "0.0.0.0", common.WEBSOCKETS_PORT):
            await asyncio.Future()

    asyncio.run(main())
