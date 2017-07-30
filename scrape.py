import requests
import re
from bs4 import BeautifulSoup
import pprint
import urllib
import csv
pp = pprint.PrettyPrinter(indent=4)

#testlink = "https://www.beehive.govt.nz/advanced_search?filters=type%3Arelease"
testlink = "https://fyi.org.nz/list/successful"

def scrape_fyi(url):
    #setup

    with open("output.csv","a") as out:
        csvwriter = csv.writer(out)

        for x in range(20):
            int = x + 1
            newurl = url + "?page=" + str(int)
            page = requests.get(newurl)
            soup = BeautifulSoup(page.content, 'html.parser')

            #Get each piece of data
            #soup2 = soup.find("div", class_="request_listing").find("span", class_="head").get_text()
            # soup2 = soup.find("div", class_="request_listing")
            # soup3 = soup2.find("span", class_="head")
            # for link in soup3.find_all('a'):
            #     print(link.get('href'))

            all_requests = soup.find_all("div", class_="request_listing")
            for req in all_requests:
                head = req.find("span", class_="head")
                for link in head.find_all('a'):
                    #print(link.get('href'))

                    end = link.get('href')
                    new_link = 'https://fyi.org.nz' + end

                    data = get_data(new_link)

                    text = data.find_all("div", class_="correspondence_text")

                    towrite = []

                    for item in text:

                        for subs in item:
                            if subs.name == 'div':
                                subs.clear()

                        html = item.get_text(strip=True)
                        #print(sum([len(i) for i in [html]]))
                        if sum([len(i) for i in [html]]) <= 250:
                            towrite.append(",".join([html]))

                        break #quick hack so we only look at first piece of correspondence

                    if len(towrite) != 0:
                        nl = []
                        nl.append(towrite[0])

                        print(towrite) #keep track of progress :)

                        nl.append(new_link)



                        csvwriter.writerow(nl)




                        # for i in range(0, len(html)):
                        #     try:
                        #         out.write(html[i])
                        #     except Exception:
                        #         1+1
            #
            # first_request = soup.find("div", class_="request_listing")
            # head = first_request.find("span", class_="head")
            # for link in head.find_all('a'):
            #         #print(link.get('href'))
            #
            #         end = link.get('href')
            #         new_link = 'https://fyi.org.nz' + end
            #
            #         data = get_data(new_link)
            #
            #         #text = data.find("div", class_="correspondence_txt")
            #         #print(text)
            #         #print(data)
            #
            #         text = data.find_all("div", class_="correspondence_text")
            #
            #         for item in text:
            #             for subs in item:
            #
            #                 if subs.name == 'div':
            #
            #                     print("GOT HERE")
            #                     subs.clear()
            #
            #             html = item.get_text()
            #             with open("output.txt","a") as out:
            #                 for i in range(0, len(html)):
            #                     try:
            #                         out.write(html[i])
            #                     except Exception:
            #                         1+1

    #print soup.find("div", class_="your-price").find("span", class_="currency").text
        #print (soup2)
        #print (soup3)

def get_data(link):
    page = urllib.request.urlopen(link)
    soup = BeautifulSoup(page, 'html.parser')
    return soup


scrape_fyi(testlink)
