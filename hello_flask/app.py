from flask import Flask,render_template
import requests 


app = Flask(__name__)

# Define table elements

headings = ('Bid','Ask','Spread')
data = (
    ("lala","lala","alla"),
    ("test","test","yo")
    )

# API call


url = "https://alpha-vantage.p.rapidapi.com/query"

# Array with to_currency and from_ currency values
forex_array = [["JPY"]]

# Do a for loop here to get different kinds of cirrencies

JPY = "JPY"
querystring = {"to_currency":to_currency,"function":"CURRENCY_EXCHANGE_RATE","from_currency":"USD"}

headers = {
	"X-RapidAPI-Key": "f4bd043eedmshcffae7889d07a6ap1dc41ajsn35bac9e1417f",
	"X-RapidAPI-Host": "alpha-vantage.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)
jsonResponse = response.json()
print(response.text)
print(jsonResponse["Realtime Currency Exchange Rate"]["8. Bid Price"])


# create a table with the API values


@app.route('/')
def index():
    return jsonResponse["Realtime Currency Exchange Rate"]["8. Bid Price"]
#def table():
    #return render_template("table.html", headings=headings, data=data)



    


# Do the same for the crypto one. 
# TO DO  
# 1) make a table with one row and one type work
# 2) Remember the last column is the subtraction
# 3) add more rows using the for loop
# #) add the crypto