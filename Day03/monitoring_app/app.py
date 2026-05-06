from flask import Flask
from flask import Response
import psutil

app = Flask(__name__)

#@app.route("/")
#def hello():
#    return Response({"Server is up & running"})

@app.route("/cpu")
def monitor_cpu():
    cpu_percent = psutil.cpu_percent()
    return Response({f"The CPU utilization is {cpu_percent}%"})

if __name__=='__main__':
    print("This will run only if I execute app.py")
    app.run()

