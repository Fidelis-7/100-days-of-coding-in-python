travel_log = [
{
    "country":"France",
    "visits": 12,
    "cities": ["Bordeaux", "Paris", "Lyon"],

},

    {
    "country":"Ghana",
    "visits":5,
    "cities":["Accra", "Tema", "Kasoa"]
    }

]

# adding countries to the travel log

def add_new_country(country, visits, cities):
    new_country = {}
    new_country["country"] = country
    new_country["visits"] = visits
    new_country["cities"] = cities
    travel_log.append(new_country)


add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
add_new_country("Nigeria", 3, ["Lagos", "Delta"])
print(travel_log)