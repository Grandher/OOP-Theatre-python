
head = '<center><header>Актёры</header><br>' + '<a href=..>%s</a><br><br><a href=editline>%s</a><br><br>'%(u'Назад',u'Добавить') \
    + '<table><th></th><th>%s</th><th>%s</th><th>%s</th><th>%s</th><th>%s</th>'%(u'Фамилия',u'Имя',u'Отчество',u'Звание',u'Стаж работы')
class actors_page:
    def __init__(self,theat):
        self.__theat=theat
    def index(self):
        s= head
        r=1
        bg=''
        for k in self.__theat.get_actors_list():
            s+='<tr%s><td>%d</td>'%(bg,r)
            s+='<td>%s</td>'% k.get_surname()
            s+='<td>%s</td>'% k.get_name()
            s+='<td>%s</td>'% k.get_secname()
            s+='<td>%s</td>'% k.get_rank()
            s+='<td>%s</td>'% k.get_experience()
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
            code = self.__theat.get_actor_new_code()
            s = self.index()[:-8]
            if code%2==0:bg=' bgcolor=silver'
            else:bg=''
            s+='<tr%s><td>%d</td>'%(bg,code)
            s+= '<td><input form="new_actor" type=text name=surname></td>'
            s+= '<td><input form="new_actor" type=text name=name></td>'
            s+= '<td><input form="new_actor" type=text name=secname></td>'
            s+= '<td><input form="new_actor" type=text name=rank></td>'
            s+= '<td><input form="new_actor" type=number name=experience></td>'
            s+= '<td><input form="new_actor" type=submit value="Подтвердить"></td>'
            s+='<td><a href=.>%s</a></td></tr>'%(u'Отменить')
            s+='</table>'
            s+= '<form id="new_actor" action="saveline"></form>'
        else:
            s= head
            r=1
            bg=''
            for k in self.__theat.get_actors_list():
                s+='<tr%s><td>%d</td>'%(bg,r)
                if k.get_code() != int(code):
                    s+='<td>%s</td>'% k.get_surname()
                    s+='<td>%s</td>'% k.get_name()
                    s+='<td>%s</td>'% k.get_secname()
                    s+='<td>%s</td>'% k.get_rank()
                    s+='<td>%s</td>'% k.get_experience()
                    s+='<td><a href=editline?code=%s>%s</a></td>'%(k.get_code(),u'Редактировать')
                    s+='<td><a href=deleteline?code=%s>%s</a></td></tr>'%(k.get_code(),u'Удалить')
                else:
                    s+='<input form="red_actor" name=code hidden=on value="%s">'% int(code)
                    s+='<td><input form="red_actor" type=text name=surname value="%s"></td>'% k.get_surname()
                    s+='<td><input form="red_actor" type=text name=name value="%s"></td>'% k.get_name()
                    s+='<td><input form="red_actor" type=text name=secname value="%s"></td>'% k.get_secname()
                    s+='<td><input form="red_actor" type=text name=rank value="%s"></td>'% k.get_rank()
                    s+='<td><input form="red_actor" type=number name=experience value="%s"></td>'% k.get_experience()
                    s+= '<td><input form="red_actor" type=submit value="Подтвердить"></td>'
                    s+='<td><a href=.>%s</a></td></tr>'%(u'Отменить')
                r+=1
                if bg:bg=''
                else:bg=' bgcolor=silver'
            s+='</table>'
            s+= '<form id="red_actor" action="changeline"></form>'
        return s
    editline.exposed = True

    def saveline(self, surname, name, secname, rank, experience):
        code=self.__theat.get_actor_new_code()
        self.__theat.create_actor(code,surname,name,secname,rank,experience)
        return self.index()
    saveline.exposed = True

    def changeline(self, code, surname, name, secname, rank, experience):
        self.__theat.get_actor(int(code)).set_surname(surname)
        self.__theat.get_actor(int(code)).set_name(name)
        self.__theat.get_actor(int(code)).set_secname(secname)
        self.__theat.get_actor(int(code)).set_rank(rank)
        self.__theat.get_actor(int(code)).set_experience(experience)
        return self.index()
    changeline.exposed = True

    def deleteline(self,code):
        if (self.__theat.remove_actor(int(code))):
            return self.index()
        else:
            s = self.index()
            s += '''
                <div id="deleteline">
                <window>
                Данный актёр задействован в выступлении <br>и не может быть удалён<br><br>
                <a href=. class="close_window">Закрыть</a>
                </window>
                </div>
            '''
            return s
    deleteline.exposed = True