# Twitter Deleter
A simple Python script for bulk deleting tweets

## Prerequisites
- A Twitter Developer Account.
To get one, go [here](https://developer.twitter.com/en/apply-for-access).  
__Note__: it could take
up to a month before your Developer Account gets created.
- Twitter Archive. If you're planning on deleting more than your last 3,200 tweets,
then you'll need your account's archive. Learn how to get it [here](https://help.twitter.com/en/managing-your-account/how-to-download-your-twitter-archive).   
__Note__: it takes a day to get the archive ready, and it's a really big zip file containing all your Twitter data.

## Getting Started
- Now that you have both, all you have to do is create a Twitter API app
[here](https://developer.twitter.com/en/apps) if you don't already have one. 
- After that, create the neccesary access tokens and client tokens in your Developer portal. 
- Unzip your Twitter Archive, go to `data` and open `tweets.js`. It is a JavaScript file and can't be read if you're using
Python, you'll have to change the `tweets` variable to json by surrounding it with __double__ quotes, changing the equals
sign to a colon and enclosing the entire file in curly braces. 
```javascript
// Before
tweets = [{...allTheTweets}] // The array contains all tweet objects

// After
{"tweets" : [{...allTheTweets}]}
// Then rename the file to tweets.json
```
- Install `requests`, `requests-oauthlib` and `python-dotenv` with pip.  
`pip install requests requests-oauthlib`
## Using the Python Script
Everything is set, now place `tweets.json` in the same folder as the Python Script,
and call it with  
`python deleter` for Windows  
or  
`python3 deleter` for Linux/Mac.  

The script creates a `log.txt` file that helps you note what index you stopped at, in a case
where the script crashes.  

You can now look up what error caused it to crash, and use the last known index as the starting point the next time you're calling the script
like so  
`python deleter <start number>`  
or  
`python3 deleter <start number>`  
where `start number` is the last known index.  
## Debugging
It is very unlikely that the program will crash due to any error unless things aren't setup right
but in the event that it does, check the log file for the last line, it should contain an error, but if
it doesn't, you can use the little piece of code at the end of the file to test for specific indexes around the last
recorded index in `log.txt`, when you find the index giving the unknown error, you can skip it and use the next index as the start number.
If the last recorded index was, say 1250, you can edit the code to log in multiples of 5 rather than 50 to narrow down the error-catching index.  

When you're sure of the index giving the errors, i.e 1262, you skip it and call script with the next index like so:  
`python deleter 1263`  
or
`python3 deleter 1263`  
And everything should work fine.  

Contact me on [Twitter](https://twitter.com/redDevv?s=09) if anything is unclear.  
Thank you.
