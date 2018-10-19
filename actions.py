from library import DataSet, InputOption
from settings import PATH


def status():
    dataset = DataSet()
    print(dataset.data)


def extract():
    docs = "Usage: valet extract -d url attr [saveas]"
    import requests
    from lxml import html

    option = InputOption()
    assert hasattr(option, 'url'), '\n'.join(["URL not found.", docs])
    assert hasattr(option, 'attr'), '\n'.join(["Attributes not found.", docs])

    url = getattr(option, 'url')
    attr = getattr(option, 'attr')
    saveas = getattr(option, 'saveas') if hasattr(option, 'saveas') else None

    print(option.__dict__)
    response = requests.get(url)
    tree = html.fromstring(response.content)

    extracts = tree.xpath(attr)

    if saveas is not None:
        f_open = open(PATH['download'] + saveas, 'w', encoding='utf-8')
        f_open.writelines([line + '\n' for line in extracts])
        f_open.close()

    for line in extracts:
        print(line)
