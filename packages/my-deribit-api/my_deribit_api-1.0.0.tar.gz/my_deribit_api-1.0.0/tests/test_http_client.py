import json
from src.my_deribit_api.deribit_api import (
    DeribitAPI,
    RetCode
)


with open('tests/config.json') as fs:
    config = json.load(fs)

api = DeribitAPI(base_url='https://test.deribit.com/api/v2', client_id=config['client_id'], client_secret=config['client_secret'], auto_refresh=False)
instrument_name = "BTC-26APR24-66000-C"
# ret_code, data = api.get_open_orders(instrument_name)
# print(ret_code, data)
# ret_code, data = api.get_instrument(instrument_name)
# print(ret_code, data)
# ret_code, data = api.get_position(instrument_name)
# print(ret_code, data)
# print(instrument_name)
# ret_code, data = api.get_positions()
# print(ret_code, data)
ret_code, data = api.get_account()
print(ret_code, data)

def test_http_api():
    assert 'client_id' in config
    assert ret_code == RetCode.OK