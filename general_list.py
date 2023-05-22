#-*- coding:utf-8 -*-
class generalList:
    def __init__(self):self.__list=[]
    def clear(self):self.__list=[]
    def find_by_code(self,code):
        for l in self.__list:
            if l.get_code()==code:return l
    def get_codes(self):return [s.get_code() for s in self.__list]
    def append_list(self,value):self.__list.append(value)
    def remove_list(self,code):
       for s in self.__list:
           if s.get_code()==code:self.__list.remove(s)

    def get_items(self):
        return [s for s in self.__list]

    def remove_item(self, value):
        self.__list.remove(self.find_by_code(value))

