import csv
import requests
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}

csvTitle = ['排名', '片名', '主演', '上映时间', '评分']


def append_to_csv(data, csv_filename, fieldnames) -> None:
    with open(csv_filename, 'a', newline='',encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        # 如果文件为空，先写入表头
        if csv_file.tell() == 0:
            writer.writeheader()
        # 写入新行数据
        writer.writerow(data)


def getHtml(url) -> str | None:
    r = requests.get(url, headers=headers)
    if r.status_code == 200:
        return r.text
    return None


def parsePage(html) -> iter:
    soup = BeautifulSoup(html, 'lxml')
    all_info = soup.findAll(name="dd")
    for info in all_info:
        rank = info.find('i', class_='board-index').get_text(strip=True)
        moveName = info.find('a', class_="image-link")["title"]
        actor = info.find('p', class_="star").get_text(strip=True).replace('主演：', '').strip()
        time = info.find('p', class_="releasetime").get_text(strip=True).replace('上映时间：', '').strip()
        score = info.find('i', class_="integer").get_text(strip=True) + info.find('i', class_="fraction").get_text(
            strip=True)
        yield [rank, moveName, actor, time, score]


def createData(iterable) -> list:
    keys = ['排名', '片名', '主演', '上映时间', '评分']
    plist = []
    for item in iterable:
        pdict = dict(zip(keys, item))
        plist.append(pdict)
    return plist

def getUrl(i) -> str:
    return 'http://maoyan.com/board/4' + f'?offset={10*i}'

def main():
    csv_filename = 'output.csv'
    '''with open('h.html', 'r', encoding='utf-8') as file:
        html = file.read()'''
    for i in range(10):
        url = getUrl(i)
        html = getHtml(url)
        if html:
            with open(f'output{i}.html', 'w', encoding='utf-8') as output_file:
                output_file.write(html)
            datas = createData(parsePage(html))
            for data in datas:
                append_to_csv(data, csv_filename, csvTitle)
        else:
            print("got nothing!")


if __name__ == "__main__":
    main()
