import requests

url = 'https://dbd-api.herokuapp.com'
shrine_url = 'https://dbd.onteh.net.au/api/shrine?includeperkinfo=1'
shrine_perk_img_url = 'https://dbd-api.herokuapp.com/perks?perk_tag='


def get_killers():
    killers = requests.request('GET', f'{url}/killers').json()
    # characters = get_characters()
    # # killers.filter(killers.role == 'killer')
    # killers = []
    # survivors = []
    # for character in characters:
    #     if characters[character]['role'] == 'killer':
    #         killers.append(characters[character])

    return killers


def get_survivors():
    survivors = requests.request('GET', f'{url}/survivors').json()

    return survivors


def get_killer_by_name_tag(name_tag):
    killer = requests.request('GET', f'{url}/killers?name_tag={name_tag}').json()

    return killer


def get_survivor_by_name_tag(name_tag):
    survivor = requests.request('GET', f'{url}/survivors?name_tag={name_tag}').json()

    return survivor


def get_perks_by_name_tag(name_tag):
    perks = requests.request('GET', f'{url}/perks?name_tag={name_tag}&lang=en').json()

    return perks

def get_shrine_perks():
    shrine_perks = requests.request('GET', shrine_url).json()

    return shrine_perks

def get_shrine_perks_img(perk_tag):
    shrine_perk_img = requests.request('GET', f'{shrine_perk_img_url}{perk_tag}&lang=en').json()

    return shrine_perk_img