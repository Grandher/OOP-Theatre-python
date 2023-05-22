from general_list import generalList
from occupation import Occupation

class Occupation_list(generalList, Occupation):
	def create_item(self, code=0, role='', contract_cost=0, actor=None, spectacle=None):
		if code in self.get_codes():
			print(f'Запись с кодом {code} уже существует')

		else:
			generalList.append_list(self, Occupation(code, role, contract_cost, actor, spectacle))