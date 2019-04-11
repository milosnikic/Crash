from bs4 import BeautifulSoup


def make_header(html):
    soup = BeautifulSoup(html, 'html')
    c = 0
    with open('crash_dataset.data', 'w+') as f:
        header = []
        for i in soup.findAll('td'):
            if c % 2 == 0:
                # Populate header
                h = i.text.strip()
                header.append(h)
            c += 1
        f.write(','.join(header) + '\n')


def write_features(html):
    soup = BeautifulSoup(html, 'html')
    c = 0
    with open('crash_dataset.data', 'a') as f:
        features = []
        for i in soup.findAll('td'):
            if c % 2 == 1:
                feature = i.text.strip()
                print(feature, c)
                if c % 5 == 0:
                    feature = feature.lstrip('x')
                features.append(feature)
            c += 1
        f.write(','.join(features) + '\n')
