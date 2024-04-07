from DrissionPage._pages.web_page import WebPage

tags = ['naruto','ahegao']  # 标签
exclude_tags = ['-yaoi', '-male_penetrated'] # 排除的标签(加个-)
save_path = r'C:\Users\GMH\Desktop\data'  # 保存路径
page_num = 5  # 爬取多少页,None时为全部

if not tags:
    full_tag = 'all' + '+' + '+'.join(exclude_tags)
else:
    full_tag = '+'.join(tags) + '+' + '+'.join(exclude_tags)
url = f'https://rule34.xxx/index.php?page=post&s=list&tags={full_tag}&pid=0'

# 创建网页对象
page = WebPage()
page.get(url)
# 获取最后一页页数
page.ele('t:a@alt=last page').click()
all_page_num = page.ele('#paginator').ele('t:b').text
if page_num is None:
    page_num = all_page_num
# 切换为session模式
page.get(url)
page.change_mode('s')
# 保存每一页的图片
for i in range(page_num):
    # 获取全部缩略图元素
    thumbs = page.eles('t:span@class=thumb')
    for thumb in thumbs:
        # 获取每张图的下载url
        new_url = thumb.ele('t:a').link
        page.get(new_url)
        img_ele = page.ele('.flexi').ele('t:img')
        # 跳过视频
        if img_ele:
            download_url = img_ele.link
            if 'jpg' in download_url:
                pic_id = download_url.split('.jpg?')[1]
            elif 'png' in download_url:
                pic_id = download_url.split('.png?')[1]
            page.download(download_url, save_path, file_exists='skip', rename=pic_id)
    # 翻页
    page.get(f'https://rule34.xxx/index.php?page=post&s=list&tags={full_tag}&pid={(i + 1) * 42}')
