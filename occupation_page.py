head = '<center><header>Выступления</header><br>' + '<a href=..>%s</a><br><br><a href=editline>%s</a><br><br>'%(u'Назад',u'Добавить') \
    + '<table><th></th><th>%s</th><th>%s</th><th>%s</th><th>%s</th>'%(u'Актёр',u'Спектакль',u'Роль',u'Стоимость контракта')
class occupation_page:
    def __init__(self,theat):
        self.__theat=theat
    def index(self):
        s=head
        r=1
        bg=''
        for k in self.__theat.get_occupations_list():
            s+='<tr%s><td>%d</td>'%(bg,r)
            s+='<td>%s</td>'% k.get_actor_fio()
            s+='<td>%s</td>'% k.get_spectacle_title()
            s+='<td>%s</td>'% k.get_role()
            s+='<td>%s</td>'% k.get_contract_cost()
            s+='<td><a href=editline?code=%s>%s</a></td>'%(k.get_code(),u'Редактировать')
            s+='<td><a href=deleteline?code=%s>%s</a></td></tr>'%(k.get_code(),u'Удалить')
            r+=1
            if bg:bg=''
            else:bg=' bgcolor=silver'
        s+='</table>'
        return s
    index.exposed=True
    def editline(self, code=0):
        if code==0:
            code = self.__theat.get_occupation_new_code()
            s = self.index()[:-8]
            if code%2==0:bg=' bgcolor=silver'
            else:bg=''
            s+='<tr%s><td>%d</td>'%(bg,code)
            s+= '<td><select name=actor form="new_occupation">'
            for c in self.__theat.get_actors_list():
                s+= '<option value=%s>%s</option>'%(str(c.get_code()),c.get_fio())
            s+= '</select>'
            s+= '<td><select name=spectacle form="new_occupation">'
            for c in self.__theat.get_spectacles_list():
                s+= '<option value=%s>%s</option>'%(str(c.get_code()),c.get_title())
            s+= '</select>'
            s+= '<td><input form="new_occupation" type=text name=role></td>'
            s+= '<td><input form="new_occupation" type=number name=contract_cost></td>'
            s+= '<td><input form="new_occupation" type=submit value="Подтвердить"></td>'
            s+='<td><a href=.>%s</a></td></tr>'%(u'Отменить')
            s+='</table>'
            s+= '<form id="new_occupation" action="saveline"></form>'
        else:
            s= head
            r=1
            bg=''
            for k in self.__theat.get_occupations_list():
                s+='<tr%s><td>%d</td>'%(bg,r)
                if k.get_code() != int(code):
                    s+='<td>%s</td>'% k.get_actor().get_fio()
                    s+='<td>%s</td>'% k.get_spectacle().get_title()
                    s+='<td>%s</td>'% k.get_role()
                    s+='<td>%s</td>'% k.get_contract_cost()
                    s+='<td><a href=editline?code=%s>%s</a></td>'%(k.get_code(),u'Редактировать')
                    s+='<td><a href=deleteline?code=%s>%s</a></td></tr>'%(k.get_code(),u'Удалить')
                else:
                    s+='<input form="red_occupation" name=code hidden=on value="%s">'% int(code)
                    s+= '<td><select name=actor form="red_occupation">'
                    for c in self.__theat.get_actors_list():
                        if c.get_code() == k.get_actor().get_code():
                            s+= '<option value=%s selected>%s</option>'%(str(c.get_code()),c.get_fio())
                        else: s+= '<option value=%s>%s</option>'%(str(c.get_code()),c.get_fio())
                    s+= '</select>'
                    s+= '<td><select name=spectacle form="red_occupation">'
                    for c in self.__theat.get_spectacles_list():
                        if c.get_code() == k.get_spectacle().get_code():
                            s+= '<option value=%s selected>%s</option>'%(str(c.get_code()),c.get_title())
                        else: s+= '<option value=%s>%s</option>'%(str(c.get_code()),c.get_title())
                    s+= '</select>'
                    s+='<td><input form="red_occupation" type=text name=role value="%s"></td>'% k.get_role()
                    s+='<td><input form="red_occupation" type=number name=contract_cost value="%s"></td>'% k.get_contract_cost()
                    s+= '<td><input form="red_occupation" type=submit value="Подтвердить"></td>'
                    s+='<td><a href=.>%s</a></td></tr>'%(u'Отменить')
                r+=1
                if bg:bg=''
                else:bg=' bgcolor=silver'
            s+='</table>'
            s+= '<form id="red_occupation" action="changeline"></form>'
        return s
    editline.exposed = True

    def saveline(self, actor, spectacle, role, contract_cost):
        code=self.__theat.get_occupation_new_code()
        act = self.__theat.get_actor(int(actor))
        spc = self.__theat.get_spectacle(int(spectacle))
        self.__theat.create_occupation(code,role,contract_cost,act,spc)
        return self.index()
    saveline.exposed = True

    def changeline(self, code, actor, spectacle, role, contract_cost):
        self.__theat.get_occupation(int(code)).set_role(role)
        self.__theat.get_occupation(int(code)).set_contract_cost(contract_cost)
        self.__theat.get_occupation(int(code)).set_actor(self.__theat.get_actor(int(actor)))
        self.__theat.get_occupation(int(code)).set_spectacle(self.__theat.get_spectacle(int(spectacle)))
        return self.index()
    changeline.exposed = True

    def deleteline(self,code):
        self.__theat.remove_occupation(int(code))
        return self.index()
    deleteline.exposed = True