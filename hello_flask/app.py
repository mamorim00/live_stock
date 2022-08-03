from flask import Flask,render_template
import requests 

# create constants for the json rows
RCER = "Realtime Currency Exchange Rate"
FROM = "1. From_Currency Code"
TO = "3. To_Currency Code"
BID = "8. Bid Price"
ASK = "9. Ask Price"


app = Flask(__name__)


# create a table with the API values


@app.route('/')
def table():

    # Define table headings
    headings = ('Instrument','Bid','Ask','Spread')

    # API call

    url = "https://alpha-vantage.p.rapidapi.com/query"

    headers = {
        "X-RapidAPI-Key": "f4bd043eedmshcffae7889d07a6ap1dc41ajsn35bac9e1417f",
        "X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com"
    }

    # Array with to_currency and from_ currency values

    forex_array = [["JPY","AUD"],["AUD","USD"],["USD","EUR"],["EUR","GBP"]]

    data = [[0],[0],[0],[0]]
    # Create a list for the data addinf as the the header the combination of strings fro the forex array
    for j in range(len(forex_array)):
        data[j][0]=(forex_array[j][0]+forex_array[j][1])
    print(data)

    # Do a for loop here to get different kinds of currencies and add to the data list
    # data list structure is data[[string 1 from + string 2 to], bid, ask, absolute value(ask-bid)]

    for i in range(len(forex_array)):

        querystring = {"to_currency":forex_array[i][0],"function":"CURRENCY_EXCHANGE_RATE","from_currency":forex_array[i][1]}
        response = requests.request("GET", url, headers=headers, params=querystring)
        jsonResponse = response.json()
        # add the bid
        data[i].append(jsonResponse[RCER][BID])
        # add the ask
        data[i].append(jsonResponse[RCER][ASK])
        #add the spread
        data[i].append("%.2f" % (abs((float(jsonResponse[RCER][BID])-float(jsonResponse[RCER][ASK])))))



    # make the data a tuple 
    data = tuple((map(tuple, data)))

    print(data)
    return render_template("table_forex.html", headings=headings, data=data)


@app.route('/table_crypto')
def table_forex():

    # Define table headings
    headings = ('Instrument','Bid','Ask','Spread')

    # API call

    url = "https://alpha-vantage.p.rapidapi.com/query"

    headers = {
        "X-RapidAPI-Key": "f4bd043eedmshcffae7889d07a6ap1dc41ajsn35bac9e1417f",
        "X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com"
    }

    # Array with to_currency and from_ currency values

    crypto_array = [["USD","BTC"],["USD","ADA"],["USD","ETH"],["USD","USDT"]]

    data = [[0],[0],[0],[0]]
    # Create a list for the data addinf as the the header the combination of strings fro the forex array
    # For crypto we only want the first and we will want the name of the coin from USD
    for j in range(len(crypto_array)):
        data[j][0]=(crypto_array[j][1])
    print(data)

    # Do a for loop here to get different kinds of currencies and add to the data list
    # data list structure is data[[string 1 from + string 2 to], bid, ask, absolute value(ask-bid)]

    for i in range(len(crypto_array)):

        querystring = {"to_currency":crypto_array[i][0],"function":"CURRENCY_EXCHANGE_RATE","from_currency":crypto_array[i][1]}
        response = requests.request("GET", url, headers=headers, params=querystring)
        jsonResponse = response.json()
        # add the bid
        data[i].append(jsonResponse[RCER][BID])
        # add the ask
        data[i].append(jsonResponse[RCER][ASK])
        #add the spread
        data[i].append("%.2f" % (abs((float(jsonResponse[RCER][BID])-float(jsonResponse[RCER][ASK])))))


    # make the data a tuple 
    data = tuple((map(tuple, data)))

    print(data)
    return render_template("table_crypto.html", headings=headings, data=data)





if __name__ == '__main__':
    app.run(debug=True)


