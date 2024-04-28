# encoding:utf-8
# python3.0

from source.save import saveData
from source.common import getHtml,getRenderHtml
from source.report import reportData
import configparser
import webbrowser
import os


# ------主函数------
# delete()
if __name__ == '__main__':
    # 获取参数
    config = configparser.ConfigParser()
    config.read("config.ini")

    # 清除数据
    save = saveData(config)
    save.deleteOldData()

    # 贝壳找房 （例：北京、通州 251-499万 80-100平） 根据自己需求添加链接
    beike1 = getHtml('''https://cq.ke.com/ershoufang/bishan/co32dp1sf1de1a5a6l3l4l5p1p2/''')
    beike2 = getHtml('''https://cq.ke.com/ershoufang/bishan/pg2co32dp1sf1de1a5a6l3l4l5p1p2/''')
    beike3 = getHtml('''https://cq.ke.com/ershoufang/bishan/pg3co32dp1sf1de1a5a6l3l4l5p1p2/''')
    beike4 = getHtml('''https://cq.ke.com/ershoufang/bishan/pg4co32dp1sf1de1a5a6l3l4l5p1p2/''')
    beike5 = getHtml('''https://cq.ke.com/ershoufang/bishan/pg5co32dp1sf1de1a5a6l3l4l5p1p2/''')
    beike_htmls = [beike1, beike2, beike3,beike4,beike5]
    for beike_html in beike_htmls:
        save.beike_save(beike_html)

    # 链家 （例：北京 0-600万 60-100平） 根据自己需求添加链接
    lianjia1 = getHtml('''https://cq.lianjia.com/ershoufang/bishan/co32de1dp1sf1l3l4l5a5a6p1p2/''')
    lianjia2 = getHtml('''https://cq.lianjia.com/ershoufang/bishan/pg2co32de1dp1sf1l3l4l5a5a6p1p2/''')
    lianjia3 = getHtml('''https://cq.lianjia.com/ershoufang/bishan/pg3co32de1dp1sf1l3l4l5a5a6p1p2/''')
    lianjia4 = getHtml('''https://cq.lianjia.com/ershoufang/bishan/pg4co32de1dp1sf1l3l4l5a5a6p1p2/''')
    lianjia5 = getHtml('''https://cq.lianjia.com/ershoufang/bishan/pg5co32de1dp1sf1l3l4l5a5a6p1p2/''')
    lianjia_htmls = [lianjia1, lianjia2, lianjia3,lianjia4,lianjia5]
    for lianjia_html in lianjia_htmls:
        save.lianjia_save(lianjia_html)

    # 58同城 高新园区 80-120W 3室 精装修(58加了验证，不爬了)
    # tongcheng1 = getHtml('''https://cq.58.com/bishanlaochengqu/ershoufang/e115j4z1/?PGTID=0d30000c-0230-0142-6daa-bc02a15548f8&ClickID=1&prices=30_60&areas=100_140''')
    # tongcheng2 = getHtml('''https://cq.58.com/bishanlaochengqu/ershoufang/e116j4z1/?PGTID=0d30000c-0230-0142-6daa-bc02a15548f8&ClickID=1&prices=30_60&areas=100_140''')
    # # print(str(tongcheng1.encode('GB18030')))
    # tongcheng_htmls = [tongcheng1, tongcheng2]
    # for tongcheng_html in tongcheng_htmls:
    #     save.tongcheng_save(tongcheng_html)

    # 安居客 （例：北京 200-600万 60-100平 按最新排序） 根据自己需求添加链接
    anjuke1 = getRenderHtml('''https://chongqing.anjuke.com/sale/bishanqu-q-bishanlaochengqu/d47-z1/?prices=30_60&areas=100_140''')
    anjuke2 = getRenderHtml('''https://chongqing.anjuke.com/sale/bishanqu-q-bishanlaochengqu/d47-p2-z1/?prices=30_60&areas=100_140''')
    anjuke3 = getRenderHtml('''https://chongqing.anjuke.com/sale/bishanqu-q-bishanlaochengqu/d47-p3-z1/?prices=30_60&areas=100_140''')
    anjuke_htmls = [anjuke1,anjuke2,anjuke3]
    for anjuke_html in anjuke_htmls:
        save.anjuke_save(anjuke_html)

    # # 房天下
    # fangtianxia1 = getHtml('''https://cq.esf.fang.com/house-a011840-b030161/c240,0-d260,40-g25,4,3-j2100-k2140-t23-i31-l3010/''')
    # fangtianxia2 = getHtml('''https://cq.esf.fang.com/house-a011840-b030161/c240,0-d260,40-g25,4,3-j2100-k2140-t23-i32-l3010/''')
    # fangtianxia3 = getHtml('''https://cq.esf.fang.com/house-a011840-b030161/c240,0-d260,40-g25,4,3-j2100-k2140-t23-i33-l3010/''')
    # fangtianxia4 = getHtml('''https://cq.esf.fang.com/house-a011840-b030161/c240,0-d260,40-g25,4,3-j2100-k2140-t23-i34-l3010/''')
    # fangtianxia5 = getHtml('''https://cq.esf.fang.com/house-a011840-b030161/c240,0-d260,40-g25,4,3-j2100-k2140-t23-i35-l3010/''')
    # fangtianxia6 = getHtml('''https://cq.esf.fang.com/house-a011840-b030161/c240,0-d260,40-g25,4,3-j2100-k2140-t23-i36-l3010/''')
    # fangtianxia_htmls = [fangtianxia1, fangtianxia2,fangtianxia3,fangtianxia4,fangtianxia5,fangtianxia6]
    # for fangtianxia_html in fangtianxia_htmls:
    #     save.fangtianxia_save(fangtianxia_html)

    # # 赶集 高新园区 80-120W 3室 精装修
    # ganji1 = getHtml('''http://dl.ganji.com/fang5/gaoxinyuanqu/b80e120h3q2/''')
    # ganji2 = getHtml('''http://dl.ganji.com/fang5/gaoxinyuanqu/b80e120h3o2q2/''')
    # ganji3 = getHtml('''http://dl.ganji.com/fang5/gaoxinyuanqu/b80e120h3o3q2/''')
    # ganji_htmls = [ganji1, ganji2, ganji3]
    # for ganji_html in ganji_htmls:
    #     ganji_save(ganji_html)

    print("生成报告中...")
    rep = reportData()
    reportFileName = rep.get_report()
    webbrowser.open('''file:///''' + os.path.dirname(__file__) + '''/reports/''' + reportFileName)

    print("OVER!!!")
