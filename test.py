import requests

if __name__ == '__main__':
    url1 = 'http://subtitle.v.geilijiasu.com/FF/C5/FFC5529A57CA777215B20C31056569D31BDD6D1A.ass'
    url2 = 'http://subtitle.v.geilijiasu.com/C5/1A/C51A449FE0D01F9C61175D31256C5D8F9CCE1CCC.ass'

    r1 = requests.get(url1)
    r2 = requests.get(url2)
