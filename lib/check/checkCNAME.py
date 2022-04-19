from .base import Base


class CheckCNAME(Base):

    required = True
    type_name = 'cname'

    @staticmethod
    def on_item(itm):
        return {
            'name': 'cname',
            'address': itm['data'],
            'ttl': itm['ttl'],
        }
