import os
import sys
import json
import requests

from dotenv import load_dotenv 
from requests_oauthlib import OAuth1

#Loads environment variables if saved in a .env file
load_dotenv()

#Gets the keys and secrets necessary from the environment variables
#This is not neccesary and you can store the keys anyhow you want
API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")
CLIENT_TOKEN = os.getenv("CLIENT_TOKEN")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

#Uncomment these to be sure the environment variables loaded

#print("API Key", API_KEY)
#print("API Secret", API_SECRET)
#print("CLIENT_TOKEN", CLIENT_TOKEN)
#print("CLIENT_SECRET", CLIENT_SECRET)

#Sets up an Authentication instance to be used for Twitter API
auth = OAuth1(API_KEY,
	             API_SECRET,
	             CLIENT_TOKEN ,
	             CLIENT_SECRET)
url = "https://api.twitter.com/1.1/statuses/destroy"

#Loads the json file containing tweet data into an instance
with open("tweet.json") as tweet_data:
    json_file = json.load(tweet_data)

#Gets the start number if it was passed as an argument while calling the Python script
start = sys.argv[1] if len(sys.argv) > 1 else 0
start = int( start) if start.isnumeric() else 0


length = len(json_file["tweets"])
#Sets up a few common error codes from Twitter API
error_codes = {144: "No status found with that ID",
               179: "Sorry, you are not authorized to see this status",
               63: "User has been suspended",
               34: "Sorry, that page does not exist",
               32: "Could not authenticate you"
              }

def delete_tweets(start=start, end=length):
    #Opens the log file for logging records
    with open("log.txt", "a") as log:
        try:
    
           for i in range(start, end):
                id = json_file["tweets"][i]["tweet"]["id"]
                #Creates the path using the URL for deletion and the tweet ID
                path = "".join([url, f"/{id}.json"])
                
                #Makes a request to delete the tweet
                r = requests.post(path, auth=auth)
                #Checks if the response contains any errors
                if not r.ok:
                    #Loops through the errors to log them
                    for error in r.json()["errors"]:
                        #Checks if the error already exists in the error_code dictionary above
                        if error["code"] not in error_codes:
                            error_codes[error["code"]] = error["message"]
                        #Logs the error
                        log.write(f"Index {i} exited with a {error['code']}\n")
                        
                        #break
               
                #If the current index is a multiple of 50
                #it is logged so you can have an idea where it stopped in the event of an error
                if i%50==0:
                    message = f"{i} Tweets deleted out of {length-1}"
                    log.write(f"\n{message}\n\n")
                    print(message)
                        
        except Exception as e:
            log.write(f"\nERROR: program exited with {e}\n")
        finally:  
            #If everything is done, it logs the error_codes dictionary and last index
            log.write(f"error_codes = {error_codes}\n")
            log.write(f"stopped at index {i} out of {length-1}\n\n\n")
    return

delete_tweets()

#An error finding code you can uncomment out if you need
#Just make sure to comment out the function call too

#id = json_file["tweets"][start]["tweet"]["id"]
#path = "".join([url, f"/{id}.json"])
#r = requests.post(path, auth=auth)
#print(r.json())
