from .base import Base


class CheckNS(Base):

    required = True
    type_name = 'ns'

    @staticmethod
    def on_item(itm):
        return {
            'address': itm['data'],
            'name': itm['data'],
            'ttl': itm['ttl'],
            'measurement_time': itm['measurement_time']
        }
