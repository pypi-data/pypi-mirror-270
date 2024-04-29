##########################################################################
##  Deribit Socket API

from binance.websocket.websocket_client import BinanceWebsocketClient
from typing import Optional
import json

from binance.websocket.binance_socket_manager import BinanceSocketManager
from enum import Enum

from websocket import (
    ABNF,
    create_connection,
    WebSocketException,
    WebSocketConnectionClosedException,
    WebSocketTimeoutException,
)

from .constant import SubscribeType, TimeInForce

class DeribitSocketManager(BinanceSocketManager):
    running: bool = True

    def _handle_heartbeat(self, op_code, frame):
        data = json.loads(frame.data)
        if data.get('method') == 'heartbeat' and data['params']['type'] == 'test_request':
            self._callback(self.on_ping)
            self.pong()
            self.logger.debug("Received Ping; PONG frame sent back")
        elif data.get('result') and isinstance(data['result'], dict) and data['result'].get('version'):
            self.logger.debug("Received PONG frame")
            self._callback(self.on_pong)

    def pong(self):
        msg = {
            "jsonrpc" : "2.0",
            "method" : "public/test"
        }
        self.send_message(json.dumps(msg))

    def read_data(self):
        data = ""
        while self.running:
            try:
                op_code, frame = self.ws.recv_data_frame(True)
            except WebSocketException as e:
                if isinstance(e, WebSocketConnectionClosedException):
                    self.logger.error("Lost websocket connection")
                elif isinstance(e, WebSocketTimeoutException):
                    self.logger.error("Websocket connection timeout")
                else:
                    self.logger.error("Websocket exception: {}".format(e))
                raise e
            except Exception as e:
                self.logger.error("Exception in read_data: {}".format(e))
                raise e

            self._handle_data(op_code, frame, data)
            self._handle_heartbeat(op_code, frame)

            if op_code == ABNF.OPCODE_CLOSE:
                self.logger.warning(
                    "CLOSE frame received, closing websocket connection"
                )
                self._callback(self.on_close)
                break

    def stop(self):
        self.running = False

class DeribitWebsocketClient(BinanceWebsocketClient):
    def _initialize_socket(
        self,
        stream_url,
        on_message,
        on_open,
        on_close,
        on_error,
        on_ping,
        on_pong,
        logger,
        timeout,
        proxies,
    ):
        return DeribitSocketManager(
            stream_url,
            on_message=on_message,
            on_open=on_open,
            on_close=on_close,
            on_error=on_error,
            on_ping=on_ping,
            on_pong=on_pong,
            logger=logger,
            timeout=timeout,
            proxies=proxies,
        )
    
    def stop(self):
        self.socket_manager.stop()


class DeribitWebsocketStreamClient(DeribitWebsocketClient):
    def __init__(
        self,
        stream_url="wss://test.deribit.com/ws/api/v2",
        on_message=None,
        on_open=None,
        on_close=None,
        on_error=None,
        on_ping=None,
        on_pong=None,
        is_combined=False,
        timeout=None,
        logger=None,
        proxies: Optional[dict] = None,
        heartbeat_interval: int = 300,
        client_id = None,
        client_secret = None,
    ):

        super().__init__(
            stream_url,
            on_message=on_message,
            on_open=on_open,
            on_close=on_close,
            on_error=on_error,
            on_ping=on_ping,
            on_pong=on_pong,
            timeout=timeout,
            logger=logger,
            proxies=proxies,
        )
        self.client_id = client_id
        self.client_secret = client_secret
        self.set_heartbeat(interval=heartbeat_interval)
        self.auth(client_id, client_secret)

    def set_heartbeat(self, interval=10):
        msg = {
            "jsonrpc" : "2.0",
            "method" : "public/set_heartbeat",
            "params" : {
                "interval" : interval
            }
        }
        self.send(msg)

    def get_instrument(self, instrument_name: str):
        msg = {
            "method" : "public/get_instrument",
            "params" : {
                "instrument_name" : instrument_name
            },
            "jsonrpc" : "2.0"
        }
        self.send(msg)

    def get_open_orders(self, instrument_name):
        msg = {
            "jsonrpc" : "2.0",
            "method" : "private/get_open_orders_by_instrument",
            "params" : {
                "instrument_name" : instrument_name
            }
        }
        self.send(msg)

    def subscribe(self, instrument_name, interval='raw', types = [SubscribeType.TICK, SubscribeType.BOOK, SubscribeType.USER_ORDER , SubscribeType.USER_TRADE]):
        channels = []
        for type in types:
            if type == SubscribeType.TICK:
                channels.append(f'ticker.{instrument_name}.{interval}')
            elif type == SubscribeType.BOOK:
                channels.append(f'book.{instrument_name}.{interval}')
            elif type == SubscribeType.TRADE:
                channels.append(f'trades.{instrument_name}.{interval}')
            elif type == SubscribeType.USER_ORDER:
                channels.append(f'user.orders.any.any.{interval}')
            elif type == SubscribeType.USER_TRADE:
                channels.append(f'user.trades.any.any.{interval}')
            elif type == SubscribeType.USER_CHANGE:
                channels.append(f'user.changes.any.any.{interval}')

        msg = {
            "method" : "public/subscribe",
            "params": {
                "channels": channels
            },
            "jsonrpc" : "2.0"
        }
        self.send(msg)

    def auth(self, client_id, client_secret):
        msg = {
            "jsonrpc" : "2.0",
            "id" : 9929,
            "method" : "public/auth",
            "params" : {
                "grant_type" : "client_credentials",
                "client_id" : client_id,
                "client_secret" : client_secret
            }
        }
        self.send(msg)

    def order(self, instrument_name, price, amount, time_in_force: TimeInForce=TimeInForce.IOC, label=''):
        msg = {
            "jsonrpc" : "2.0",
            "method" : "private/buy",
            "params" : {
                "instrument_name" : instrument_name,
                "price": price,
                "amount": amount,
                "type": "limit",
                "time_in_force": time_in_force.value,
                "label": label
            }
        }
        self.send(msg)




  