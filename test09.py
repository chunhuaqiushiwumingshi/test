# import json
# import re
# import time
# from easy_excel_util import Builder, ExportField
# import requests


# # url = 'http://data.weatherat.com/meizu/weather/6GRbp9J9Ttt4gdvATZizKDPV3CLmeIzU/2' 
# #     response = requests.request('GET', url)
# #     data = response.text
# #     data_json = json.loads(data)
# #     weather = data_json.get('data').get('condition').get('condition')
# #     temperature = data_json.get('data').get('condition').get('temp')
# #     mz_weather_dict = {}
# #     mz_weather_dict['weather'] = weather
# #     mz_weather_dict['temperature'] = int(temperature)
# msg = [{'city': 'str(city_name)', 'meizu': 'str(mz_temperature)', 'xiaomi': 'str(xm_temperature)','hefeng':'str(hef_temperature)'}]
# print(msg,type(msg))


class BaBa1():
    name = "马斯克"
    money = "6000个小目标"
    __age = 18          # __开头变量被称为私有变量，name它是不能够被继承的

    def make_monkey(self):
        print("1")
        
    def __get_age(self):  # __开头的方法被称为私有方法，不希望外部的类来引用，只能在本类中使用
        return self.__age
    
class BaBa2():
    name = "码云"
    money = "1000个小目标"
    
    def make_monkey1(self):
        print("2")


class SuperSon(BaBa1, BaBa2):
    name = "super ma"
    
    def test(self):
        super().make_monkey()       # 多继承能使用super默认就是它

# python3： 优先找自己的，使用广度优先查找算法
ss = SuperSon()
ss.make_monkey()
ss.test()

print(ss.money)
ss.make_monkey1()