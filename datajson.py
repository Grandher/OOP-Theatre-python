from data import data
import json

class datajson(data):
	def read(self):
		with open(self.get_infile(), "r", encoding="utf-8") as read_file:
			data = json.load(read_file)

		for k in data["actor"]:
			code = k["code"]
			surname = k["surname"]
			name = k["name"]
			secname = k["secname"]
			rank = k["rank"]
			experience = k["experience"]
			self.get_theat().create_actor(code, surname, name, secname, rank, experience)

		for k in data["spectacle"]:
			code = k["code"]
			title = k["title"]
			year = k["year"]
			budget = k["budget"]
			self.get_theat().create_spectacle(code, title, year, budget)

		for k in data["occupation"]:
			code = k["code"]
			role = k["role"]
			contract_cost = k["contract_cost"]
			actor = self.get_theat().get_actor(int(k["actor"]))
			spectacle = self.get_theat().get_spectacle(int(k["spectacle"]))
			self.get_theat().create_occupation(code, role, contract_cost, actor, spectacle)

	def write(self):
		data = {"actor": [], "spectacle": [], "occupation": []}
		for k in self.get_theat().get_actors_list():
			aact = {}
			aact["code"] = k.get_code()
			aact["surname"] = k.get_surname()
			aact["name"] = k.get_name()
			aact["secname"] = k.get_secname()
			aact["rank"] = k.get_rank()
			aact["experience"] = k.get_experience()#.split()[0]
			data["actor"].append(aact)

		for k in self.get_theat().get_spectacles_list():
			aspec = {}
			aspec["code"] = k.get_code()
			aspec["title"] = k.get_title()
			aspec["year"] = k.get_year()
			aspec["budget"] = k.get_budget()#.split()[0]
			data["spectacle"].append(aspec)

		for k in self.get_theat().get_occupations_list():
			aocc = {}
			aocc["code"] = k.get_code()
			aocc["actor"] = k.get_actor_code()#.get_code()
			aocc["spectacle"] = k.get_spectacle_code()#.get_code()
			aocc["role"] = k.get_role()
			aocc["contract_cost"] = k.get_contract_cost()#.split()[0]
			data["occupation"].append(aocc)

		with open(self.get_outfile(), "w", encoding="utf-8") as write_file:
			json.dump(data, write_file, indent=1, ensure_ascii=False)

