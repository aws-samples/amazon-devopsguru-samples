#!/usr/local/python/3.3.2/bin/python3.3
#script-version: 1

import requests

url = 'https://awyewo5ib8.execute-api.ap-south-1.amazonaws.com/prod/'

def main():

  #SEND API Requests
  while (True):
      print("\n\n  Iterating sending requests...+++++")
      response = requests.get(url)
      result = response.text
      code = response.status_code
      print (response, result, code)

if __name__ == "__main__":
    main()
