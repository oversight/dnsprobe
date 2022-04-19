from .base import Base


class CheckCNAME(Base):

    required = True
    type_name = 'cname'

    @staticmethod
    def on_item(itm):
        # TODO one record
        return {
            'name': 'cname',
            'address': itm['data'],
            'ttl': itm['ttl'],
        }

    @classmethod
    def iterate_results(cls, data: dict):
        itm = cls.on_item(data)

        state = {}
        state[cls.type_name] = itm
        return state
