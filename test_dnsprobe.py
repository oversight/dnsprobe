import asyncio
import unittest

from lib.check import CHECKS


def _get_hostconfig(fqdn, ptr, name_servers):
    return {
        'probeConfig': {
            'dnsProbe': {
                'fqdn': fqdn,
                'ptr': ptr,
                'nameServers': name_servers
            }
        }
    }


def _setup(name, fqdn=None, ptr=None, name_servers=['8.8.8.8']):
    data = {
        'hostUuid': '',
        'checkName': name,
        'hostConfig': _get_hostconfig(fqdn, ptr, name_servers),
    }
    check = CHECKS[name]
    asyncio.run(check.run(data, {}))


class TestProbe(unittest.TestCase):

    def test_check_a(self):
        name = 'CheckA'
        _setup(name, 'siridb.com')

    def test_check_aaaa(self):
        name = 'CheckAAAA'
        _setup(name, 'siridb.com')

    def test_check_caa(self):
        name = 'CheckCAA'
        _setup(name, 'docs.thingsdb.net')

    def test_check_cname(self):
        name = 'CheckCNAME'
        _setup(name, 'docs.thingsdb.net')

    def test_check_ds(self):
        name = 'CheckDS'
        _setup(name, 'siridb.com')

    def test_check_mx(self):
        name = 'CheckMX'
        _setup(name, 'siridb.com')

    def test_check_ns(self):
        name = 'CheckNS'
        _setup(name, 'siridb.com')

    def test_check_ptr(self):
        name = 'CheckPTR'
        _setup(name, ptr='4.4.8.8.in-addr.arpa.')

    def test_check_soa(self):
        name = 'CheckSOA'
        _setup(name, 'cesbit.com')

    def test_check_srv(self):
        name = 'CheckSRV'
        _setup(name, '_sip._tls.o365.test-technology.nl')

    def test_check_txt(self):
        name = 'CheckTXT'
        _setup(name, 'siridb.com')

    def test_check_caa_no_answer(self):
        name = 'CheckCAA'
        _setup(name, 'cesbit.com')


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestProbe('test_check_a'))
    suite.addTest(TestProbe('test_check_aaaa'))
    suite.addTest(TestProbe('test_check_caa'))
    suite.addTest(TestProbe('test_check_cname'))
    suite.addTest(TestProbe('test_check_ds'))
    suite.addTest(TestProbe('test_check_mx'))
    suite.addTest(TestProbe('test_check_ns'))
    suite.addTest(TestProbe('test_check_ptr'))
    suite.addTest(TestProbe('test_check_soa'))
    suite.addTest(TestProbe('test_check_srv'))
    suite.addTest(TestProbe('test_check_txt'))
    suite.addTest(TestProbe('test_check_caa_no_answer'))

    runner = unittest.TextTestRunner()
    runner.run(suite)
