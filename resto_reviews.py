# Sam Kececi
# 2018
import requests
import json


def get_resto_data(input_search):
  google_API_key = "AIzaSyA6cM8bxbFvn9ZyLqIINIAeKEhKo_-vVC8"

  fields = ['name', 'formatted_address', 'rating', 'opening_hours']
  fields_formatted = ",".join(fields)

  print(fields_formatted)

  parameters = {'key' : google_API_key, 'input' : input_search, 'inputtype' : 'textquery', 'fields' : fields_formatted, 'locationbias' : 'ipbias'}

  response = requests.get("https://maps.googleapis.com/maps/api/place/findplacefromtext/json", params=parameters)

  return(response.json())

# takes list of resto search strings and returns a dict of resto name, rating, location
# sorted by highest to lowest rating
def highest_rated_from_list(resto_list):
  raw_data_list = []
  for resto in resto_list:
      raw_data_list.append(get_resto_data(resto))

  # {name : rating}
  ratings_dict = {}

  for entry in raw_data_list:
    # take first candidate (if multiple)
    entry = entry["candidates"][0]
    name = entry["name"]
    rating = entry["rating"]
    ratings_dict[name] = rating

  top_ratings = sorted(ratings_dict, key=ratings_dict.get)
  print(top_ratings)





# print(get_resto_data('jin ramen'))
resto_list_test = ['ippudo ramen', 'jin ramen', 'momofuku noodle bar']
highest_rated_from_list(resto_list_test)

"""
{
  "candidates": [
    {
      "formatted_address": "462 Amsterdam Ave, New York, NY 10024, USA",
      "name": "Jin Ramen",
      "opening_hours": {
        "open_now": "TRUE",
        "weekday_text": []
      },
      "rating": 4.4
    },
    {
      "formatted_address": "3183 Broadway, New York, NY 10027, USA",
      "name": "Jin Ramen",
      "opening_hours": {
        "open_now": "TRUE",
        "weekday_text": []
      },
      "rating": 4.4
    }
  ],
  "debug_log": {
    "line": []
  },
  "status": "OK"
}
"""
