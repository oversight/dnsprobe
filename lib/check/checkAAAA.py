from .base import Base


class CheckAAAA(Base):

    required = True
    type_name = 'aaaa'

    @staticmethod
    def on_item(itm):
        return {
            'name': itm['data'],
            'address': itm['data'],
            'ttl': itm['ttl'],
        }
