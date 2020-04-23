from parameters import Original_url as url
from get_data import get_data
from export_elements import export_elements
from compare import compare

def main():
#purpose: a progrem for tests.
#checks if input HTML tags from the same website is equal to the tags saved in SQL SERVER DB
#written by: Shir Rabi, April 2020
#input: url
#output: comparision between input website Html elements to those who supposed to be
    db_data=get_data()
    current_data_tags,current_data_times=export_elements()
    compare(current_data_times, current_data_tags, db_data)

if __name__=='__main__':
    main()