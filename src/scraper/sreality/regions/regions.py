import unicodedata


def remove_diacritic(input):
    '''
    Accept a unicode string, and return a normal string (bytes in Python 3)
    without any diacritical marks.
    '''
    return unicodedata.normalize('NFKD', input).encode('ASCII', 'ignore')


def get_districts(f):
    region = 'praha','stredocesky','karlovarsky','plzensky','jihocesky', 'vysocina','jihomoravsky','zlinsky',\
             'moravskoslezsky','olomoucky','kralovehradecky','liberecky','ustecky'
    with open(f,'r',encoding="utf8") as f:
        input = remove_diacritic((f.read())).decode('utf8').lower().replace(' ','')
        districts = [line for line in input.splitlines() ]
    for d in districts:
        if d in region:
            print(f'"{d}":')
            continue
        else:
            print(f'"{d}",')



if __name__ == '__main__':
    dis = get_districts('regions.txt')
    # print(dis)
