from bs4 import BeautifulSoup
import requests
import sys

def export_elements():
    # input: url
    # output: list of HTML elements in the web page
    #         list of the repitition of the elements.
    # getting website data
    try:
        url=input("input url and then a space: ")
        #connect website
        response = requests.get(url)


        soup = BeautifulSoup(response.text, "html.parser")

        # print(soup.get_text)#does it work?
        tag_names = []
        [tag_names.append(tag.name) for tag in soup.findAll()]

        # getting a tidy table
        # count how many times each element is in page
        unique = list(set(tag_names))
        tag_times = []
        for tag in unique:
            tag_times.append(tag_names.count(tag))
        return unique,tag_times

    except requests.exceptions.RequestException as e :
        print(e)
        sys.exit()
