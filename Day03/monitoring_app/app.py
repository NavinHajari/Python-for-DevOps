from flask import Flask
from flask import Response

app = Flask(__name__)
@app.route("/")

def hello():
    return Response({"Server is up & running"})

if __name__=='__main__':
    print("This will run only if I execute app.py")
    app.run()

