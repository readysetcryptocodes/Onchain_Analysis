#Module to obtain coinmetrics API v2 dataset
#Credit to CryptoManiac for getting the ball rolling with initial API code.

import requests
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd

def getSupportedAssets():
    response = requests.get('https://community-api.coinmetrics.io/v2/assets')
    return response.json()['assets']

def getAvalMetrics():
    reqtosend = 'https://community-api.coinmetrics.io/v2/metrics'
    response = requests.get(reqtosend)
    return response.json()['metrics']
    
def getAssetMetricForTimeRange(asset, metrics, startdate, enddate):
    reqtosend = 'https://community-api.coinmetrics.io/v2/assets/'
    reqtosend += asset
    reqtosend += '/metricdata'
    reqtosend += '?metrics=' + metrics
    reqtosend += '&start=' + startdate
    reqtosend += '&end=' + enddate
    response = requests.get(reqtosend)
    return response.json()['metricData']['series']
	
def getAssetMetricFromStartDate(asset, metrics, startdate):
    reqtosend = 'https://community-api.coinmetrics.io/v2/assets/'
    reqtosend += asset
    reqtosend += '/metricdata'
    reqtosend += '?metrics=' + metrics
    reqtosend += '&start=' + startdate    
    response = requests.get(reqtosend)
    return response.json()['metricData']['series']
    
def getAssetMetric(asset, metrics):
    reqtosend = 'https://community-api.coinmetrics.io/v2/assets/'
    reqtosend += asset
    reqtosend += '/metricdata'
    reqtosend += '?metrics=' + metrics
    response = requests.get(reqtosend)
    return response.json()['metricData']['series']

    

 
# print supported assets
supassets = getSupportedAssets()
print(supassets)

#print available metrics
availmetrics = getAvalMetrics()
print(availmetrics)

# print PriceUSD for BTC between 18-07-2010 and 17-08-2010
#for val in getAssetMetricForTimeRange('btc', 'CapRealUSD','20110101','20190725'):
#    print(val['time'], val['values'])

# print CapRealUSD for BTC
#for val in getAssetMetric('btc', 'CapRealUSD'):
#    print(val['time'], val['values'])
    
# print Realised price = CapRealUSD/SplyCur
CapRealUSD = getAssetMetricFromStartDate('btc', 'CapRealUSD', '20110101')
SplyCur = getAssetMetricFromStartDate('btc', 'SplyCur', '20110101')
for i in range(0,len(CapRealUSD)):  
    RealisedPrice_BTC = float(CapRealUSD[i]['values'][0])/float(SplyCur[i]['values'][0])
    #print(RealisedPrice_BTC)


def asset_array(asset):
    CapRealUSD = getAssetMetric(asset, 'CapRealUSD')
    SplyCur = getAssetMetric(asset, 'SplyCur')
    return CapRealUSD

BTC_array = asset_array('dcr')
print(BTC_array)

