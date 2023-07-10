from flask import Flask
from flask import request
import array
import serial
import datetime
import time


# Create a Flask application
app = Flask(__name__)

ser = serial.Serial('/dev/ttyUSB0', 19200)


# Define a route and its corresponding view function
@app.route('/Person/Log',methods = ['POST'])
def hello():
    data = request.json
    if(data["person_name"] != "" and int(time.time()*1000) <= data["timestamp"] + 1000000):
        datetime_obj = datetime.datetime.fromtimestamp(int(data["timestamp"]/1000))
        datetime_str = datetime_obj.strftime('%Y-%m-%d %H:%M:%S')
        ser.write(datetime_str.encode("utf-8"))
        ser.write([10])
        print(data["person_name"])
        ser.write(data["person_name"].encode("utf-8"))
        ser.write([10])
        print(data["person_code"])
        ser.write(data["person_code"].encode("utf-8"))
        ser.write([10])
        ser.write("Enjoy Your Meal :)".encode("utf-8"))
        ser.write([10,10, 29, 86, 66, 1 ])
    return 'Hello, World!'

# Run the Flask application
if __name__ == '__main__':
    # Specify the server and port for the application to run on
    app.run(host='0.0.0.0', port=5000,debug=True)


