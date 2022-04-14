from .base import Base


class CheckSRV(Base):

    required = True
    type_name = 'srv'

    @staticmethod
    def on_item(itm):
        return {
            'address': itm['data'],  # TODO
            'name': itm['data'],  # TODO
            'ttl': itm['ttl'],
            'measurement_time': itm['measurement_time']
        }
