from .base import Base


class CheckSOA(Base):

    required = True
    type_name = 'soa'

    @staticmethod
    def on_item(itm):
        # TODO metrics?
        primary_ns, email = itm['data'].split(' ')[:2]
        return {
            'email': email,
            'name': primary_ns,
            'primaryNS': primary_ns,
            'ttl': itm['ttl'],
        }
