from general import General
class Spectacle(General):
    #(Title   , Year, Budget)
    #(Название, Год , Бюджет)
    def __init__(self, code=0, title='', year=0, budget=0):
        General.__init__(self, code)
        self.set_title(title)
        self.set_year(year)
        self.set_budget(budget)

    def set_title(self, title):
        self.__title = title
    def set_year(self, year):
        self.__year = year
    def set_budget(self, budget):
        self.__budget = budget
        #self.__budget = str(budget) + ' млн. рублей'

    def get_title(self):
        return self.__title
    def get_year(self):
        return self.__year
    def get_budget(self):
        return self.__budget