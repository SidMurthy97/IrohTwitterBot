import tweepy
import webbrowser
import os 
import pickle 


def getQuote():
    # first line of quotes.txt is an iterator and points to the next untweeted quote 
    filepath = 'quotes.txt'
    with open(filepath,encoding="utf8") as fp:
        quotes = fp.readlines()
        index = int(quotes[0]) #get index 
        quote = quotes[index] #get quote 
    
    newIndex = index+1 #increment index 
    if newIndex > 48:
        newIndex = 1
    
    quotes[0] = str(newIndex) + "\n"

    with open("quotes.txt", "w",encoding="utf8") as f:
        f.writelines(quotes) #overwrite file with new incremented indx 


    return quote

def first_time_authenciation():

    auth = tweepy.OAuthHandler(os.environ['TWITTER_API_KEY'],os.environ['TWITTER_SECRET_KEY'],'oob')
    
    try:
        redirect_url = auth.get_authorization_url()
    except tweepy.TweepError:
        print('Error! Failed to get request token.')
    
    webbrowser.open(redirect_url)
    user_pin_input = input("enter authorisation pin: ")

    auth.get_access_token(user_pin_input)

    with open('apiObject.txt','wb') as file:
        pickle.dump(auth,file)

def load_authenciation():
 
    with open('apiObject.txt','rb') as file:
        auth = pickle.load(file)
    
    api = tweepy.API(auth)

    return api

def tweet(quote,api):
    tweet = quote + "#avatarthelastairbender #ATLA"
    api.update_status(tweet)

if __name__ == "__main__":

    quote = getQuote()
    first_time_authenciation()
    api = load_authenciation()
    tweet(quote,api)
