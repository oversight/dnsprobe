from .base import Base


class CheckSRV(Base):

    required = True
    type_name = 'srv'

    @staticmethod
    def on_item(itm):
        priority, weight, port, target = itm['data'].split(' ')
        return {
            'name': target,
            'port': int(port),
            'priority': int(priority),
            'target': target,
            'ttl': int(itm['ttl']),
            'weight': int(weight),
        }
