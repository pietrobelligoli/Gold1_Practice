def get_prices():
  import requests

  symbol = 'XAU,XAG,XPD,XPT,XRH'
  base_currency = 'EUR'
  endpoint = 'latest'
  access_key = 'o65ww2g1zd18fqm7euy9h2at766a9amft1r6srflwfle1gqu6lx029fshbfu'

  resp = requests.get('https://metals-api.com/api/'+endpoint+'?access_key='+access_key+'&base='+base_currency+'&symbols='+symbol)
  s = resp.json()['success']
  rates=resp.json()['rates']

  oz=28.3495
  
  conversion={'XAU' : 'Gold',
              'XAG' : 'Silver',
              'XPD' : 'Palladium',
              'XPT' : 'Platinum',
              'XRH' : 'Rhodium'}

  prices={}
  
  for key in rates.keys():
    prices[conversion[key]]=rates[key]/oz
  
  return(s,prices)