# Sam Kececi
# 2018
import requests
import json

google_API_key = "AIzaSyA6cM8bxbFvn9ZyLqIINIAeKEhKo_-vVC8"
# input_search = 'jin ramen'
input_search = input("Enter a restaurant name")

fields = ['name', 'formatted_address', 'rating', 'opening_hours']
fields_formatted = ",".join(fields)

print(fields_formatted)

parameters = {'key' : google_API_key, 'input' : input_search, 'inputtype' : 'textquery', 'fields' : fields_formatted, 'locationbias' : 'ipbias'}

response = requests.get("https://maps.googleapis.com/maps/api/place/findplacefromtext/json", params=parameters)

print(response.content)
