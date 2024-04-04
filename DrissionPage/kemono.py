import os.path

from DrissionPage import SessionPage

url = 'https://kemono.su/fanbox/user/6570768'
save_path = r'C:\Users\GMH\Desktop\data'
download_downloads = False
download_content = True
download_files = True


def make_dir(path):
    if os.path.exists(path):
        pass
    else:
        os.makedirs(path)


def deal_each_page(page_obj, _save_path):
    # 下载Downloads
    downloads = page_obj.eles('t:a@class=post__attachment-link')
    if downloads:
        if download_downloads:
            for download in downloads:
                page_obj.download(download.link, _save_path)
        else:
            with open(_save_path + '\\downloads.txt', 'a', encoding='ANSI') as f:
                for download in downloads:
                    f.write(download.link)

    # 下载文Content
    content = page_obj.ele('t:div@class=post__content')
    if content:
        if download_content:
            with open(_save_path + '\\content.txt', 'w',encoding='utf-8') as f:
                f.write(content.text)

    # 下载Files
    files = page_obj.eles('t:a@class=fileThumb')
    if files:
        if download_files:
            for file in files:
                page_obj.download(file.link, _save_path)
        else:
            with open(_save_path + '\\files.txt', 'a', encoding='ANSI') as f:
                for file in files:
                    f.write(file.link)


def main():
    # 创建网页对象
    page = SessionPage()
    page.get(url)

    # 获取信息
    artist = page.ele('t:span@itemprop=name').text
    page_num = page.ele('#paginator-top').ele('t:small').text.split(' ')[-1]
    page_num = int(int(page_num) / 50)

    # 翻页爬取信息
    for i in range(page_num + 1):
        print(f'正在处理第{i + 1}页信息...')

        # 获取全部文章链接
        page.get(url + f'?o={str(i * 50)}')
        items = page.eles('t:article@class=post-card post-card--preview')[:3]
        links = [item.ele('t:a').link for item in items]

        # 爬取每篇文章里的数据
        all_num = len(links)
        current_num = 1
        for link in links:
            # 发送请求
            page.get(link)

            # 获取标题并创建对应文件夹
            title = page.ele('.post__title').eles('t:span')[0].text
            print(f'{current_num}-{all_num}.{title}')
            _save_path = os.path.join(save_path, artist)
            _save_path = os.path.join(_save_path, title)
            make_dir(_save_path)

            # 下载内容
            deal_each_page(page, _save_path)

            current_num += 1
            print('\n')


main()
