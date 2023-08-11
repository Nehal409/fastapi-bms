from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastsocket import create_socketio_app
from combinedSoCApproach import calculate_soc

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

# battery_data_file = 'demo-batteryReadings.csv'
# soc_results = calculate_soc(battery_data_file)

# for results in soc_results:
#     print(f"Timestamp: {results['Timestamp']}")
#     print(f"Coulomb Counting SoC: {results['Coulomb Counting SoC']:.4f}")
#     print(f"Voltage-Based SoC (OCV): {results['Voltage-Based SoC (OCV)']:.4f}")
#     print(f"Combined SoC: {results['Combined SoC']:.4f}")
#     print("---------------------")


create_socketio_app(app)

