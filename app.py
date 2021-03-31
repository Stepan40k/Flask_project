from flask import Flask, render_template # сперва подключим модуль
from data import title,subtitle,tours,departures,description

app = Flask(__name__) # объявим экземпляр фласка

@app.route('/')
def render_main():
   return render_template('index.html',
                          main_title=title,
                          dps=departures,
                          desc=description,
                          subtit=subtitle,
                          tours=tours,deps=departures)

@app.route('/departures/<departure>/')
def render_departure(departure):
    dep_dict = {'Moscow':'C Москвы',
                'Spb':'Из Санкт-Петербурга',
                'Kazan':'Из Казани',
                'Novosib':'Из Новосибирска',
                'Eburg':'Из Екатеринбургу'}
    return render_template('departure.html',
                           deps=departures,
                           cur_dep=departure, main_title=title,
                           dep_dict=dep_dict)

@app.route('/tours/<int:id>/')
def render_tour(id):
    return render_template('tour.html', main_title=title, tour=tours, id=id, dps=departures)

app.run() # запустим сервер