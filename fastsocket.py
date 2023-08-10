import socketio

sio = socketio.AsyncServer(async_mode='asgi')

data = [{
    "name": "nn",
    "age": 22
}]

@sio.on('connect')
async def on_connection(sid, _, m):
    print(f'{sid}-Client connected')
    await sio.emit('message', data)

@sio.on('disconnect')
def test_disconnect(sid):
    print(f'{sid}-Client disconnected')

def create_socketio_app(app):
    socket_app = socketio.ASGIApp(sio, static_files={'/': 'static/'})
    app.mount('/', socket_app)

