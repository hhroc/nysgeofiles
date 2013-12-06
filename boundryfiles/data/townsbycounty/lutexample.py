import simplejson

with open("countylut.json","r") as f:
    data = f.read()
    counties = simplejson.loads(data)
    
    for county in counties:
        countyname = county['countyname']
        countycode = county['countycode']
        statecode = county['statecode']

