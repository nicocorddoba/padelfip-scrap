from plugins.scrap.scrap import run

url = "https://www.padelfip.com/es/calendario-premier-padel/?events-year="
gender_arg = "Men" #Men or Women

if __name__ == "__main__":
    list_events = run(url + "2024", gender_arg)