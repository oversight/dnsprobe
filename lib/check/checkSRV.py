from .base import Base


class CheckSRV(Base):

    required = True
    type_name = 'srv'

    @staticmethod
    def on_item(itm):
        priority, weight, port, target = itm['data'].split(' ')
        return {
            'name': target,
            'port': port,
            'priority': priority,
            'target': target,
            'ttl': itm['ttl'],
            'weight': weight,
        }
