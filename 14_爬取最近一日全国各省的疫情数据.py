import requests
from bs4 import BeautifulSoup
import re
import json
from tqdm import tqdm


class CoronaVirusSpider():

    def __init__(self):
        self.url = 'https://ncov.dxy.cn/ncovh5/view/pneumonia'

    def send_request(self, url):
        """
        发送请求，获取响应
        :param url: 请求的url
        :return: 响应内容
        """
        response = requests.get(url)
        content = response.content.decode()
        return content

    def parse_data(self, content, tag_id):
        """
        提取关键信息，并解析成Python数据
        :param content: 响应内容数据
        :return: 返回解析后的数据
        """
        soup = BeautifulSoup(content, 'lxml')
        script = soup.find(attrs={'id': tag_id})
        text = script.get_text
        # 从数据中获取json字符串
        json_str = re.findall(r'\[.*\]', str(text))[0]
        # 将json字符串转为Python数据
        data = json.loads(json_str)
        return data

    def save_file(self, data, path):
        """
        将数据存入文件
        :param data: 待保存的数据
        :param path: 保存路径
        :return:
        """
        # 将数据以json格式存入文件
        with open(path, 'w', encoding='utf8') as f:
            json.dump(data, f, ensure_ascii=False)

    def coll_last_day_corona_virus_data(self):
        """
        采集最近一日世界各国的疫情数据
        :return:
        """
        content = self.send_request(self.url)
        data = self.parse_data(content, tag_id='getListByCountryTypeService2true')
        self.save_file(data, 'data/corona_virus_country_data.json')

    def coll_statistics_corona_virus_data(self):
        """
        爬取1月23日以来世界各国的疫情数据
        :return:
        """
        # 加载各国的疫情数据
        with open('data/corona_virus_country_data.json', encoding='utf8') as f:
            last_day_corona_virus_data = json.load(f)
        # 定义列表，用于存储世界各国的统计数据
        corona_virus_list = []
        # 遍历各国的疫情数据，获取统计数据的url
        for country in tqdm(last_day_corona_virus_data, '爬取1月23日以来世界各国的疫情信息'):
            # 发送请求，获取统计数据
            statistics_data_url = country['statisticsData']
            statistics_data_json_str = self.send_request(statistics_data_url)
            # 将json字符串转为Python数据
            statistics_data = json.loads(statistics_data_json_str)['data']
            for data in statistics_data:
                data['provinceName'] = country['provinceName']
            corona_virus_list.extend(statistics_data)
            # 保存数据
            self.save_file(corona_virus_list, 'data/corona_virus_list.json')

    def coll_last_day_corona_virus_data_of_province(self):
        """
        爬取最近一日全国各省的疫情数据
        :return:
        """
        # 发送请求，获取响应内容
        content = self.send_request(self.url)
        # 解析数据
        data = self.parse_data(content, tag_id='getAreaStat')
        # 保存数据
        self.save_file(data, 'data/coll_last_day_corona_virus_data_of_province.json')

    def run(self):
        # self.coll_last_day_corona_virus_data()
        # self.coll_statistics_corona_virus_data()
        self.coll_last_day_corona_virus_data_of_province()


if __name__ == '__main__':
    spider = CoronaVirusSpider()
    spider.run()
