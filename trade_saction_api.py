import requests, json


# https://developer.trade.gov/

# https://www.trade.gov/data-visualization/csl-search






def tradGov(name):

    url = f"https://data.trade.gov/consolidated_screening_list/v1/search?name={name}"

    hdr ={
    # Request headers
    'Cache-Control': 'no-cache',
    'subscription-key': '85e74f9c1bac45a1ad719254f9beda47',
    }

    res=requests.get(url, headers=hdr)

    return res.json()






if __name__=='__main__':

    corps=tradGov('FOZ FOR TRADING')


