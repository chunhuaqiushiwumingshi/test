import json
import re
import time
from easy_excel_util import Builder, ExportField
import requests

weather_dict = {}
weather_data = []

def get_hf_weather(city_id):
    url = 'http://data.weatherat.com/meizu/weather/6GRbp9J9Ttt4gdvATZizKDPV3CLmeIzU/' + city_id
    response = requests.request('GET', url)
    data = response.text
    data_json = json.loads(data)
    weather = data_json.get('data').get('condition').get('condition')
    temperature = data_json.get('data').get('condition').get('temp')
    mz_weather_dict = {}
    mz_weather_dict['weather'] = weather
    mz_weather_dict['temperature'] = int(temperature)
    return mz_weather_dict


def get_xm_weather(gov_city_id):
    global weather_dict
    url = 'http://weatherapi.market.xiaomi.com/wtr-v3/weather/all?latitude=101&longitude=102&locationKey=weathercn%3A' + gov_city_id + '&days=15&appKey=weather20151024&sign=zUFJoAR2ZVrDy1vF3D07&isGlobal=false&locale=zh_cn';
    response = requests.request("GET", url)
    response.encoding = response.apparent_encoding
    data = response.text
    data_json = json.loads(data)
    current_weather = data_json.get('current')
    weather = current_weather.get('weather')
    temperature = current_weather.get('temperature').get('value')
    xm_weather_dict = {}
    xm_weather_dict['weather'] = weather_dict[weather]
    xm_weather_dict['temperature'] = int(temperature)
    return xm_weather_dict


def get_hefeng_weather(gov_city_id):
    url = 'https://devapi.qweather.com/v7/weather/now?key=a9d683271a8241daaf6433d3e965d7bb&location=' + gov_city_id
    response = requests.request("GET", url)
    print(response)
    data = response.text
    data_json = json.loads(data)
    current_weather = data_json.get('now')
    weather = current_weather.get('text')
    temperature = current_weather.get('temp')
    hef_weather_dict = {}
    hef_weather_dict['weather'] = weather
    hef_weather_dict['temperature'] = int(temperature)
    return hef_weather_dict


def send_msg(msg):
    global weather_data
    weather_data = weather_data + msg
    return weather_data


def str_middle(buff, w1, w2):
    try:
        buff = buff.replace('\n', '')
        buff = buff.replace('\r', '')
        pat = re.compile(w1 + '(.*?)' + w2, re.S)
        result = pat.findall(buff)
        if len(result) > 0:
            return result[0]
        else:
            return ''
    except:
        return ""


def read_file():
    with open('city_info_new.txt', 'r', encoding='utf-8') as city_file:
        city_list = city_file.readlines()
    for i in range(0, len(city_list)):
        city_list[i] = city_list[i].rstrip('\n')
    return city_list


def check_data():
    city_list = read_file()
    print('>>>>>>开始比较天气')
    print('区域名称 -> 魅族 -> 小米 -> 和风')
    for i in range(0, len(city_list)):
        try:
            city_info = city_list[i]
            city_info_list = city_info.split(':')
            mz_city_id = city_info_list[0]
            city_name = city_info_list[1]
            gov_city_id = city_info_list[2]
            # print(city_name + ' -> ' + getGovWeather(gov_city_id))
            mz_weather_dict = get_hf_weather(mz_city_id)
            xm_weather_dict = get_xm_weather(gov_city_id)
            # mz_weather = mz_weather_dict['weather']
            mz_temperature = mz_weather_dict['temperature']
            print(mz_temperature)
            # xm_weather = xm_weather_dict['weather']
            xm_temperature = xm_weather_dict['temperature']
            print(xm_temperature)
            hef_weather_dict = get_hefeng_weather(gov_city_id)
            # hef_weather = hef_weather_dict['weather']
            hef_temperature = hef_weather_dict['temperature']
            print(hef_temperature)
            if 1>0:
                msg = [{'city': str(city_name), 'meizu': str(mz_temperature), 'xiaomi': str(xm_temperature),'hefeng':str(hef_temperature)}]
                send_msg(msg)
                print(msg)
                # 记得停一小段时间，不然容易出错
                time.sleep(0.05)
                print("导出"+str(city_name)+"成功")
        except Exception as e:
            print('>>>>>>>>>' + str(city_list[i]) + '天气获取异常>>>>>>>')
            print(e)
            time.sleep(10)
    print('>>>>>>天气比较结束，一共2082个区域的天气')


def init_weather_info():
    global weather_dict
    with open('weather_info.json', 'r', encoding='utf-8') as weather_info_file:
        weather_info = weather_info_file.readlines()
        weather_info_json = json.loads(weather_info[0])
        for key in range(len(weather_info_json)):
            weather_dict[str(weather_info_json[key].get('code'))] = weather_info_json[key].get('wea')


def xlsx():
    global weather_data
    Builder.build_export(xlsx=True).sheet(
        index=0, data=weather_data, parse_map=dict(
        city=ExportField(index=0, col_name='城市', width=15), 
        meizu=ExportField(index=1, col_name='魅族', width=10), 
        xiaomi=ExportField(index=2, col_name='小米', width=10),
        hefeng=ExportField(index=2, col_name='和风', width=10)
        )
        ).do_export('/PYTHON/0915.xlsx')


if __name__ == '__main__':
    init_weather_info()
    check_data()
    xlsx()
    print("导出成功")

    
