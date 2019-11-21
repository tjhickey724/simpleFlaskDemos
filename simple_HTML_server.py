"""
  simple_HTTP_server is a webserver sending HTML to the browser
  and using forms and URL parameters to get data sent back
"""
from flask import Flask, request
app = Flask(__name__)

@app.route('/')
@app.route('/main')
def main():
    """ this returns a simple HTML page when the user visits / or /main """
    page1 = """
     <html>
      <head>
        <title>Hello!</title>
      </head>
      <body>
       <h1>Hello World</h1>
       <ul>
         <li>
          <a href="/whoareyou">About</a>
         </li>
         <li>
          <a href="/calculate">Calculator</a>
         </li>
       </ul>
      </body>
     </html>
    """
    return page1

@app.route('/whoareyou')
def whoareyou():
    """ this shows how to define a new route, e.g. /whoareyou """
    return 'I am Groot'

@app.route('/greeting/<name>')
def greeting(name):
    """ this shows how to pass a value (name) in through the URL """
    return 'How are you, '+name

@app.route('/calculate',methods=['GET','POST'])
def calculate():
    """ this shows how to use HTML forms to send data (x) to the server """
    page2 = """
    <form method="post" action="calculate">
      x <input type="text" name="x" placeholder="enter a number"> <br>
      <input type="submit">
      </form>
    """
    # the first time you visit a page request.method is 'GET'
    # if you press on the submit button it goes to the same page
    # but request.method is 'POST' we can the get the values passed
    # in using the dictionary request.form
    # We are only sending in partial HTML here which works but isn't advised
    if request.method == 'POST':
        z = int(request.form['x'])
        return "The square of "+str(z)+" is "+str(z*z)+"<hr>"+page2
    else:
        return page2;



if __name__ == '__main__':
    app.run('0.0.0.0',port=3000)
