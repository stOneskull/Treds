from zipfile import ZipFile


def zipbook(thezip):
    book = {}

    with ZipFile(thezip) as zipbob:
        for name in zipbob.namelist():
            if name.endswith('/'):
                chapter = name[:-1]
                book[chapter] = {}
                continue

            with zipbob.open(name) as scrib:
                page = name.split('/')[1]
                book[chapter][page] = [
                line.decode().rstrip() for line in scrib
                ]

    return book


pics = zipbook('pics.zip')
texts = zipbook('texts.zip')


if __name__ == "__main__":
    for chapter in pics:
        for pic in pics[chapter]:
            for line in pics[chapter][pic]:
                print(line)

