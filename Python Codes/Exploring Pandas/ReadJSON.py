import pandas as pd

#big data sets are often stored or extracted as JSON
#JSON is plain text but has the format of an object and is well known in the world of programming including pandas

#load the JSON file into a Dataframe:
data=pd.read_json('data.json')
print("\n")
print(data.to_string())
print("\n")

#Dictionary as JSON
'''
JASON = Python Dictionary
JSON object have the same format as python dictionaries
'''

#load a python dictionary into dataframe;
data1 = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409.1,
    "1":479.0,
    "2":340.0,
    "3":282.4,
    "4":406.0,
    "5":300.5
  }
}

df = pd.DataFrame(data1)

print(df) 
