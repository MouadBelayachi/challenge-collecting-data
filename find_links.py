from selenium import webdriver


driver = webdriver.Chrome()


for page in range(1,334):
    
    url = "https://www.immoweb.be/en/search/house-and-apartment/for-sale?countries=BE&page=" + str(page) + "&orderBy=most_expensive"

    driver.get(url)
    
    elems = driver.find_elements_by_xpath("//a[@href]")

    for elem in elems:
        
        link = str(elem.get_attribute("href"))
        
        if 'searchId' in link:
            with open('links.txt','a') as f:
                f.write(link)
                f.write('\n')