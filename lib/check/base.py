import asyncio
import logging

from agentcoreclient import IgnoreResultException
from dns.resolver import NoAnswer

from .utils import dns_query


class Base:
    type_name = None
    interval = 300
    required = False

    @classmethod
    async def run(cls, data, asset_config=None):
        try:
            asset_id = data['hostUuid']
            config = data['hostConfig']['probeConfig']['dnsProbe']
            fqdn = config.get('fqdn', None)
            ptr = config.get('ptr', None)
            name_servers = config.get('nameServers', None)
            interval = data.get('checkConfig', {}).get('metaConfig', {}).get(
                'checkInterval')
            assert interval is None or isinstance(interval, int)
        except Exception as err:
            logging.error(f'invalid check configuration: `{err}`')
            return

        max_runtime = .8 * (interval or cls.interval)
        try:
            state_data = await asyncio.wait_for(
                cls.get_data(fqdn, ptr, name_servers),
                timeout=max_runtime
            )
        except asyncio.TimeoutError:
            raise Exception('Check timed out.')
        except NoAnswer:
            raise IgnoreResultException
        except IgnoreResultException:
            raise
        except Exception as err:
            raise Exception(f'Check error: {err.__class__.__name__}: {err}')
        else:
            return state_data

    @classmethod
    async def get_data(cls, fqdn: str, ptr: str, name_servers: list):
        data, measurement_time = await cls.run_check(
            fqdn, ptr, name_servers)

        state = cls.iterate_results(data, measurement_time)
        return state

    @classmethod
    async def run_check(cls, fqdn: str, ptr: str, name_servers: list):
        if not fqdn:
            raise IgnoreResultException(
                f'{cls.__name__} did not run; fqdn is not provided')
        return await dns_query(fqdn, cls.type_name, name_servers)

    @staticmethod
    def on_item(itm: dict):
        return itm

    @classmethod
    def on_items(cls, itms: list):
        out = {}
        for i in itms:
            itm = cls.on_item(i)
            name = itm['name']
            out[name] = itm
        return out

    @classmethod
    def iterate_results(cls, data: list, measurement_time: float):
        itms = cls.on_items(data)
        state = {}
        state[cls.type_name] = itms
        state['stat'] = {
            'timeit': {
                'name': 'timeit',
                'measuredTime': measurement_time
            }
        }
        return state
