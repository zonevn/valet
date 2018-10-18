from library import DataSet, InputOption


def getstate():
    task = DataSet()
    print(task.data)


def extract():
    import requests
    from lxml import html

    option = InputOption()

    if not hasattr(option, 'url'):
        raise Exception("Url Not Found.")
    if not hasattr(option, 'attr'):
        raise Exception("Attribute Not Found.")

    url = getattr(option, 'url')
    attr = getattr(option, 'attr')
    print(option.__dict__)
    req = requests.get(url)
    res = html.fromstring(req.content)
    for line in res.xpath(attr):
        print(line)


