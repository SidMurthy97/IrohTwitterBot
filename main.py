
def getQuote():

    filepath = 'quotes.txt'
    with open(filepath,encoding="utf8") as fp:
        quotes = fp.readlines()
        index = int(quotes[0])
        quote = quotes[index]
    
    newIndex = index+1
    if newIndex > 10:
        newIndex = 1
    
    quotes[0] = str(newIndex) + "\n"

    with open("quotes.txt", "w",encoding="utf8") as f:
        f.writelines(quotes)


    print(quote)

if __name__ == "__main__":

    getQuote()