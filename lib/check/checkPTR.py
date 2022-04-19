import dns.reversename

from .base import Base
from .utils import dns_query


class CheckPTR(Base):

    required = True
    type_name = 'ptr'

    @classmethod
    async def run_check(cls, ip_address: str):
        return await dns_query(
            dns.reversename.from_address(ip_address),
            cls.type_name
        )

    @staticmethod
    def on_item(itm):
        return {
            'address': itm['data'],
            'name': itm['data'],
            'ttl': itm['ttl'],
        }
