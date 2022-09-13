class SeleniumExceptions(Exception):
    def __init__(self, url, message):
        self.url = url
        self.message = message


class PageIsNotLoaded(SeleniumExceptions):
    def __init__(self, *, url, message='Page is not leaded'):
        super(PageIsNotLoaded, self).__init__(url=url, message=message)
