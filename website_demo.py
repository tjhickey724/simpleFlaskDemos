"""
  website_demo shows how to use templates to generate HTML
  from data selected/generated from user-supplied information
"""

from flask import Flask, render_template, request
app = Flask(__name__)

lines = open('data/romeo_and_juliet.txt').read().splitlines()

def factors(n):
	""" returns the list of divisors of an integer n """
	return [x for x in range(1,n+1) if n%x==0]

@app.route('/')
def main():
	""" renders the main page """
	return render_template("main.html")

@app.route('/b')
def mainBootstrap():
	""" show how to generate a bootstrap-styled page """
	return render_template("mainbootstrap.html")

@app.route('/fancy')
def fancymain():
	""" shows how to use template layouts to create styled pages """
	return render_template("fancymain.html")

@app.route('/bio')
def bio():
	""" generates a bio page with links and images """
	return render_template('bio.html')

@app.route('/randj/<word>')
def randj(word):
	""" returns all lines of Romeo and Juliet containing the given word """
	the_lines = [line for line in lines if word in line]
	return render_template('randj.html',word=word,the_lines=the_lines)

@app.route('/factors/<n>')
def factors_display(n):
	""" displays all divisors of n in a list """
	factors_list = factors(int(n))
	return render_template(
		"factors.html",
		number=n,
		factors=factors_list
	)

@app.route('/calculate',methods=['GET','POST'])
def calculate():
	""" gets n using a form and prints the divisors with a template """
	if request.method == 'POST':
		n = request.form['number']
		factors_list = factors(int(n))
		return render_template("calculate.html",number=n,factors=factors_list)
	else:
		return render_template("calculate.html",number=1,factors=[1])


if __name__ == '__main__':
    app.run('0.0.0.0',port=3000)
