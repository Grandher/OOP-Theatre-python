from general_list import generalList
from spectacle import Spectacle

class Spectacle_list(generalList, Spectacle):
	def create_item(self, code=0, title='', year=0, budget=0):
		if code in self.get_codes():
			print(f'Спектакль с кодом {code} уже существует')

		else:
			generalList.append_list(self, Spectacle(code, title, year, budget))