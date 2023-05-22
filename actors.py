from general import General
class Actors(General):
    #(Surname, Name, Secname , Rank  , Experience)
    #(Фамилия, Имя , Отчество, Звание, Стаж)
    def __init__(self, code=0, surname='', name='', secname='', rank='', experience=0):
        General.__init__(self, code)
        self.set_surname(surname)
        self.set_name(name)
        self.set_secname(secname)
        self.set_fio(surname, name, secname)
        self.set_rank(rank)
        self.set_experience(experience)

    def set_surname(self, surname):
        self.__surname = surname
    def set_name(self, name):
        self.__name = name
    def set_secname(self, secname):
        self.__secname = secname
    def set_fio(self, surname, name, secname):
        if (self.__name == '' or self.__surname == '' or self.__secname == ''):
            self.__fio = ''
        else:
            self.__fio = self.__surname + " " + self.__name[0] + ". " + self.__secname[0] + "."
    def set_rank(self, rank):
        self.__rank = rank
    def set_experience(self, experience):
        self.__experience = experience
        """
        if experience % 10 == 1:
            self.__experience = str(experience) + ' год'
        elif (experience % 10 == 2 or experience % 10 == 3 or experience % 10 == 4) and (experience < 10 or experience > 20):
            self.__experience = str(experience) + ' года'
        else:
            self.__experience = str(experience) + ' лет'
        """

    def get_surname(self):
        return self.__surname
    def get_name(self):
        return self.__name
    def get_secname(self):
        return self.__secname
    def get_fio(self):
        return self.__fio
    def get_rank(self):
        return self.__rank
    def get_experience(self):
        return self.__experience
    def get_code(self):
        return super().get_code()