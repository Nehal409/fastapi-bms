import socketio
from combinedSoCApproach import calculate_soc

sio = socketio.AsyncServer(async_mode='asgi')

battery_data_file = 'demo-batteryReadings.csv'
soc_results = calculate_soc(battery_data_file)


@sio.on('connect')
async def on_connection(sid, _, m):
    print(f'{sid}-Client connected')
    await sio.emit('message', soc_results)

@sio.on('disconnect')
def test_disconnect(sid):
    print(f'{sid}-Client disconnected')

def create_socketio_app(app):
    socket_app = socketio.ASGIApp(sio, static_files={'/': 'static/'})
    app.mount('/', socket_app)

