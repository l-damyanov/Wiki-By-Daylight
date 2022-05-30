import re

from asyncio import constants
from flask import Flask, render_template, redirect, url_for

from api import get_killers, get_shrine_perks, get_shrine_perks_img, get_survivors, get_killer_by_name_tag, get_perks_by_name_tag, get_survivor_by_name_tag

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return redirect(url_for('home_page'))


@app.route('/home_page')
def home_page():
    killers = get_killers()
    survivors = get_survivors()
    return render_template('index.html', killers=killers, survivors=survivors)


@app.route('/details/killer/<name_tag>')
def killer_details_page(name_tag):
    killer = get_killer_by_name_tag(name_tag)[0]
    perks = get_perks_by_name_tag(name_tag)
    return render_template('details.html', killer=killer, perks=perks)


@app.route('/details/survivor/<name_tag>')
def survivor_details_page(name_tag):
    survivor = get_survivor_by_name_tag(name_tag)[0]
    perks = get_perks_by_name_tag(name_tag)
    return render_template('details.html', survivor=survivor, perks=perks)

@app.route('/shrine')
def shrine_page():
    data = get_shrine_perks()
    shrine_perks = data['perks']
    filtered_perks = []
    CLEANR = re.compile('<.*?>') 

    for perk in shrine_perks:
        perk_tag = "".join(perk['name'].split(' '))
        perk_tag = "".join(perk_tag.split(':'))
        shrine_perk_img = get_shrine_perks_img(perk_tag)[0]
        perk['icon'] = shrine_perk_img['icon']
        cleantext = re.sub(CLEANR, '', str(perk['description']))
        perk['description'] = cleantext
        filtered_perks.append(perk)
    return render_template('shrine.html', shrine_perks=filtered_perks)

@app.route('/contacts')
def contacs_page():
    return render_template('contacts.html')

if __name__ == '__main__':
    app.run()
