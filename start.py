import cherrypy
import sys
sys.path.insert(0, "./library")

from theatre import Theatre
from datajson import datajson
from datasql import datasql
from actors_page import actors_page
from spectacle_page import spectacle_page
from occupation_page import occupation_page
class start:
    def __init__(self):
        self.__theat=Theatre()
        #self.__datajson=datajson(self.__theat, 'data.json', 'data.json')
        #self.__datajson.read()
        self.__datasql=datasql(self.__theat,'data.sqlite')
        self.__datasql.read()
        self.actors_page=actors_page(self.__theat)
        self.spectacle_page=spectacle_page(self.__theat)
        self.occupation_page=occupation_page(self.__theat)

    def index(self):
        s = """
                    <body><center><header>Занятость в театре</header><br><br>
                    <a class="btn-class" href=actors_page\>Актёры</a><br>
                    <a class="btn-class" href=spectacle_page\>Спектакли</a><br>
                    <a class="btn-class" href=occupation_page\>Выступления</a><br><br>
                    <a href="load">Загрузить</a><br>
                    <a href="save">Сохранить</a><br>
                    <a href="clen">Очистить</a>
                    </center></body>
                """
        return s
    index.exposed=True

    def load(self):
        s = self.index()
        s += '''
            <div id="deleteline">
            <window>
            <b>Импорт данных</b><br>
            Не забудьте сначала сделать резервную копию ваших данных! Все данные будут заменены!<br><br>
            <input form="load" type="file" name=page accept=".json, .SQLITE">
            <input form="load" type=submit value="Подтвердить">
            <form id="load" action="loader"></form>
            <a href=. class="close_window">Закрыть</a>
            </window>
            </div>
        '''
        return s
    load.exposed = True

    def loader(self, page):
        self.__theat=Theatre()
        if page.endswith('.json'):
            self.__datajson=datajson(self.__theat, page, page)
            self.__datajson.read()
        elif page.endswith('.sqlite'):
            self.__datasql=datasql(self.__theat, page, page)
            self.__datasql.read()
        self.actors_page=actors_page(self.__theat)
        self.spectacle_page=spectacle_page(self.__theat)
        self.occupation_page=occupation_page(self.__theat)
        return self.index()
    loader.exposed = True

    def save(self):
        s = self.index()
        s += '''
            <div id="deleteline">
            <window>
            <b>Экспорт данных</b><br>
            Вы можете сохранить данные в одном из предложенных форматов. Не забудьте указать имя файла.<br><br>
            <form id="json" action="savejson"><input type="text" placeholder="Имя файла" name=name><input type=submit value="Сохранить как json">
            </form>
            <form id="sql" action="savesql"><input type="text" placeholder="Имя файла" name=name><input type=submit value="Сохранить как SQlite">
            </form>
            <a href=. class="close_window">Закрыть</a>
            </window>
            </div>
        '''
        return s
    save.exposed = True

    def savejson(self, name):
        name += '.json'
        self.__datajson=datajson(self.__theat, name, name)
        self.__datajson.write()
        s = self.index()
        s += '''
            <div id="deleteline">
            <window>
            Файл %s успешно сохранён.
            <a href=. class="close_window">Закрыть</a>
            </window>
            </div>
        ''' % name
        return s
    savejson.exposed = True
    def savesql(self, name):
        name += '.sqlite'
        self.__datasql=datasql(self.__theat, name, name)
        self.__datasql.write()
        s = self.index()
        s += '''
            <div id="deleteline">
            <window>
            Файл %s успешно сохранён.
            <a href=. class="close_window">Закрыть</a>
            </window>
            </div>
        ''' % name
        return s
    savesql.exposed = True
    def clen(self):
        self.__theat=Theatre()
        self.actors_page=actors_page(self.__theat)
        self.spectacle_page=spectacle_page(self.__theat)
        self.occupation_page=occupation_page(self.__theat)
        s = self.index()
        s += '''
            <div id="deleteline">
            <window>
            Все данные очищены.<br><br>
            <a href=. class="close_window">Закрыть</a>
            </window>
            </div>
        '''
        return s
    clen.exposed = True
    
root=start()
cherrypy.config.update({
'log.screen': True,
})

cherrypy.tree.mount(root)

if __name__ == '__main__':
    cherrypy.engine.start()
    cherrypy.engine.block()