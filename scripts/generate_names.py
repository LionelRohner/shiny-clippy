from names_dataset import NameDataset

nd = NameDataset()

# Params
n = 2
countries = []
# print(nd.get_country_codes())

# Get names
male_names = nd.get_top_names(n=n, gender="Male", use_first_names=True)
female_names = nd.get_top_names(n=n, gender="Female", use_first_names=True)
lastnames = nd.get_top_names(n=n, use_first_names=False)

# Unpack and flatten
male_names = [
    name
    for country in male_names.values()
    for names in country.values()
    for name in names
]

female_names = [
    name
    for country in female_names.values()
    for names in country.values()
    for name in names
]

lastnames = [name for country in lastnames.values() for name in country]

all_names = sorted(male_names + female_names + lastnames)

# Simplify
all_names = {name for name in all_names}

# Write file
with open("../data/names.txt", "w+") as file:
    for name in all_names:
        file.write(name + "\n")

print(f"Generated {len(all_names)} names in data/names.txt!")
