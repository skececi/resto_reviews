# Sam Kececi
# 2018
import requests
import json
import config

def get_resto_data(input_search):
  google_API_key = config.google_API_key

  fields = ['name', 'formatted_address', 'rating', 'opening_hours']
  fields_formatted = ",".join(fields)

  parameters = {'key' : google_API_key, 'input' : input_search, 'inputtype' : 'textquery', 'fields' : fields_formatted, 'locationbias' : 'ipbias'}

  response = requests.get("https://maps.googleapis.com/maps/api/place/findplacefromtext/json", params=parameters)

  return(response.json())

# takes list of resto search strings and returns a dict of resto name, rating, location
# sorted by highest to lowest rating
def highest_rated_from_list(resto_list):
  raw_data_list = []
  for resto in resto_list:
      raw_data_list.append(get_resto_data(resto))


  ratings_list = []

  for entry in raw_data_list:
    # take first candidate (if multiple)
    entry = entry["candidates"][0]
    ratings_list.append((entry["name"], entry["rating"], entry["formatted_address"]))

  return ratings_list

# print(get_resto_data('jin ramen'))
resto_list_test = ['ippudo ramen', 'jin ramen', 'momofuku noodle bar']
print(highest_rated_from_list(resto_list_test))

# TODO: how long of a drive/walk from current location/address


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
