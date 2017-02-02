# temperlog
temperature logging

Setup temperature logging via USB temperature sensor. 
Send data to Graphite and display locally via google draw charts

Raw data file collected by the sensor has a format:
    2017/01/27 15:35:01 Temperature 106.81F 41.56C
    2017/01/27 15:40:01 Temperature 105.12F 40.62C

Json data file has a format:

{
"cols": [
  {"id": "timestamp", "label": "DateTime",  "type": "datetime"},
  {"id": "tempF",     "label": "degrees F", "type": "number"},
  {"id": "tempC",     "label": "degrees C", "type": "number"}
],
"rows": [
{"c":[{"v": "Date(2017,0,27,15,35,1)"}, {"v": 106.81}, {"v": 41.56}]},
{"c":[{"v": "Date(2017,0,27,15,40,1)"}, {"v": 105.12}, {"v": 40.62}]},
{"c":[{"v": "Date(2017,0,27,15,45,1)"}, {"v": 105.80}, {"v": 41.00}]},
...
}
