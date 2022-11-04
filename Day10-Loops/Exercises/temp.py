# temp
DatosPaises =[
    {
        "name": "Afghanistan",
        "capital": "Kabul",
        "languages": [
            "Pashto",
            "Uzbek",
            "Turkmen"
        ],
        "population": 27657145,
        "flag": "https://restcountries.eu/data/afg.svg",
        "currency": "Afghan afghani"
    },
        {
        "name": "Åland Islands",
        "capital": "Mariehamn",
        "languages": [
            "Swedish",
            "Albanian"
        ],
        "population": 28875,
        "flag": "https://restcountries.eu/data/ala.svg",
        "currency": "Euro"
    },
    {
        "name": "Albania",
        "capital": "Tirana",
        "languages": [
            "Albanian"
        ],
        "population": 2886026,
        "flag": "https://restcountries.eu/data/alb.svg",
        "currency": "Albanian lek"
    },
]


MasHablados = []
for i in range(len(DatosPaises)):
        if len(DatosPaises[i]["languages"]) > 1:
            for ipais in range(len(DatosPaises[i]["languages"])):
                MasHablados.append(DatosPaises[i]["languages"][ipais])
                ipais = ipais + 1
        else:
            MasHablados.append(DatosPaises[i]["languages"][0])

LengUnicos = set(MasHablados)
LengUnicos = list(LengUnicos)

Diccionario = {}


"""
Lenguas = set()
for i in range(len(DatosPaises)):
    print(DatosPaises[i]["languages"])
    Lenguas.update(DatosPaises[i]["languages"])
print()
print(len(Lenguas))
"""