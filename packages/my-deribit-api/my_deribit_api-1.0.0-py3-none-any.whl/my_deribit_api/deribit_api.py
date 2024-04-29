import json
from json import JSONDecodeError
from binance.api import API
import logging
import requests
import multitasking
from time import sleep

from binance.error import ClientError, ServerError

from .constant import GrantType, RetCode, OrderType, TimeInForce

class DeribitAPI(API):
    """API base class

    Keyword Args:
        base_url (str, optional): the API base url, useful to switch to testnet, etc. By default it's https://api.binance.com
        timeout (int, optional): the time waiting for server response, number of seconds. https://docs.python-requests.org/en/master/user/advanced/#timeouts
        proxies (obj, optional): Dictionary mapping protocol to the URL of the proxy. e.g. {'https': 'http://1.2.3.4:8080'}
        show_limit_usage (bool, optional): whether return limit usage(requests and/or orders). By default, it's False
        show_header (bool, optional): whether return the whole response header. By default, it's False
        private_key (str, optional): RSA private key for RSA authentication
        private_key_pass(str, optional): Password for PSA private key
    """
    
    running: bool = True
    refresh_token: str = ''
    expires_in: int = 0
    

    def __init__(
        self,
        api_key=None,
        api_secret=None,
        base_url='https://test.deribit.com/api/v2',
        timeout=None,
        proxies=None,
        show_limit_usage=False,
        show_header=False,
        private_key=None,
        private_key_pass=None,
        client_id=None,
        client_secret=None,
        auto_refresh=True
    ):
        self.api_key = api_key
        self.api_secret = api_secret
        self.base_url = base_url
        self.timeout = timeout
        self.proxies = None
        self.show_limit_usage = False
        self.show_header = False
        self.private_key = private_key
        self.private_key_pass = private_key_pass
        self.client_id = client_id
        self.client_secret = client_secret
        self.session = requests.Session()
        self.session.headers.update(
            {
                "Content-Type": "application/json;charset=utf-8"
            }
        )

        if show_limit_usage is True:
            self.show_limit_usage = True

        if show_header is True:
            self.show_header = True

        if type(proxies) is dict:
            self.proxies = proxies

        self._logger = logging.getLogger(__name__)
        self.auth(auto_refresh=auto_refresh)
    
    def _handle_exception(self, response):
        status_code = response.status_code
        if status_code < 400:
            return
        if 400 <= status_code < 500:
            try:
                err = json.loads(response.text)['error']
            except JSONDecodeError:
                raise ClientError(
                    status_code, None, response.text, None, response.headers
                )
            error_data = err
            if "data" in err:
                error_data = err["data"]
            raise ClientError(
                status_code, err["code"], error_data, response.headers, error_data
            )
        raise ServerError(status_code, response.text)
    
    def stop(self):
        self.running = False
    
    def auth(self, grant_type=GrantType.CLIENT_CREDENTIALS, auto_refresh=True):
        params = {'grant_type': grant_type.value}
        if grant_type == GrantType.CLIENT_CREDENTIALS:
            params.update({'client_id': self.client_id, 'client_secret': self.client_secret})
        elif grant_type == GrantType.REFRESH_TOKEN:
            params.update({'refresh_token': self.refresh_token})

        data = self.send_request('GET', '/public/auth', params)
        if data.get('result'):
            self.session.headers.update({
                "Authorization": f"{data['result']['token_type']} {data['result']['access_token']}"
            })
            self.refresh_token = data['result']['refresh_token']
            self.expires_in = data['result']['expires_in']
        self._logger.info(f'auth:{data}')
        # print(data)
        
        if auto_refresh:
            self.auth_interval()

    @multitasking.task
    def auth_interval(self):
        while self.running:
            sleep(self.expires_in - 60)
            self.auth(grant_type=GrantType.REFRESH_TOKEN, auto_refresh=False)
            

    def request_path(self, method, url_path, params):
        try:
            data = self.send_request(method, url_path, params)
        except Exception as e:
            return RetCode.ERROR, e.error_data
        
        reuslt = data and data.get('result') or None
        
        return RetCode.OK, reuslt 
    
    def get_instrument(self, instrument_name):
        url_path = '/public/get_instrument'
        return self.request_path('GET', url_path, {'instrument_name': instrument_name})

    def get_open_orders_by_instrument(self, instrument_name):
        url_path = '/private/get_open_orders_by_instrument'
        return self.request_path('GET', url_path, {'instrument_name': instrument_name})
    
    def get_open_orders_by_currency(self, currency):
        url_path = '/private/get_open_orders_by_currency'
        return self.request_path('GET', url_path, {'currency': currency})
    
    def get_position(self, instrument_name):
        url_path = '/private/get_position'
        return self.request_path('GET', url_path, {'instrument_name': instrument_name})
    
    def get_positions(self, currency='BTC', kind='option'):
        url_path = '/private/get_positions'
        return self.request_path('GET', url_path, {'currency': currency, 'kind': kind})
    
    def get_account(self, currency='BTC', extended=False):
        url_path = '/private/get_account_summary'
        return self.request_path('GET', url_path, {'currency': currency, 'extended': 'true' if extended else 'false'})
    
    def get_order_book(self, instrument_name, depth=5):
        url_path = '/public/get_order_book'
        return self.request_path('GET', url_path, {'instrument_name': instrument_name, 'depth': depth})
    
    def buy(self, instrument_name, price, amount, type=OrderType.LIMIT, time_in_force=TimeInForce.GTC, label=''):
        url_path = '/private/buy'
        return self.request_path('GET', url_path, {
            'instrument_name': instrument_name,
            'price':price, 'amount': amount,
            'type': type.value,
            'time_in_force': time_in_force.value,
            'label': label
        })
    
    def sell(self, instrument_name, price, amount, type=OrderType.LIMIT, time_in_force=TimeInForce.GTC, label=''):
        url_path = '/private/sell'
        return self.request_path('GET', url_path, {
            'instrument_name': instrument_name,
            'price':price, 'amount': amount,
            'type': type.value,
            'time_in_force': time_in_force.value,
            'label': label
        })
    
    def cancel(self, order_id):
        url_path = '/private/cancel'
        return self.request_path('GET', url_path, {
            'order_id': order_id,
        })
    
 
