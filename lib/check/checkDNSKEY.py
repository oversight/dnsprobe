import dns.dnssec
from .base import Base


class CheckDNSKEY(Base):

    required = True
    type_name = 'dnskey'

    @staticmethod
    def on_item(itm):
        _, protocol, algorithm = itm['data'].split(' ')[:3]
        key = ''.join(key[3:])
        return {
            'algorithm': algorithm,
            # 'flag': itm['flag'],  # TODO not present
            'key': key,
            # 'keyID': itm['keyID'],  # TODO not present
            'name': dns.dnssec.key_id(key),
            'protocol': protocol,
            'ttl': itm['ttl'],
        }
