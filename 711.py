# coding=utf-8
import requests
import pandas as pd
from DbDataset import DbDataset
# 建立一個縣市的list

cityc = [
    '基隆市'

]

city = [
    u'基隆市',
    u'台北市',
    u'新北市',
    u'桃園市',
    u'新竹市',
    u'新竹縣',
    u'苗栗縣',
    u'台中市',
    u'彰化縣',
    u'雲林縣',
    u'南投縣',
    u'嘉義縣',
    u'嘉義市',
    u'台南市',
    u'高雄市',
    u'屏東縣',
    u'台東縣',
    u'花蓮縣',
    u'宜蘭縣',
    u'連江縣',
    u'金門縣',
    u'澎湖縣'
]
# 使用迴圈來依序取得每一個城市的門市資訊

for index, city in enumerate(city):

   
    # 剛剛在開發者模式觀察到的Post發出的資訊是那些

    data = {
        'strTargetField': 'COUNTY',
        'strKeyWords': '%s' % city
    }

    res = requests.post(
        'http://www.ibon.com.tw/retail_inquiry_ajax.aspx', data=data)

    # with open('log.txt', 'w+') as logfile:
    #     logfile.write(res.text.encode('utf8'))
    #     logfile.close()
    # 第一次迴圈建立dataframe，並將城市填入。資料的形式是table，所以直接使用read_html快速拿下!

    if index == 0:
        items = {}
        df_711_store = pd.read_html(res.text, header=0)[0]
        df_711_store[u'縣市'] = city
        items['marketid']=df_711_store[u'店號']
        items['nickname']=df_711_store[u'店名']
        items['addr']=df_711_store[u'地址']
        items['city']=df_711_store[u'縣市']
        DbDataset.datasetInsertShop(items)

    # 第二次迴圈以上就將資訊直接append到dataframe裡

    if index > 0:
        items = {}
        df_711_store_ = pd.read_html(res.text, header=0)[0]
        df_711_store_[u'縣市'] = city
        items['marketid']=df_711_store_[u'店號']
        items['nickname']=df_711_store_[u'店名']
        items['addr']=df_711_store_[u'地址']
        items['city']=df_711_store_[u'縣市']
        DbDataset.datasetInsertShop(items)
        # print(df_711_store_['縣市'])
        # print(df_711_store_['店名'])
        # print(df_711_store_['店號'])
        # print(df_711_store_['地址'])
         
        df_711_store = df_711_store.append(df_711_store_)

    # 打印出進度
    #loc = pd.read_html(res.text, header=0)[0].shape[0]
    # print(loc)
    # with open('locat.txt', 'w+') as logfile:
    #    logfile.write(loc.encode('utf8'))
    #    logfile.close()

    # print('%2d) %-*s %4d' %
    # (index, 5, city, pd.read_html(res.text, header=0)[0].shape[0]))

# 將資料輸出成Excel

df_711_store.to_excel(r'711.xlsx', encoding="UTF-8", index=False)
