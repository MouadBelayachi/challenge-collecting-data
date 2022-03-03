from selenium import webdriver

# set webdriver
driver = webdriver.Chrome()


# loop over 333 pages on immoweb
for page in range(1, 334):

    # set urls
    url = (
        "https://www.immoweb.be/en/search/house-and-apartment/for-sale?countries=BE&page="
        + str(page)
        + "&orderBy=most_expensive"
    )

    driver.get(url)

    # get links on webpage
    elems = driver.find_elements_by_xpath("//a[@href]")

    # loop over found links
    for elem in elems:

        # get href attribute of each links
        link = str(elem.get_attribute("href"))

        # make sure link leads to page on immoweb
        if "searchId" in link:
            # write string of link to text file
            with open("links.txt", "a") as f:
                f.write(link)
                f.write("\n")
