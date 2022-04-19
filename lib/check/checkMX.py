from .base import Base

class CheckMX(Base):

    required = True
    type_name = 'mx'

    @staticmethod
    def on_item(itm):
        preference, address = itm['data'].split(' ')
        return {
            'address': address,
            'name': address,
            'preference': int(preference),
            'ttl': int(itm['ttl']),
        }
