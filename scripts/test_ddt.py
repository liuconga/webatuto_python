"""测试unittest的数据驱动ddt"""

"""引入：unittest框架的本身不带数据驱动功能，所以需要引入三方框架
    方式1.ddt
    方式2.parameterized 参数化
    
  ddt优势：可以直接读取json和yaml文件：如果不是以.yml或yaml结尾的文件，
  默认都当成json文件进行读取
    """

"""
   ddt使用步骤：
   1.导包 import ddt
   2.用@ddt.ddt标记类
   3.用@ddt.data()标记方法进行参数化
      3.1 ddt读取普通数据
      @ddt.data(1, 2, 3)
      def test_ddt(self, value):
          print('我打印了+', value)
          打印结果：我打印了+ 1
                  我打印了+ 2
                  我打印了+ 3 
  
      3.2 ddt读取多个列表
      @ddt.data(['18301225040', '123456', '8888'], ['17301225040', '654321', '6666'])
      @ddt.unpack
     
      3.3 ddt跟读取xml文件结合进行数据驱动
      @ddt.data(*ReadData.read_xml('data.xml'))
      @ddt.unpack
  
      3.4 ddt跟读取Excel文件结合进行数据驱动
      @ddt.data(*ReadData.read_excel('data.xlsx'))
      @ddt.unpack
  
      3.5 ddt读取json文件：必须是数组嵌套对象的格式
      @ddt.file_data('../data/data_ddt.json')
      @ddt.unpack
      
         json文件格式：
          [
              {
              "username":"1830999822",
              "password":"654321",
              "yzm":"6666"
               },
              {
              "username":"17301397788",
              "password":"123456",
              "yzm":"6666"
              }
          ]
"""

import ddt
import unittest
from tool.read_data import ReadData


@ddt.ddt
class TestDDt(unittest.TestCase):
    """ddt数据驱动测试类"""

    # 1.ddt读取普通数据
    # @ddt.data(1, 2, 3)
    # def test_ddt(self, value):
    #     print('我打印了+', value)
    #     """打印结果：我打印了+ 1
    #                我打印了+ 2
    #                我打印了+ 3 """

    # 2.ddt读取多个列表
    # @ddt.data(['18301225040', '123456', '8888'], ['17301225040', '654321', '6666'])

    # 3.ddt跟读取xml文件结合进行数据驱动
    # @ddt.data(*ReadData.read_xml('data.xml'))

    # 4.ddt跟读取Excel文件结合进行数据驱动
    # @ddt.data(*ReadData.read_excel('data.xlsx'))

    # 5.ddt读取json文件：必须是数组嵌套对象的格式
    @ddt.file_data('../data/data_ddt.json')
    @ddt.unpack
    def test_ddt_f(self, username, password, yzm):
        print("username:", username, "passwrod:", password, "yzm:", yzm)


if __name__ == '__main__':
    unittest.main()
