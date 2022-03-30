GestureServer
=============

GestureServer is a really quick and dirty way to use your phone as a multitouch OSC interface if both your phone and computer are connected to the same network.

Workflow:

- Launch your favorite OSC synthesizer.
- Launch the WebSocket server (`python websocket_server.py`) and Web server (`flask run`).
- Run `python qr_code.py` to produce a QR code in your terminal. (Use `python qr_code.py -i` if you're using a light theme.)
- Scan the QR code with your phone to visit a Web page that streams multitouch data to the WebSocket server.
