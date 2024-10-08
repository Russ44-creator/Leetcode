'''
第四轮 integration。一共3问。 第一问是给一个json file, 
转化成object, 取object里面前十个坐标;
第二问是发一个http post request,
去download一个PNG文件并保存到本地, 打开文件可以看到一个地图截图;
第三问是把第二问中的request里的坐标换成第一问的坐标, 然后make http request. 
提前掌握一下Jackson 和 OKHTTP的library就行.
'''
import json
import requests

def parse_json():
    # Path to the JSON file
    file_path = 'ride_simple.json'

    # Open the file and parse the JSON content
    with open(file_path, 'r') as file:
        data = json.load(file)

    coordinates = data['features'][0]['geometry']['coordinates']
    first_ten_coordinates = coordinates[:10]

    # Output the first 10 coordinates
    print(first_ten_coordinates)

def send_post_request(url, json_path, output_path):
    # 读取JSON文件
    with open(json_path, 'r') as file:
        json_data = file.read()

    # 发送POST请求
    response = requests.post(url, data=json_data, headers={'Content-Type': 'application/json'})

    # 检查请求是否成功
    if response.status_code == 200:
        # 将返回的图片内容写入文件
        with open(output_path, 'wb') as f:
            f.write(response.content)
        print("File saved successfully.")
    else:
        print("Failed to retrieve data:", response.status_code)

parse_json()