from flask import Flask, request, render_template
application = Flask(__name__)

@application.route('/')
def selectdata():
       return render_template('index.html')
if __name__ == '__main__':
    application.run(port=5001)


