countries = input().split(", ")
capitals = input().split(", ")

my_dict = {country: capital for country, capital in tuple(zip(countries, capitals))}
[print(f"{country} -> {capital}") for country, capital in my_dict.items()]
