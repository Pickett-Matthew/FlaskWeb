#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 22:11:15 2019

@author: matthewpickett
"""

#OANDA access key = d14bb2de2a81b1b8180ee6b13fff8e6e-0741cc9f49ea55f0538542cfeac52eb1
#account number = 101-001-11138682-001


from oandapyV20 import API
import oandapyV20.endpoints.trades as trades
import json
import oandapyV20.endpoints.pricing as pricing
import pandas as pd
from flask import Flask, render_template

app = Flask(__name__)

api = API(access_token="d14bb2de2a81b1b8180ee6b13fff8e6e-0741cc9f49ea55f0538542cfeac52eb1")
accountID = "101-001-11138682-001"

#reduce a trade by it's id
r = trades.TradesList(accountID)

#print("REQUEST:{}".format(r))

rv = api.request(r)
#print("RESPONSE:\n{}".format(json.dumps(rv, indent=2)))

#this will get pricing info

    
#specify the currency type and all the info that comes with it.
params = {"instruments": "EUR_USD"}

r = pricing.PricingInfo(accountID=accountID, params=params)
rv = api.request(r)
df = pd.DataFrame(r.response['prices'])

prices = df.loc[:, "bids"]


for value in prices:
    value[0]
    
p = value[0]


@app.route("/")
def swiper():
    return render_template("swiper.html", p=p)



if __name__ =='__main__':
    app.run(debug=True)
