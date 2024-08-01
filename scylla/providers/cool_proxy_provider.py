import re

from pyquery import PyQuery

from scylla.database import ProxyIP
from .base_provider import BaseProvider


class CoolProxyProvider(BaseProvider):

    def parse(self, document: PyQuery) -> [ProxyIP]:
        ip_list: [ProxyIP] = []

        for ip_row in document.find('table tr'):
            ip_row: PyQuery = ip_row
            ip_element: PyQuery = ip_row.find('td:nth-child(1)')
            port_element: PyQuery = ip_row.find('td:nth-child(2)')

            if ip_element and port_element:
                p = ProxyIP(ip=re.sub(r'document\.write\(.+\)', '', ip_element.text()), port=port_element.text())

                ip_list.append(p)

        return ip_list

    def urls(self) -> [str]:
        return [
            'https://www.cool-proxy.net/',
        ]

    @staticmethod
    def should_render_js() -> bool:
        return True
