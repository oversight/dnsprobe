from .base import Base


class CheckA(Base):

    required = True
    type_name = 'a'

    @staticmethod
    def on_item(itm):
        return {
            'name': itm['data'],
            'address': itm['data'],
            'ttl': itm['ttl'],
            'measurement_time': itm['measurement_time']
        }
