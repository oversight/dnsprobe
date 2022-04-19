import asyncio
import logging

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
            ip4 = config['ip4']
            fqdn = config['fqdn']
            dns_server = config['dnsServer']
            interval = data.get('checkConfig', {}).get('metaConfig', {}).get(
                'checkInterval')
            assert interval is None or isinstance(interval, int)
        except Exception as e:
            logging.error(f'invalid check configuration: `{e}`')
            return

        max_runtime = .8 * (interval or cls.interval)
        try:
            state_data = await asyncio.wait_for(
                cls.get_data(fqdn),
                timeout=max_runtime
            )
        except asyncio.TimeoutError:
            raise Exception('Check timed out.')
        except Exception as e:
            raise Exception(f'Check error: {e.__class__.__name__}: {e}')
        else:
            return state_data

    @classmethod
    async def get_data(cls, fqdn: str):
        data = []
        try:
            data = await cls.run_check(fqdn, cls.type_name)
            # TODO if None? return None?
            if data is None:
                return None
        except Exception:
            logging.exception('DNS query error\n')
            raise

        try:
            state = cls.iterate_results(data)
        except Exception:
            logging.exception('DNS parse error\n')
            raise

        return state

    @classmethod
    async def run_check(cls, fqdn: str):
        return await dns_query(fqdn, cls.type_name)


    @classmethod
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
    def iterate_results(cls, data: list):
        itms = cls.on_items(data)

        state = {}
        state[cls.type_name] = itms
        return state
