from bs4 import BeautifulSoup
import requests
import json
import csv
import time
import random


# create list with urls of properties (from a text file)
links = []
with open("links_part_two_b.txt") as f:
    urls = f.readlines()

for link in urls:
    links.append(link)


# loop over all urls in list links
for url in links:

    # set timer to avoid detection
    timer = random.random() * 0.5 + 0.1
    time.sleep(timer)

    # soup to scrape data from url
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    x = soup.find("script", attrs={"type": "text/javascript"}).text.strip()[20:-1]

    # make sure data is in JSON format and can be converted to python dictionary
    try:
        data = json.loads(x)
    except:
        data = []

    # extract relevant data while making sure the keys exist
    try:
        locality = data["property"]["location"]["locality"]
    except:
        locality = None
    try:
        property_type = data["property"]["type"]
    except:
        property_type = None
    try:
        property_subtype = data["property"]["subtype"]
    except:
        property_subtype = None
    try:
        price = data["transaction"]["sale"]["price"]
    except:
        price = None
    try:
        sale_type = data["transaction"]["type"]
    except:
        sale_type = None
    try:
        bedroom_count = data["property"]["bedroomCount"]
    except:
        bedroom_count = None
    try:
        bathroom_count = data["property"]["bathroomCount"]
    except:
        bathroom_count = None
    try:
        net_Habital_surface = data["property"]["netHabitableSurface"]
    except:
        net_Habital_surface = None
    try:
        kitchen = data["property"]["kitchen"]
    except:
        kitchen = None
    try:
        furnished = data["transaction"]["sale"]["isFurnished"]
    except:
        furnished = None
    try:
        open_fire = data["property"]["fireplaceExists"]
    except:
        open_fire = None
    try:
        terrace = data["property"]["hasTerrace"]
    except:
        terrace = None
    try:
        terrace_surface = data["property"]["terraceSurface"]
    except:
        terrace_surface = None
    try:
        garden = data["property"]["hasGarden"]
    except:
        garden = None
    try:
        garden_surface = data["property"]["gardenSurface"]
    except:
        garden_surface = None
    try:
        land_surface = data["property"]["land"]["surface"]
    except:
        land_surface = None
    try:
        land_plot_surface = data["property"]["constructionPermit"][
            "totalBuildableGroundFloorSurface"
        ]
    except:
        land_plot_surface = None
    try:
        facade_count = data["property"]["building"]["facadeCount"]
    except:
        facade_count = None
    try:
        pool = data["property"]["hasSwimmingPool"]
    except:
        pool = None
    try:
        building_state = data["property"]["building"]["condition"]
    except:
        building_state = None

    # list of all extracted data
    relevant_data = [
        locality,
        property_type,
        property_subtype,
        price,
        sale_type,
        bedroom_count,
        bathroom_count,
        net_Habital_surface,
        kitchen,
        furnished,
        open_fire,
        terrace,
        terrace_surface,
        garden,
        garden_surface,
        land_surface,
        land_plot_surface,
        facade_count,
        pool,
        building_state,
    ]

    # write list as row to cvs file
    with open("result_part_two_b.csv", "a") as f:
        writer = csv.writer(f)
        writer.writerow(relevant_data)
