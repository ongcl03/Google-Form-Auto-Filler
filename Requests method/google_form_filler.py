import requests
import json

def fill(url, form_data):
    print(requests.post(url, data = form_data))


url = "https://docs.google.com/forms/u/0/d/e/1FAIpQLScvsr_4LZFcxFlAVD030_sISeaV5I5loRGCBuxuipdDgVsNUw/formResponse"
form_data = {
    # "entry.1813953896": "Option 2",
    "entry.1338845028" : "hello", 
    "entry.1353047505" : "testing",
    "pageHistory" : "0,1"                                           # need to add page history when google form has multiple pages
    }

fill(url, form_data)