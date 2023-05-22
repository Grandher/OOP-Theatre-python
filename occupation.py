#-*- coding:utf-8 -*-
from general import General
from spectacle import Spectacle
from actors import Actors
class Occupation(General):
    #(Actor, Spectacle, Role, Contract_Cost)
    #(Актёр, Спектакль, Роль, Стоимость контракта)
    def __init__(self, code=0, role='', contract_cost=0, actor=None, spectacle=None):
        General.__init__(self,code)
        self.set_role(role)
        self.set_contract_cost(contract_cost)
        #__actor = Actors()
        #__spectacle = Spectacle()
        self.set_actor(actor)
        self.set_spectacle(spectacle)

    def set_role(self, role):
        self.__role = role
    def set_contract_cost(self, contract_cost):
        self.__contract_cost = contract_cost
        #self.__contract_cost = str(contract_cost) + ' тыс. рублей'
    def get_role(self):
        return self.__role
    def get_contract_cost(self):
        return self.__contract_cost

    def set_actor(self, actor):
        self.__actor = actor
    def get_actor(self):
        return self.__actor
    def get_actor_code(self):
        return self.__actor.get_code()
    def clr_actor(self):
        self.__actor = None

    def get_actor_surname(self):
        return self.__actor.get_surname()
    def get_actor_name(self):
        return self.__actor.get_name()
    def get_actor_secname(self):
        return self.__actor.get_secname()
    def get_actor_fio(self):
        return self.__actor.get_fio()
    def get_actor_rank(self):
        return self.__actor.get_rank()
    def get_actor_experience(self):
        return self.__actor.get_experience()



    def set_spectacle(self, spectacle):
        self.__spectacle = spectacle
    def get_spectacle(self):
        return self.__spectacle
    def get_spectacle_code(self):
        return self.__spectacle.get_code()
    def clr_spectacle(self):
        self.__spectacle = None

    def get_spectacle_title(self):
        return self.__spectacle.get_title()
    def get_spectacle_year(self):
        return self.__spectacle.get_year()
    def get_spectacle_budget(self):
        return self.__spectacle.get_budget()


    def export_occupation(self):
        if self.__actor != None:
            act = 'Актёр: ' + self.get_actor_fio() + ', ' + self.get_actor_rank() + ', ' + str(self.get_actor_experience())
        else:
            act = 'Нет актёра'
        if self.__spectacle != None:
            spec = 'Спектакль: ' + self.get_spectacle_title() + ', ' + str(self.get_spectacle_year()) + ', ' + str(self.get_spectacle_budget())
        else:
            spec = 'Нет спектакля'
        rez = act + '\n' + spec + '\nРоль: ' + self.get_role() + '\nСтоимость контракта: ' + str(self.get_contract_cost())
        return rez