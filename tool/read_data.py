import json
import xml
from xml.dom.minidom import Document

import xlrd
import yaml
from xlrd import Book
from xlrd.sheet import Sheet


class ReadData(object):
    path = './data/'

    @classmethod
    def read_json(cls, file_name: str):
        """读取json的工具类"""
        with open(cls.path + file_name) as f:
            data = json.load(f)
            data_list = list()
            i: dict
            for i in data:
                for v in list(i.values()):
                    data_list.append(tuple(v.values()))
            return data_list

    @classmethod
    def read_txt(cls, file_name: str):
        """读取txt的工具类"""
        data: list = []
        with open(cls.path + file_name) as f:
            # 通过readlines()读取所有行
            for i in f.readlines():
                data.append(tuple(i.strip().split(',')))
        return data[1:]

    @classmethod
    def read_yaml(cls, file_name: str):
        """读取yaml文件的工具类"""
        data_list = list()
        with open(cls.path + file_name) as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            for i in data:
                for v in i.values():
                    data_list.append(tuple(v.values()))
        return data_list

    @classmethod
    def read_excel(cls, file_name: str):
        """读取excel文件的工具类"""
        # 0.导包import xlrd
        # from xlrd import Book
        # from xlrd.sheet import Sheet
        data_list = []
        # 1.通过xlrd包的open_workbook获取excel的文件对象为Book类型
        book: Book = xlrd.open_workbook(cls.path + file_name)
        # 2.通过book对象找到所需sheet表
        sheet: Sheet = book.sheet_by_name("login")
        # 3.sheet.nrows获取sheet表的总行数，sheet.nclos获取表的总列数
        for i in range(sheet.nrows):
            data_raw = []
            for k in range(sheet.ncols):
                # 4.sheet.cell_value(i,k) 获取i行k列单元格的值
                if isinstance(sheet.cell_value(i, k), str):
                    data_raw.append(sheet.cell_value(i, k))
                elif isinstance(sheet.cell_value(i, k), float):
                    data_raw.append(int(sheet.cell_value(i, k)))

            data_list.append(data_raw)

        return data_list[1:]

    @classmethod
    def read_xml(cls, file_name: str):
        """读取xml中数据【使用DOM解析】"""
        data_list = []
        # 0.导包：import xml.dom.minidom
        # 1.获取dom对象
        dom = xml.dom.minidom.parse(cls.path + file_name)
        # 2.通过dom对象获取元素
        # 2.1获取标签为user的总的元素个数
        data_user = dom.getElementsByTagName('user')
        # 2.2获取标签为username的总的元素个数
        data_username = dom.getElementsByTagName('username')
        # 2.3获取标签为password的总的元素个数
        data_pwd = dom.getElementsByTagName('password')
        # 2.4获取标签为yzm的总的元素个数
        data_yzm = dom.getElementsByTagName('yzm')
        for i in range(len(data_user)):
            # 定义列表中列表(包括：username ,password,yzm)
            data = []
            data.append(data_username[i].childNodes[0].data)
            data.append(data_pwd[i].childNodes[0].data)
            data.append(data_yzm[i].childNodes[0].data)
            # 添加data到总列表
            data_list.append(data)

        return data_list


if __name__ == '__main__':
    # print(ReadData.read_json('data.json'))
    # print(ReadData.read_txt('data.txt'))
    # print(ReadData.read_yaml('data.yaml'))
    # print(ReadData.read_excel('data.xlsx'))
    ReadData.read_xml('data.xml')
