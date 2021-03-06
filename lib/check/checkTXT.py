from .base import Base


class CheckTXT(Base):

    required = True
    type_name = 'txt'

    @staticmethod
    def on_item(itm):
        return {
            'record': itm['data'],
            'name': itm['data'],
            'ttl': int(itm['ttl']),
        }
