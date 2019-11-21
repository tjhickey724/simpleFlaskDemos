"""
real_estate_demo.py generates a web-based interface to a dataset.
It reads the data using the csv (comma separated values) package
and stores it in a list of dictionaries. It allows the user to
search for homes sold in 1 week in California by zip or price
"""

import csv
from flask import Flask, render_template, request
app = Flask(__name__)


sales = list(csv.DictReader(open('data/RE.csv')))
zips = list({x['zip'] for x in sales})


def convert_to_list(dict):
	""" creates a list of the key-value pairs in the dictionary """
	return [[k,dict[k]] for k in dict];


@app.route('/',methods=['GET','POST'])
def main():
	""" creates the main page """
	return render_template("re_main.html")



@app.route('/byzip',methods=['GET','POST'])
def byzip():
	""" generates the page with houses by zipcode """
	if request.method == 'POST':
		n = request.form['zip']
		house_list = [convert_to_list(x) for x in sales if x['zip']==n]
		return render_template("zip.html",zip=n,zips=zips,house_list=house_list)
	else:
		return render_template("zip.html",zip='00000',zips=zips,house_list=[])

@app.route('/byprice',methods=['GET','POST'])
def byprice():
	""" generates the page with houses by price """
	if request.method == 'POST':
		low = float(request.form['low'])
		high = float(request.form['high'])
		house_list = [convert_to_list(x) for x in sales if low<=float(x['price'])<=high]
		return render_template("price.html",low=low,high=high,house_list=house_list)
	else:
		return render_template("price.html",low=100000,high=105000,house_list=[])


if __name__ == '__main__':
    app.run('0.0.0.0',port=3000)
