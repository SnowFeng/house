# house
爬取链家（安居客，58同城，赶集后续更新）的房源信息，便于广大未买房子的朋友们尽快成为房奴！！！Crawl the house informations of lianjia.com (anjvke.com, 58.com, ganji.com after the update), convenient for the majority of friends who did not buy the house as soon as to become the mortgage slave!!!

## 直接运行
在 https://leancloud.cn/ 内建立账号
修改house.py为自己的App ID App KEY

python house.py

## 个性化运行
此程序是把leancloud作为云数据库使用，可以根据自己需求修改save()，爱保存哪保存哪。

修改链家的网址，查询的限定条件需要能够保存在URL内，例如链家的排序也是可以保存在URL内的，一看例子你也应该就懂了，不懂的话就再看一遍。