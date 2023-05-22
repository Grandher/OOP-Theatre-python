from general_list import generalList
from actors import Actors

class Actors_list(generalList, Actors):
	def create_item(self, code=0, surname='', name='', secname='', rank='', experience=0):
		if code in self.get_codes():
			print(f'Актёр с кодом {code} уже существует')

		else:
			generalList.append_list(self, Actors(code, surname, name, secname, rank, experience))
