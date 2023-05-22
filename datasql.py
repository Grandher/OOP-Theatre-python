import os
import sqlite3 as db
from data import data


emptydb = """
PRAGMA foreign_keys = ON;

create table actor
(code integer primary key,
surname text,
name text,
secname text,
rank text,
experience integer);

create table spectacle
(code integer primary key,
title text,
year integer,
budget real);

create table occupation
(code integer primary key,
role text,
contract_cost text,
actor integer references actor(code) on update cascade on delete set null,
spectacle integer references spectacle(code) on update cascade on delete set null);
"""


class datasql(data):
	def read(self):
		conn = db.connect(self.get_infile())
		curs = conn.cursor()
		curs.execute('select code, surname, name, secname, rank, experience from actor')
		data = curs.fetchall()
		for r in data:
			self.get_theat().create_actor(r[0], r[1], r[2], r[3], r[4], r[5])
		curs.execute('select code, title, year, budget from spectacle')
		data = curs.fetchall()
		for r in data:
			self.get_theat().create_spectacle(r[0], r[1], r[2], r[3])
		curs.execute('select code, role, contract_cost, actor, spectacle from occupation')
		data = curs.fetchall()
		for r in data:
			if r[3]:
				ac = int(r[3])
			else:
				ac = r[3]
			if r[4]:
				sp = int(r[4])
			else:
				sp = r[4]
			self.get_theat().create_occupation(r[0], r[1], r[2], self.get_theat().get_actor(ac), \
				self.get_theat().get_spectacle(sp))
		conn.close()

	def write(self):
		conn = db.connect(self.get_outfile())
		curs = conn.cursor()
		curs.executescript(emptydb)
		for ac in self.get_theat().get_actors_list():
			curs.execute("insert into actor(code, surname, name, secname, rank, experience) values(?, ?, ?, ?, ?, ?)",\
			 ( ac.get_code(), ac.get_surname(), ac.get_name(), ac.get_secname(), ac.get_rank(), ac.get_experience() ))
		for sp in self.get_theat().get_spectacles_list():
			curs.execute("insert into spectacle(code, title, year, budget) values(?, ?, ?, ?)",\
			 ( sp.get_code(), sp.get_title(), sp.get_year(), sp.get_budget() ))
		for a in self.get_theat().get_occupations_list():
			if a.get_actor():
				ac = a.get_actor().get_code()
			else:
				ac = "NULL"
			if a.get_spectacle():
				sp = a.get_spectacle().get_code()
			else:
				sp = "NULL"
			curs.execute("insert into occupation(code, role, contract_cost, actor, spectacle) values(?, ?, ?, ?, ?)",\
			 ( a.get_code(), a.get_role(), a.get_contract_cost(), ac, sp ))
		conn.commit()
		conn.close()