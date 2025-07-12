## Lets see some child abuse report just to Weight the whole thing down >:)
Countys_USA_2020_per1000 = {'California': 43.5,
  'Modoc_County': 132.2,  
  'Del_Norte_County' : 115.7,
  'Lassen_County'	: 109.1,
  'Siskiyou_County' :	100.5,
  'Calaveras_County' : 96.6,
  'Mendocino_County' : 95.9,
  'Trinity_County' : 89.0,
  'Amador_County' : 88.9,
  'Tuolumne_County' :	86.8,
  'Tehama_County'	: 78.9,
  'Humboldt_County'	: 77.8,
  'Madera_County'	: 77.1,
  'Shasta_County'	: 77.1,
  'Lake_County'	: 74.2,
  'Glenn_County' :	73.4,
  'Nevada_County'	: 72.8,
  'Inyo_County'	: 71.5,
  'Butte_County' : 67.4,
  'Yuba_County'	: 65.5,
  'Mariposa_County'	: 61.5,
  'Fresno_County'	: 61.3,
  'Mono_County'	: 60.2,
  'Tulare_County'	: 58.9,
  'Merced_County'	: 58.0,
  'San_Luis_Obispo_County' :	57.7,
  'Stanislaus_County'	: 57.3,
  'Imperial_County'	: 57.0,
  'Riverside_County' : 56.9,
  'Plumas_County'	: 55.0,
  'Kern_County' : 53.2,
  'Santa_Barbara_County' : 53.2,
  'San_Diego_County' : 50.4,
  'Sacramento_County' : 50.3,
  'Solano_County' : 50.3,
  'Sonoma_County'	: 48.3,
  'El_Dorado_County' : 47.7,
  'Kings_County' : 46.5,
  'Napa_County'	: 46.3,
  'San_Bernardino_County' : 46.3,
  'Ventura_County' : 46.1,
  'San_Benito_County' : 45.5,
  'Sutter_County' : 43.5,
  'Placer_County' : 43.3,
  'Yolo_County'	: 43.0,
  'Colusa_County' : 42.8,
  'San_Joaquin_County' : 41.8,
  'Los_Angeles_County' : 40.7,
  'Monterey_County' : 36.4,
  'Santa_Cruz_County'	: 35.7,
  'Orange_County'	: 34.7,
  'Contra_Costa_County'	: 34.0,
  'San_Francisco_County' : 33.4,
  'Alameda_County' : 29.1,
  'San_Mateo_County' : 25.0,
  'Santa_Clara_County' : 25.0,
  'Marin_County'	: 19.8,
  'Alpine_County'	: None,
  'Sierra_County'	: None}
def Show_me(mode : str, target = None):
  print("The rate of juvenile abuse's report is represented in terms of the rate per thousand for the year of 2020 [USA]:\n")
  if mode == 'all': 
    for key, value in Countys_USA_2020_per1000.items():
      print(f"In the {key} a total of {value} out of 1000 childs were reported as been abused\n")
  elif mode == 'sing':
    for key, value in Countys_USA_2020_per1000.items():
      if key.lower() == target:
         print(f"In the {key} a total of {value} out of 1000 childs were reported as been abused\n")
  elif mode == 'mult':
    for key, value in Countys_USA_2020_per1000.items():
      if key.lower() in target:
         print(f"In the {key} a total of {value} out of 1000 childs were reported as been abused\n")
Show_me('all')
