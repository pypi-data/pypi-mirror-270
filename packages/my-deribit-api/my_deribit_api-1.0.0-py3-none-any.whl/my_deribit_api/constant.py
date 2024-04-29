from enum import Enum

class GrantType(Enum):
    CLIENT_CREDENTIALS = 'client_credentials'
    CLIENT_SIGNATURE = 'client_signature'
    REFRESH_TOKEN = 'refresh_token'

class RetCode(Enum):
    OK = 'ok'
    ERROR = 'error'

class SubscribeType(Enum):
    TICK = 'TICK'
    BOOK = 'BOOK'
    TRADE = 'TRADE'
    USER_ORDER = 'USER_ORDER'
    USER_TRADE = 'USER_TRADE'
    USER_CHANGE = 'USER_CHANGE'

class TimeInForce(Enum):
    GTC = 'good_til_cancelled'
    GTD = 'good_til_day'
    FOK = 'fill_or_kill'
    IOC = 'immediate_or_cancel'

class OrderType(Enum):
    LIMIT = 'limit'
    MARKET = 'market'

class Status(Enum):
    OPEN = 'open'
    FILLED = 'filled'
    REJECTED = 'rejected'
    CANCELLED = 'cancelled'
    UNTRIGGERED = 'untriggered'