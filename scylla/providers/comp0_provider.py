from scylla.providers.plain_text_provider import PlainTextProvider

class Comp0Provider(PlainTextProvider):

    def urls(self) -> [str]:
        return [
            'https://sunny9577.github.io/proxy-scraper/proxies.txt',
        ]
