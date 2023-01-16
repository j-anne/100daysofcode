travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇
def add_new_country(country, num_visit, city_visited):
    # travel_log.append({
#   "country": country,
#   "visits": num_visit,
#   "cities": city_visited
# })

  # Solution:
  new_country = {}
  new_country["country"] = country
  new_country["visits"] = num_visit
  new_country["cities"] = city_visited
  travel_log.append(new_country)

#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)