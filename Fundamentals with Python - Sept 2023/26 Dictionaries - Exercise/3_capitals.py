country_list = input().split(", ")
capital_list = input().split(", ")

my_dict = dict(zip(country_list, capital_list))

for country, capital in my_dict.items():
    print(f"{country} -> {capital}")