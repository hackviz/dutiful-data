import requests
import re
from bs4 import BeautifulSoup
import pprint
import urllib
import csv
pp = pprint.PrettyPrinter(indent=4)

baselink = "https://fyi.org.nz/list/successful"

def scrape_fyi(url):

    #open the csv writer outside the loops
    with open("output.csv","a") as out:
        csvwriter = csv.writer(out)

        #iterate through the current limit of 20 pages of search results
        for x in range(20):
            int = x + 1
            newurl = url + "?page=" + str(int)
            page = requests.get(newurl)
            soup = BeautifulSoup(page.content, 'html.parser')

            #grab all the request listings on the search page
            all_requests = soup.find_all("div", class_="request_listing")

            #from the request listings, grab the URL of the link to the individual request page
            for req in all_requests:
                head = req.find("span", class_="head")
                for link in head.find_all('a'):

                    #concatenate the URLs
                    end = link.get('href')
                    new_link = 'https://fyi.org.nz' + end

                    data = get_data(new_link)

                    text = data.find_all("div", class_="correspondence_text")

                    towrite = []

                    for item in text:

                        #this clears the "attachments" div in the correspondence_text
                        for subs in item:
                            if subs.name == 'div':
                                subs.clear()
                        #strip out newlines etc
                        html = item.get_text(strip=True)
                        #method to limit results to queries under 250 characters (for postcard suitability)
                        if sum([len(i) for i in [html]]) <= 250:
                            towrite.append(",".join([html]))

                        break #quick hack so we only look at first piece of correspondence - original functionality had entire chain

                    #don't write empty rows
                    if len(towrite) != 0:
                        nl = []
                        nl.append(towrite[0])

                        print(towrite) #keep track of progress on the command line :)

                        nl.append(new_link)

                        csvwriter.writerow(nl)


#method to grab data from a subpage link via BeautifulSoup
def get_data(link):
    page = urllib.request.urlopen(link)
    soup = BeautifulSoup(page, 'html.parser')
    return soup

#run things
scrape_fyi(baselink)
