import tweepy
import webbrowser
import os 

def getQuote():

    filepath = 'quotes.txt'
    with open(filepath,encoding="utf8") as fp:
        quotes = fp.readlines()
        index = int(quotes[0])
        quote = quotes[index]
    
    newIndex = index+1
    if newIndex > 48:
        newIndex = 1
    
    quotes[0] = str(newIndex) + "\n"

    with open("quotes.txt", "w",encoding="utf8") as f:
        f.writelines(quotes)


    return quote

def Twitter_authenciate():
    auth = tweepy.OAuthHandler(os.environ['TWITTER_API_KEY'],os.environ['TWITTER_SECRET_KEY'],'oob')
    
    try:
        redirect_url = auth.get_authorization_url()
    except tweepy.TweepError:
        print('Error! Failed to get request token.')
    
    webbrowser.open(redirect_url)
    user_pin_input = input("enter authorisation pin: ")

    auth.get_access_token(user_pin_input)
    api = tweepy.API(auth)

    return api

def tweet(quote,api):
    tweet = quote + "#avatarthelastairbender #irohquotes"
    api.update_status(tweet)

if __name__ == "__main__":

    quote = getQuote()
    api = Twitter_authenciate()
    tweet(quote,api)