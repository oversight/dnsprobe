import asyncio
import copy
import dns.asyncresolver
import dns.message
import logging


def make_rr(simple, rdata):
    csimple = copy.copy(simple)
    csimple["data"] = rdata.to_text()
    return csimple


def flatten_rrset(rrs):
    simple = {}
    if len(rrs) > 0:
        simple["ttl"] = rrs.ttl
        return [make_rr(simple, rdata) for rdata in rrs]
    else:
        return [simple]


def to_dict(message):
    simple = []
    for rrs in message.answer:
        simple.extend(flatten_rrset(rrs))
    return simple


async def dns_query(name, query_type):
    try:
        aresolver = dns.asyncresolver.Resolver()
        # TODO REMOVE following line; used to test code for DS and DNSKEY;
        # due to ubuntu issue:
        # "dns.resolver.NoNameservers: All nameservers failed to answer the
        # query siridb.com. IN DNSKEY: Server 127.0.0.53 TCP port 53 answered
        # [Errno 99] Cannot assign requested address"
        aresolver.nameservers = ['8.8.8.8']

        start = asyncio.get_event_loop().time()
        a = await aresolver.resolve(name, query_type)
        measurement_time = asyncio.get_event_loop().time() - start
    except Exception as err:
        logging.exception(err)
    else:
        response = to_dict(a.response)
        response['measurement_time'] = measurement_time
        return to_dict(a.response)
