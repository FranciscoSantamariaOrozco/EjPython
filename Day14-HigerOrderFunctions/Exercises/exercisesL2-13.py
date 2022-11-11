#Exercises - Day 13
print()

# L2-13 - Crea una función que devuelva un diccionario, donde las llaves sean la letra de comienzo de los paises 
# y los valores el número de paises que comienzan por esa letra.


"""Imports, listas y variables"""
from string import ascii_uppercase
Abecedario = ascii_uppercase
# Lista de países.
countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Cape Verde',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombi',
  'Comoros',
  'Congo (Brazzaville)',
  'Congo',
  'Costa Rica',
  "Cote d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor Timur)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia, The',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Macedonia',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia and Montenegro',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Swaziland',
  'Sweden',
  'Switzerland',
  'Syria',
  'Taiwan',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe',
]


"""Funciones"""
# Función encargada de sacar un conteo de cuantos países comienzan por cada letra.
def ContarPaises(Lista):
  ConteoTotales = []
  for i in range(len(Abecedario)):                  # Definimos un bucle que itere sobre la lista abecedario.
    Count = 0                                       # Declaramos el conteo de cada letra aquí, para que se resetee a cada ciclo del bucle for.
    for i2 in range(len(Lista)):                    # Definimos otro bucle qe itere sobre la lista de países.
      Pais = Lista[i2]                              # Declaramos una variable str "Pais", que contenga el valor del país de la lista que estamos procesando.
      if Pais.startswith(Abecedario[i]) is True:    # Si el pais que estamos procesando comienza por la letra indicada....
        Count += 1                                  # Aumentamos el contador en 1, y aumentamos i2 para pasar al siguiente país.
        i2 = i2 + 1
      else:                                         # Si no simplemente pasamos al siguiente país.
        i2 = i2 + 1     
    ConteoTotales.append(Count)                     # Una vez finalizado el bucle for i2 que itera por todos los países, añadimos el valor actual de count
  return ConteoTotales                              # a conteo totales. Finalmente obtendremos una lista "Conteo totales" con la cantidad de paises que empiezan con cada letra, ordenado alfabeticamente.
# Función encargada de crear un diccionario, partiendo de la lista abecedario, y la función ContarPaises
def Diccionario(lista):
  Dicc = dict()
  ListaTodolisto = ContarPaises(lista)            # Primero pasamos el resultado de la función contar paises a una lista.
  for i in range(len(Abecedario)):                # Declaramos un bucle for que itera sobre el Abecedario.
      Dicc[Abecedario[i]] = ListaTodolisto[i]     # En cada loop, añade la letra que ocupa la posición x, con el valor correspondiente.
  return Dicc                                     # Devolvemos el diccionario como resultado.
DiccionarioSolucionado = Diccionario(countries)


"""Programa"""
Consulta = input("Introduce la letra de la que quieres comprobar la cantidad de países: ")
Consulta = Consulta.upper()
if Abecedario.count(Consulta) == 1:
  print(DiccionarioSolucionado.get(Consulta), "países comienzan por la letra", Consulta,".")
  print()
else:
  print("Error. Debes introducir una sola letra, los números no son validos.")
  print()