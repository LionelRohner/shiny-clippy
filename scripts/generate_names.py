import pandas as pd
import re
import requests
from names_dataset import NameDataset
from pathlib import Path

# Path handling
base = Path(__file__).resolve().parent
data_file = base / ".." / "data" / "names.txt"
data_file = data_file.resolve()


# Functions
def convert_to_pd(data: dict) -> pd.DataFrame:
    df = []

    for country, genders in data.items():
        if isinstance(genders, dict):
            for gender, names in genders.items():
                for name in names:
                    df.append(
                        {
                            "name": name,
                            "gender": gender,
                            "country_alpha2": country,
                        }
                    )
        # If genders is not a dict, then its a list of names
        else:
            for name in genders:
                df.append(
                    {"name": name, "gender": None, "country_alpha2": country}
                )

    return pd.DataFrame(df)


# Pattern: match any character NOT in Latin ranges (U+0000–U+024F)
latin_regex = re.compile(r"[^\u0000-\u024F]")


def is_latin(text: str, latin_regex: re.Pattern[str]) -> bool:
    return not bool(re.search(latin_regex, text))


# test = [
#     "ឡាំ យ៉ង",
#     "Khemra",
#     "Løvër",
#     "Tynii",
#     "សួុន.ឆៃយ៉ាទ្ធី.មានជយ័n",
#     "Sokon",
#     "Bakkeng",
#     "Vännâk",
#     "Mengly",
#     "Preyveng",
# ]
#
# for t in test:
#     print(is_latin(t, latin_regex))

# Get data ----

# Countries
# Select countries  from restcountries API
# fields: https://gitlab.com/restcountries/restcountries/-/blob/master/FIELDS.md
fields = ["cca2", "population"]
url = f"https://restcountries.com/v3.1/all?fields={','.join(fields)}"
response = requests.get(url)
data = response.json()

countries_api = pd.json_normalize(data)

# Names
nd = NameDataset()
countries_names = [c.alpha_2 for c in nd.get_country_codes()]

# Remove countries not present in names dataset
countries_api = countries_api.loc[countries_api["cca2"].isin(countries_names)]


# Hyperparams for output
n = 3000  # per country
top_n_countries = 20
countries_api_top = (
    countries_api.sort_values("population", ascending=False)
    .head(top_n_countries)["cca2"]
    .tolist()
)
print(countries_api_top)
# Extract names
male_names = nd.get_top_names(n=n, gender="Male", use_first_names=True)
male_names = convert_to_pd(male_names)

female_names = nd.get_top_names(n=n, gender="Female", use_first_names=True)
female_names = convert_to_pd(female_names)

lastnames = nd.get_top_names(n=n, use_first_names=False)
lastnames = convert_to_pd(lastnames)

all_names = pd.concat([male_names, female_names, lastnames], ignore_index=True)

all_names_filtered = all_names.loc[
    all_names["country_alpha2"].isin(countries_api_top)
]

# Remove non-latin and dedup
all_names_filtered["is_latin"] = all_names["name"].apply(
    lambda text: is_latin(text, latin_regex)
)
latin_names = all_names_filtered[all_names_filtered["is_latin"]]
unique_names = latin_names["name"].unique()

# Write file
with data_file.open("w+") as file:
    for name in unique_names:
        file.write(name + "\n")

print(f"Generated {len(unique_names)} names in {data_file}!")
