#-*- coding:utf-8 -*-
class General:
    def __init__(self,code=0):
        self.set_code(code)
    def set_code(self,value):self.__code=value
    def get_code(self):return self.__code

