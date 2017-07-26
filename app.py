from flask import Flask, render_template, request, redirect
from bokeh.plotting import figure, output_file, show
from bokeh.embed import components 
import requests, json, datetime, calendar, pandas as pd
import bokeh
app = Flask(__name__)

localTesting = False
#Quandl API Url
QAPI1 = "https://www.quandl.com/api/v3/datasets/WIKI/"
QAPI2 = ".json?column_index=4&end_date="
QAPI3 = "&start_date="
QAPI4 = "?api_key=s5LSSVBym4s5JzhtWNwh"

@app.route('/')
def main():
 	return redirect('/index')

@app.route('/index')
def index():
 	return render_template('index.html', bokehVersion = bokeh.__version__)

@app.route('/', methods=['POST'])
def ticker_form_post():
    text = request.form['ticker_text']
    processed_text = text.upper()
    
    end_date = datetime.date.today()
    month = end_date.month - 1
    if month is 0:
    	month = 12
    year = int(end_date.year - 1 / 12)
    day = min(end_date.day,calendar.monthrange(year,month)[1])
    start_date = datetime.date(year,month,day)
    request_string = QAPI1 + processed_text + QAPI2 + end_date.strftime("%Y-%m-%d") + QAPI3 + start_date.strftime("%Y-%m-%d") + QAPI4

    r = requests.get(request_string)
    stock_dict = json.loads(r.text) #This makes a dictionary 
    df = pd.DataFrame(stock_dict["dataset"]["data"])
    #convert strings to datetimes
    datetimes = [ datetime.datetime.strptime(x, "%Y-%m-%d") for x in df.loc[:,0].tolist() ]

    # output to static HTML file
    output_file("graph.html")
	# create a new plot with a title and axis labels
    p = figure(title="End of Day Prices, Via Quandl", x_axis_label='Date', y_axis_label='USD', x_axis_type="datetime")
	# add a line renderer with legend and line thickness
    p.line(datetimes, df.loc[:,1].tolist(), legend=processed_text, line_width=2)
    p.legend.location = "top_left"
  
    script, div = components(p)

    return render_template('graph.html', script=script, div=div)

if __name__ == '__main__':
    if localTesting:
    	app.run(host='0.0.0.0')
    else:
        #Port for deployment on Heroku
    	app.run(port=33507, debug=True) 
	
