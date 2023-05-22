from actors_list import Actors_list
from spectacle_list import Spectacle_list
from occupation_list import Occupation_list

class Theatre:
    def __init__(self):
        self.__actors = Actors_list()
        self.__spectacles = Spectacle_list()
        self.__occupations = Occupation_list()

    def create_actor(self, code=0, surname='', name='', secname='', rank='', experience=0):
        self.__actors.create_item(code, surname, name, secname, rank, experience)

    def create_spectacle(self, code=0, title='', year=0, budget=0):
        self.__spectacles.create_item(code, title, year, budget)

    def create_occupation(self, code=0, role='', contract_cost=0, actor=None, spectacle=None):
        self.__occupations.create_item(code, role, contract_cost, actor, spectacle)

    def get_actors_list(self):
        return self.__actors.get_items()
    def get_spectacles_list(self):
        return self.__spectacles.get_items()
    def get_occupations_list(self):
        return self.__occupations.get_items()

    def get_actor(self, code):
        return self.__actors.find_by_code(code)

    def get_spectacle(self, code):
        return self.__spectacles.find_by_code(code)

    def get_occupation(self, code):
        return self.__occupations.find_by_code(code)

    def get_actor_new_code(self):
        if self.__actors.get_codes():
            return max(self.__actors.get_codes())+1
        else: return 1
    def get_spectacle_new_code(self):
        if self.__spectacles.get_codes():
            return max(self.__spectacles.get_codes())+1
        else: return 1
    def get_occupation_new_code(self):
        if self.__occupations.get_codes():
            return max(self.__occupations.get_codes())+1
        else: return 1

    def rewrite_codes(self, array):
        i = 1
        for j in array:
            j.set_code(i)
            i += 1

    def remove_actor(self, code):
        if self.__occupations.get_items() != []:
            for b in self.__occupations.get_items():
                if b.get_actor().get_code() == code:
                    return False;
        self.__actors.remove_item(code)
        self.rewrite_codes(self.get_actors_list())
        return True

    def remove_spectacle(self, code):
        if self.__occupations.get_items() != []:
            for b in self.__occupations.get_items():
                if b.get_spectacle().get_code() == code:
                    return False;
        self.__spectacles.remove_item(code)
        self.rewrite_codes(self.get_spectacles_list())
        return True

    def remove_occupation(self, code):
        self.__occupations.remove_item(code)
        self.rewrite_codes(self.get_occupations_list())
