import json
from src.my_deribit_api.deribit_websocket import (
    DeribitWebsocketStreamClient
)


with open('tests/config.json') as fs:
    config = json.load(fs)

def on_message(x, y):
    print(f'on_message:{y}')

def on_ping(x):
    print(f'on_message:{x}')

def on_pong(x):
    print(f'on_message:{x}')

ws = DeribitWebsocketStreamClient(client_id=config['client_id'], client_secret=config['client_secret'], on_message=on_message, on_ping=on_ping, on_pong=on_pong)
# ws.auth('l3gSQPH-', 'v1c4QjbNxwhiTTHooXCjg61bhO_KB_69FJWTdBdwUSo')
# ws.subscribe("BTC-26APR24-66000-C")
# ws.get_instrument('BTC-26APR24-66000-C')
instrument_name = "BTC-26APR24-66000-C"
# ws.subscribe(instrument_name, sub_types=[SubscribeType.TRADE])
# ws.order(instrument_name, 0.033, 39, label='test_order', time_in_force=TimeInForce.IOC)
ws.get_open_orders(instrument_name)