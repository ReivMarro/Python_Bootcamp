# Previously we took json from API and worked with it, so it was formattable and could be worked as a dictionary using python
# We are going to work with information that comes in the format of a string
# We need to convert this using the json library
import json

R5D4 = '''{
	"name": "R5-D4",
	"height": "97",
	"mass": "32",
	"hair_color": "n/a",
	"skin_color": "white, red",
	"eye_color": "red",
	"birth_year": "unknown",
	"gender": "n/a",
	"homeworld": "https://swapi.dev/api/planets/1/",
	"films": [
		"https://swapi.dev/api/films/1/"
	],
	"species": [
		"https://swapi.dev/api/species/2/"
	],
	"vehicles": [],
	"starships": [],
	"created": "2014-12-10T15:57:50.959000Z",
	"edited": "2014-12-20T21:17:50.321000Z",
	"url": "https://swapi.dev/api/people/8/"
}'''
R5D4 = json.loads(R5D4) # We are taking the string and throwing it in a conversion tool and turned it into a dictionary
print(R5D4['name'])
# We can also edit information thanks to the conversion tools available
R5D4['name'] = "Robot 5 Data 4"
R5D4_str = json.dumps(R5D4) # 'dumps' stands for 'dump string'
print(R5D4_str)
# With all of this we have taken a string and converted it to a dictionary using '.loads'
# Then we changed the name and dumped that data back into a string using '.dumps'