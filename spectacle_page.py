head = '<center><header>Спектакли</header><br>' + '<a href=..>%s</a><br><br><a href=editline>%s</a><br><br>'%(u'Назад',u'Добавить') \
    + '<table><th></th><th>%s</th><th>%s</th><th>%s</th>'%(u'Название',u'Год',u'Бюджет')
class spectacle_page:
    def __init__(self,theat):
        self.__theat=theat
    def index(self):
        s= head
        r=1
        bg=''
        for k in self.__theat.get_spectacles_list():
            s+='<tr%s><td>%d</td>'%(bg,r)
            s+='<td>%s</td>'% k.get_title()
            s+='<td>%s</td>'% k.get_year()
            s+='<td>%s</td>'% k.get_budget()
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
            code = self.__theat.get_spectacle_new_code()
            s = self.index()[:-8]
            if code%2==0:bg=' bgcolor=silver'
            else:bg=''
            s+='<tr%s><td>%d</td>'%(bg,code)
            s+= '<td><input form="new_spectacle" type=text name=title></td>'
            s+= '<td><input form="new_spectacle" type=number name=year></td>'
            s+= '<td><input form="new_spectacle" type=number name=budget></td>'
            s+= '<td><input form="new_spectacle" type=submit value="Подтвердить"></td>'
            s+='<td><a href=.>%s</a></td></tr>'%(u'Отменить')
            s+='</table>'
            s+= '<form id="new_spectacle" action="saveline"></form>'
        else:
            s= head
            r=1
            bg=''
            for k in self.__theat.get_spectacles_list():
                s+='<tr%s><td>%d</td>'%(bg,r)
                if k.get_code() != int(code):
                    s+='<td>%s</td>'% k.get_title()
                    s+='<td>%s</td>'% k.get_year()
                    s+='<td>%s</td>'% k.get_budget()
                    s+='<td><a href=editline?code=%s>%s</a></td>'%(k.get_code(),u'Редактировать')
                    s+='<td><a href=deleteline?code=%s>%s</a></td></tr>'%(k.get_code(),u'Удалить')
                else:
                    s+='<input form="red_spectacle" name=code hidden=on value="%s">'% int(code)
                    s+='<td><input form="red_spectacle" type=text name=title value="%s"></td>'% k.get_title()
                    s+='<td><input form="red_spectacle" type=number name=year value="%s"></td>'% k.get_year()
                    s+='<td><input form="red_spectacle" type=number name=budget value="%s"></td>'% k.get_budget()
                    s+= '<td><input form="red_spectacle" type=submit value="Подтвердить"></td>'
                    s+='<td><a href=.>%s</a></td></tr>'%(u'Отменить')
                r+=1
                if bg:bg=''
                else:bg=' bgcolor=silver'
            s+='</table>'
            s+= '<form id="red_spectacle" action="changeline"></form>'
        return s
    editline.exposed = True

    def saveline(self, title, year, budget):
        code=self.__theat.get_spectacle_new_code()
        self.__theat.create_spectacle(code,title,year,budget)
        return self.index()
    saveline.exposed = True

    def changeline(self, code, title, year, budget):
        self.__theat.get_spectacle(int(code)).set_title(title)
        self.__theat.get_spectacle(int(code)).set_year(year)
        self.__theat.get_spectacle(int(code)).set_budget(budget)
        return self.index()
    changeline.exposed = True

    def deleteline(self,code):
        if (self.__theat.remove_spectacle(int(code))):
            return self.index()
        else:
            s = self.index()
            s += '''
                <div id="deleteline">
                <window>
                Данный спектакль задействован в выступлении <br>и не может быть удалён<br><br>
                <a href=. class="close_window">Закрыть</a>
                </window>
                </div>
            '''
            return s
    deleteline.exposed = True