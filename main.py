from flask import Flask
from wrap import mainGen
from flask import request

app = Flask(__name__)


@app.route('/')
def index():
    refcode = request.args.get('refcode')
    if refcode:
        mainGen(refcode)
        return 'Done Completed'
    else:
      return '''
      <html>
      <head>
      <title>
      Wrap Unlimited plus Generator
      </title>
      </head>

      <body>
      <form>
      <p>
      Enter the reffaral code:
      </p>
      <input name="refcode" />
      
      </form>
      </body>
      

      </html>
      ''''''
      <html>
      <head>
      </head>
      

      </html>
      '''

    # ref = mainGen(refcode)

    


app.run(host='0.0.0.0', port=81)
