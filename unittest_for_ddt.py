import unittest
from ddt import ddt,data,unpack,file_data
from selenium import webdriver
@ddt
class Demo_ddt(unittest.TestCase):
    # @data(*[[1,2,3],4,5,6])
   # @data((1,2,3),(1,0,1),(0,0,0),(1,1,3))
    # @data((1,2,3))
    # @data([1,2,3,4,5])
    #@unpack
    #@data({"a":"1","b":2},{"a":"1","b":2})
    @file_data('../data/data.yaml')
    def test(self,**data):
        #print('a')
        #print(data["a"])
        # print(a,b,c)
        # print(type(a))
        #print(type(a))
        #print(data['data'])
        print(data)
        # print('b=',b)
        # # print(data[1])
        # print("c=",c)
        # print(d)
        #Zwebdriver.Chrome()








if __name__ == '__main__':
    unittest.main()