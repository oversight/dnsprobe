from .base import Base


class CheckDS(Base):

    required = True
    type_name = 'ds'

    @staticmethod
    def on_item(itm):
        key_tag, algorithm, digest_type, digest = itm['data'].split(' ')
        return {
            'algorithm': int(algorithm),
            'digest': digest,
            'digestType': int(digest_type),
            'keyTag': int(key_tag),
            'name': key_tag,
            'ttl': int(itm['ttl']),
        }
