import requests
from bs4 import BeautifulSoup

# header必须正确
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}
# 用户A的歌单 注意是没有#的形式
nn163_cloud_url1 = 'http://music.163.com/playlist?id=749512938'
# 获取我们需要的数据
s = requests.session()
bs1 = BeautifulSoup(s.get(nn163_cloud_url1, headers=headers).content, "lxml")

# 用户A的歌单list
songA = []
for i in bs1.ul.children:
    songA.append(i.string)
    print(i.string)

nn163_cloud_url2 = 'http://music.163.com/playlist?id=321201766'
bs2 = BeautifulSoup(s.get(nn163_cloud_url2, headers=headers).content, "lxml")

songB = []
for i in bs2.ul.children:
    songB.append(i.string)
    print(i.string)

print("----------------分割线----------------------")
setA = set(songA)
setB = set(songB)
# 取交集
simi = setA.intersection(setB)
# 取并集
all = setA.symmetric_difference(setB)
foo = open("similar.txt", "w")
for song in simi:
    print(song)
    foo.write(song+"\n")
x = len(simi) / len(all)
print("总歌曲", len(all))
print("相同歌曲", len(simi))
print("歌单相似度:", x)
foo.write(str(x))
foo.close()



