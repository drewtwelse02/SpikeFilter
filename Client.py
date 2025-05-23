import websocket

def on_message(ws, message):
    print(f"Received: {message}")

def on_error(ws, error):
    print(f"Error: {error}")

def on_close(ws, close_status_code, close_msg):
    print("Connection closed")

def on_open(ws):
    print("Connection opened")
    ws.send("Hello, Server!")

if __name__ == "__main__":
    ws = websocket.WebSocketApp("ws://localhost:8765",
                                 on_open=on_open,
                                 on_message=on_message,
                                 on_error=on_error,
                                 on_close=on_close)

    ws.run_forever()