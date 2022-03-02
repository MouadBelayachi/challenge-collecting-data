from bs4 import BeautifulSoup
import requests
import json
import csv
import time
import random


links = []

with open('links_part_three.txt') as f:
    urls = f.readlines()
    
for link in urls:
    links.append(link)



for url in links:
    
    timer = random.random()*2+1
    time.sleep(timer)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    x = soup.find('script', attrs={'type': 'text/javascript'}).text.strip()[20:-1]
    
    try:
        data = json.loads(x)
    except:
        data = []
    
    try:
        locality = data['property']['location']['locality']
    except:
        locality = None
    try:
        property_type = data['property']['type']
    except:
        property_type = None
    try:
        property_subtype = data['property']['subtype']
    except:
        property_subtype = None
    try:
        price = data['transaction']['sale']['price']
    except:
        price = None
    try:
        sale_type = data['transaction']['type']
    except:
        sale_type = None
    try:
        bedroom_count = data['property']['bedroomCount']
    except:
        bedroom_count = None      
    try:
        bathroom_count = data['property']['bathroomCount']
    except:
        bathroom_count = None
    try:
        net_Habital_surface = data['property']['netHabitableSurface']
    except:
        net_Habital_surface = None
    try:
        kitchen = data['property']['kitchen']
    except:
        kitchen = None
    try:
        furnished = data['transaction']['sale']['isFurnished']
    except:
        furnished = None
    try:
        open_fire = data['property']['fireplaceExists']
    except:
        open_fire = None
    try:
        terrace =  data['property']['hasTerrace']
    except:
        terrace = None
    try:
        terrace_surface = data['property']['terraceSurface']
    except:
        terrace_surface = None
    try:
        garden = data['property']['hasGarden']
    except:
        garden = None
    try:
        garden_surface = data['property']['gardenSurface']
    except:
        garden_surface = None
    try:
        land_surface = data['property']['land']['surface']
    except:
        land_surface = None
    try:
        land_plot_surface = data['property']['constructionPermit']['totalBuildableGroundFloorSurface']
    except:
        land_plot_surface = None
    try:
        facade_count = data['property']['building']['facadeCount']
    except:
        facade_count = None
    try:
        pool = data['property']['hasSwimmingPool']
    except:
        pool = None
    try:
        building_state = data['property']['building']['condition']
    except:
        building_state = None
    
    relevant_data = [locality, property_type, property_subtype, price, sale_type, bedroom_count, bathroom_count, net_Habital_surface, kitchen, furnished,
                     open_fire, terrace, terrace_surface, garden, garden_surface, land_surface, land_plot_surface, facade_count, pool, building_state]
    
    with open('result_part_three.csv', 'a') as f:
        writer = csv.writer(f)
        writer.writerow(relevant_data)
    
    
    
