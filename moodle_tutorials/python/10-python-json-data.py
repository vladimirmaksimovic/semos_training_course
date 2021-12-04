import urllib.request
import json

def printResults(data):
  JSON = json.loads(data)

  if "title" in JSON["metadata"]:
    print(JSON["metadata"]["title"])

  count = JSON["metadata"]["count"]
  print(str(count) + " events recorded")

  for i in JSON["features"]:
    print(i["properties"]["place"])
  
  print("------------------------")

  for i in JSON["features"]:
    if i["properties"]["mag"] >= 4.0:
      print("%2.1f" % i["properties"]["mag"], i["properties"]["place"])
  
  print("-----------------------\n")

  print("Events that were felt:")

  for i  in JSON["features"]:
    feltReports = i["properties"]["felt"]
    if feltReports != None:
      if feltReports > 0:
        print("%2.1f" % i["properties"]["mag"], i["properties"]["place"],
        " reported " + str(feltReports) + " times")

def main():
  # define a variable to hold the source URL
  urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

  # open the URL and read the data
  webUrl = urllib.request.urlopen(urlData)
  print("result code: " + str(webUrl.getcode()))   # result code: 200
  
  if (webUrl.getcode() == 200):
    data = webUrl.read()
    printResults(data)
  else:
    print("Error")

  


if __name__ == "__main__":
  main()