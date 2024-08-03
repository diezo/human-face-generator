from json import JSONDecodeError
from PIL import Image
from io import BytesIO
from time import time
import prompts
import sys
from requests import get, Response
from constants import genders, ages, ethnicities, genders_friendly, ages_friendly, ethnicities_friendly
from random import choice

# Load Random Parameters
if len(sys.argv) > 1 and sys.argv[1] == "random":

    # Fetch Dictionary Keys
    genders_keys: list[str] = list(genders.keys())
    ages_keys: list[str] = list(ages.keys())
    ethnicities_keys: list[str] = list(ethnicities.keys())

    # Remove "Random" Values (As We're Doing That Part)
    genders_keys.remove("r")
    ages_keys.remove("r")
    ethnicities_keys.remove("r")

    # Assign Random Values
    gender, age, ethnicity = (
        choice(genders_keys),
        choice(ages_keys),
        choice(ethnicities_keys)
    )

    # Accounce Chosen Values
    print(f"Gender: {genders_friendly[gender]}")
    print(f"Age: {ages_friendly[age]}")
    print(f"Ethnicity: {ethnicities_friendly[ethnicity]}")

# Ask for Parameters
else: gender, age, ethnicity = prompts.ask()

# Type Hinting
gender: str = gender
age: str = age
ethnicity: str = ethnicity

# Initiate HTTP Request
response: Response = get(
    url=f"https://this-person-does-not-exist.com/new"
    f"?time={str(int(time()))}"
    f"&gender={genders[gender]}"
    f"&age={ages[age]}"
    f"&etnic={ethnicities[ethnicity]}"
)

print()

# Request Succeeded?
if response.status_code == 200:

    try:
        response_dict: dict = response.json()

        if response_dict.get("generated", "") == "true":
            
            # Log Image Url
            url: str = "https://this-person-does-not-exist.com" + response_dict["src"]
            print(f"URL: {url}")

            # Show Image
            Image.open(BytesIO(get(url).content)).show()

        else:
            print(f"Unable to generate an image")
    
    # Invalid Response
    except JSONDecodeError:
        print(f"Unable to generate an image")

# Response Not 'OK'
else:
    print(f"Unable to generate an image\nStatus: {response.status_code}")
