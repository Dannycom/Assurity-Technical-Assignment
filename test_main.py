import requests
import json

resp = requests.get("https://api.tmsandbox.co.nz/v1/Categories/6328/Details.json?catalogue=false") #get request from API
json_resp = resp.json() #formatting into json format

#test for Name
def test_name():
    assert json_resp['Name'] == 'Badges'

#test for CanRelist
def test_canrelist():
    assert json_resp['CanRelist'] is True

#test for Promotions element
def test_promo():
    for ele in json_resp["Promotions"]:
        if ele["Name"] == "Feature":
            assert ele["Description"] == "Better position in category"
