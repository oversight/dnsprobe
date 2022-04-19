import dns.dnssec
from .base import Base


class CheckDNSKEY(Base):

    required = True
    type_name = 'dnskey'

    @staticmethod
    def on_item(itm):
        data = itm['data'].split(' ')
        _, protocol, algorithm = data[:3]
        key = ''.join(data[3:])
        return {
            'algorithm': int(algorithm),
            # 'flag': itm['flag'],  # TODO not present
            'key': key,
            # 'keyID': itm['keyID'],  # TODO not present
            'name': key,
            'protocol': int(protocol),
            'ttl': int(itm['ttl']),
        }
