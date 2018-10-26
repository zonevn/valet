import argparse

import nmap
from nmap import PortScanner

from base import BaseCommand


class Command(BaseCommand):
    def add_args(self, parser: argparse.ArgumentParser):
        parser.add_argument("ips")

    def handle(self, *args, **kwargs):
        IPs = kwargs.pop('ips')
        nm = nmap.PortScanner()
        print("Scanning...")
        nm.scan(IPs, arguments='-sP')

        th = ['addr', 'mac', 'ven', 'stat']
        row_format = "{:>15}" * (len(th) + 1)
        print(row_format.format(*th))
        for h in nm.all_hosts():
            if 'mac' in nm[h]['addresses']:
                addr = nm[h]['addresses']
                ipv4 = addr['ipv4']
                mac = addr['mac']
                ven = nm[h]['vendor']
                status = nm[h]
                row = [ipv4, mac, ven[mac], status['state']]
                print(row_format.format(*row))
