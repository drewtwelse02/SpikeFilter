import asyncio
import websockets

# Async generator to read a file line by line with a delay
async def stream_file(path, queue, delay=1):
    with open(path, 'r') as f:
        for line in f:
            await asyncio.sleep(delay)  # simulate streaming
            await queue.put((path, line.strip()))

# WebSocket handler
async def handler(websocket, path):
    queue = asyncio.Queue()

    # Start streaming both files concurrently
    producer1 = asyncio.create_task(stream_file('data/NEWS_2025-05-14.csv', queue, delay=0.2))
    producer2 = asyncio.create_task(stream_file('data/SPIKE_2025-05-14.csv', queue, delay=0.3))

    # Wait until both are done, and stream data to the client
    while not (producer1.done() and producer2.done() and queue.empty()):
        try:
            source, data = await asyncio.wait_for(queue.get(), timeout=5)
            message =data
            await websocket.send(message)
        except asyncio.TimeoutError:
            break

    await websocket.send("Streaming completed.")

# Start the server
async def main():
    async with websockets.serve(handler, "localhost", 8765):
        print("Server started at ws://localhost:8765")
        await asyncio.Future()  # run forever

asyncio.run(main())
