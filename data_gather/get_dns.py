import json
import time
from typing import AnyStr, List, Dict

import dns.resolver
from dns import resolver


class HostnameResolver:
    hostnames_file_path = 'hostnames.json'

    def __init__(self):
        self.resolver = resolver.Resolver()
        self.dns_records = {}
        self.timed_outs = []
        self.hostnames = self.load_hostnames(self.hostnames_file_path)

    def exec(self):
        self.dns_records, self.timed_outs = self.resolve_list(self.hostnames)
        timed_out_results, _ = self.resolve_list(self.timed_outs)
        self.dns_records.update(timed_out_results)
        self.save_dns_records(self.dns_records)

    @staticmethod
    def save_dns_records(dns_records):
        json.dump(dns_records, open('data_gather/dns_results.json', 'w'))

    @staticmethod
    def load_hostnames(path: AnyStr) -> List[AnyStr]:
        hostnames = json.load(open(path, 'r'))
        return hostnames

    def resolve_list(self, hostnames: List[AnyStr]) -> (Dict, List[AnyStr]):
        dns_records = {}
        timed_outs = []
        for hostname in hostnames:
            print("Resolving " + hostname + " ...")
            try:
                answer: resolver.Answer = self.resolver.resolve(hostname)
                for item in answer:
                    dns_records[hostname] = [str(item)] + dns_records.get(hostname, [])
            except dns.resolver.LifetimeTimeout:
                print("Timeout -> " + hostname)
                time.sleep(2)
                timed_outs.append(hostname)
            except (dns.resolver.NoAnswer, dns.resolver.NXDOMAIN, dns.resolver.NoNameservers):
                continue
        return dns_records, timed_outs


if __name__ == '__main__':
    HostnameResolver().exec()