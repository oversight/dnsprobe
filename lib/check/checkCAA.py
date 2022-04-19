from .base import Base


class CheckCAA(Base):

    required = True
    type_name = 'caa'

    @staticmethod
    def on_item(itm):
        return {
            'name': itm['data'],
            'record': itm['data'],
            'ttl': itm['ttl'],
        }
