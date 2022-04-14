from .base import Base

class CheckDS(Base):

    required = True
    type_name = 'ds'

    @staticmethod
    def on_item(itm):
        key_tag, algorithm, digest_type, digest = itm['data'].split(' ')
        return {
            'algorithm': algorithm,
            'digest': digest,
            'digestType': digest_type,
            'keyTag': key_tag,
            'name': key_tag,
            'ttl': itm['ttl'],
            'measurement_time': itm['measurement_time']
        }
