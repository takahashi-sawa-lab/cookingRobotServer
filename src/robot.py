import sys
import time
import argparse
import json
import requests

parser = argparse.ArgumentParser()
parser.add_argument('-t', '--test', action='store_true')
args = parser.parse_args()

orderOutput_url = "https://cookingrobotserver.herokuapps.com/order/output"
orderOutput_testurl = "http://localhost:5000/order/output"

def main():
    try:
        if args.test:
            response = requests.get(orderOutput_testurl)
        else:
            response = requests.get(orderOutput_url)
    except Exception as e:
        print(e)
        sys.exit(1)



if __name__ == '__main__':
    main()
