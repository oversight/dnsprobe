from agentcoreclient import IgnoreResultException

from .base import Base
from .utils import dns_query


class CheckPTR(Base):

    required = True
    type_name = 'ptr'

    @classmethod
    async def run_check(cls, fqdn: str, ptr: str, name_servers: list):
        if not ptr:
            raise IgnoreResultException(
                f'{cls.__name__} did not run; ptr is not provided')
        return await dns_query(
            ptr,
            cls.type_name,
            name_servers
        )

    @staticmethod
    def on_item(itm):
        return {
            'address': itm['data'],
            'name': itm['data'],
            'ttl': int(itm['ttl']),
        }
