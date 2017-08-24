import json
import subprocess
import click
import requests
import Nimam_Chasa

params = (
    ('appId', '*******'),
    ('appKey', '**********'),
)

r = requests.get('https://api.flightstats.com/flex/flightstatus/rest/v2/json/flight/status/931017258', params=params)


jsonDict = json.loads(r.text)

delaysDict = jsonDict.get('flightStatus').get('delays')
actualRunwayDepartureDict = jsonDict.get('flightStatus').get('operationalTimes').get('actualRunwayDeparture')
estimatedRunwayArrivalDict = jsonDict.get('flightStatus').get('operationalTimes').get('estimatedRunwayArrival')


print('Delays:')
for y in delaysDict:
    print('\t', y, ':', delaysDict[y])
print('----------------------------')
print('ActualRunwayDeparture:')
for y in actualRunwayDepartureDict:
    print('\t', y, ':', actualRunwayDepartureDict[y])
print('----------------------------')
print('EstimatedRunwayArrival:')
for y in estimatedRunwayArrivalDict:
    print('\t', y, ':', estimatedRunwayArrivalDict[y])



#Ask User if he wants to automatically download flight data for today?
if click.confirm('Do you want to download flights data automatically?', default=True):
    subprocess.call('Nimam_Chasa.py', shell=True)


