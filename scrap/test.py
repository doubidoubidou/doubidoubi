import requests

url = 'https://i1.wp.com/qpic.ws/images/2023/08/14/AKlhTe.jpg?ssl=1'  # 图片URL
response = requests.get(url)
print(response.content)
