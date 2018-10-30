import argparse

import nmap

from base import BaseCommand


class Command(BaseCommand):
    def add_args(self, parser: argparse.ArgumentParser):
        parser.add_argument('host')

    def handle(self, *args, **kwargs):
        host = kwargs.pop('host')
        nm = nmap.PortScanner()

        nm.scan(host, arguments='-sP')

        th = ['IPv4', 'MAC', 'State', 'Vendor']
        row_style = '{:<20}' * len(th)
        dash = '-' * 80

        print(row_style.format(*th))
        print(dash)
        for h in nm.all_hosts():

            if 'mac' in nm[h]['addresses']:
                addr = nm[h]['addresses']
                mac = addr['mac']
                vendors = nm[h]['vendor']
                ven = vendors[mac] if mac in vendors else 'Unknown'
                status = nm[h]['status']

                print(row_style.format(h, mac, status['state'], ven))
