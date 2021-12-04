""" Retrieving data from the internet """

import urllib.request

def main():
  webUrl = urllib.request.urlopen("http://www.google.com")
  print("result code: " + str(webUrl.getcode()))   # result code: 200
  data = webUrl.read()
  print(data)  # Google html code


if __name__ == "__main__":
  main()