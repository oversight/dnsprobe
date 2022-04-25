from .base import Base


class CheckSOA(Base):

    required = True
    type_name = 'soa'

    @staticmethod
    def on_item(itm):
        primary_ns, responsible_name, serial, refresh, retry, expire, minimum \
            = itm['data'].split(' ')
        return {
            'name': primary_ns,
            'primaryNS': primary_ns,
            'responsibleName': responsible_name,
            'serial': serial,
            'refresh': refresh,
            'retry': retry,
            'expire': expire,
            'minimum': minimum,
            'ttl': int(itm['ttl']),
        }
