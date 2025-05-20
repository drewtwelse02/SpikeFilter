import websocket
import MessageHandler
import DBHandler
import asyncio
class MyWebSocketClient:
    def __init__(self, url):
        self.msg_h      = MessageHandler.MsgHandler()
        self.db_handler = DBHandler.DB()
        self.ws = websocket.WebSocketApp(
            url,
            on_open   =self.on_open,
            on_message=self.on_message,
            on_error  =self.on_error,
            on_close  =self.on_close
        )

    def on_message(self, ws, message):
        #print("On Message")
        self.msg_h.filter_message(message,self.db_handler)

    def on_error(self, ws, error):
        print(f"Error: {error}")

    def on_close(self, ws, close_status_code, close_msg):
        print("Connection closed")

    def on_open(self, ws):
        print("Connection opened")
        ws.send("Hello, Server!")

    def run(self):
        self.ws.run_forever()


client = MyWebSocketClient("ws://localhost:8765")
asyncio.run(client.run())
