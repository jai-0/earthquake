import flask
from flask import Flask, render_template, request,redirect
import tweepy
from getmap import *
import getmap
import os
import random
app = Flask(__name__)
tomtomapi_key=os.getenv("tomtomapi_key")
consumer_key = os.getenv("consumer_key")
consumer_secret = os.getenv("consumer_secret")
access_token = os.getenv("access_token")
access_token_secret = os.getenv("access_token_secret")

def authenticate_api():
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
        auth.set_access_token(access_token, access_token_secret)
        return tweepy.API(auth)
    except Exception as error:
        print(f"An error occurred when attempting to authenticate with the twitter API. reason: {error}")

@app.route('/')
def index():
    return render_template('index.html') 


@app.route('/error', methods=['POST'])
def getvalue():
    api = authenticate_api()
    
    startDate = request.form['theStartDate']
    endDate = request.form['theEndDate']

    Magnitude = request.form['magnitude']

    City = request.form['city']
    cwd = os.getcwd()
    try:
      getMap(City,tomtomapi_key)
    except:
      return render_template('error.html')
    
    media = api.media_upload(f"{cwd}/tempimg.png")

    
    tweet="Hey, this is Sakardharan with an earthquake forecast. I predict that from %s till %s an earthquake of magnitude %s can occur at %s (%s , %s). These are just predictions, but, prevention is better than cure :D " % (startDate,endDate, Magnitude,City,getmap.lati,getmap.long)
    
    tweet = api.update_status(status=tweet, media_ids=[media.media_id]) 
  
      
      #sakardharan is just a random name :D
    print('tweet has been tweeted')
    tweetId=tweet.id_str
    
    return redirect(f"https://twitter.com/edent/status/{tweetId}")  
#initial checkpoints:
#ask for date
#ask for location
#ask for magnitude
#have a paragraph ready


if __name__ == '__main__':
    app.run( # Starts the site
		host='0.0.0.0',  # EStablishes the host, required for repl to detect the site
		port=random.randint(2000, 9000)  # Randomly select the port the machine hosts on.
   
	)
    
