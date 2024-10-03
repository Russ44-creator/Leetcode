'''
第四轮 integration。一共3问。 第一问是给一个json file, 
转化成object, 取object里面前十个坐标;
第二问是发一个http post request,
去download一个PNG文件并保存到本地, 打开文件可以看到一个地图截图;
第三问是把第二问中的request里的坐标换成第一问的坐标, 然后make http request. 
提前掌握一下Jackson 和 OKHTTP的library就行.
'''
import json

def parse_json():
    json_data = '{"name": "Lingfeng", "age": 25, "city": "Providence"}'

    # 使用 json.loads() 将 JSON 字符串转换为字典
    dictionary = json.loads(json_data)

    # 输出字典
    print(dictionary)