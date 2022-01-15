from flask import Flask, render_template, url_for ,request,redirect, Response

from flaskext.mysql import MySQL

import RPi.GPIO as GPIO

from camera_pi import Camera

import time
import os
app = Flask(__name__)


GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)



ledRed = 13

buzzer= 19

senPIR = 17

ledGreen= 26

senPIRSts = 0

ledRedSts = 0

buzzerSts = 0

ledGreenSts = 0


GPIO.setup(senPIR, GPIO.IN)

GPIO.setup(ledRed, GPIO.OUT)

GPIO.setup(buzzer,GPIO.OUT)

GPIO.setup(ledGreen, GPIO.OUT)

GPIO.output(ledRed, GPIO.LOW)

GPIO.output(buzzer, GPIO.LOW)

GPIO.output(ledGreen, GPIO.LOW)


mysql=MySQL()

app.config["MYSQL_DATABASE_USER"]='Your ID'

app.config["MYSQL_DATABASE_PASSWORD"]='Your Psswd'

app.config["MYSQL_DATABASE_DB"]='Your database'

app.config["MYSQL_DATABASE_HOST"]='localhost'

mysql.init_app(app)


@app.route("/login",methods=['GET','POST'])

def login():

    senPIRSts = GPIO.input(senPIR)

#    	os.system('python bot.py')
    ledRedSts = GPIO.input(ledRed)

    buzzerSts = GPIO.input(buzzer)

    ledGreenSts = GPIO.input(buzzer)

    templateData = {'ledRed': ledRedSts,

                    'senPIR': senPIRSts,

                    'buzzer': buzzerSts,

                    'ledGreen': ledGreenSts}

    if request.method=='POST':

        username=request.form['username']

        password=request.form['password']

        con=mysql.connect()

        cur=con.cursor()

        cur.execute("SELECT * FROM `register` WHERE `username` = '"+username+"' and `password` = '"+password+"'")

        data=cur.fetchone()

        if data[2]==username and data[6]==password:

            return render_template('index.html', **templateData)

    else:

        return render_template('login.html')





@app.route('/<deviceName>/<action>')

def do(deviceName, action):


    if deviceName == "ledRed":

        actuator = ledRed

    if deviceName == "buzzer":

        actuator = buzzer

    if deviceName == "ledGreen":

        actuator = ledGreen

    if action == "on":

        GPIO.output(actuator, GPIO.HIGH)

    if action == "off":

        GPIO.output(actuator, GPIO.LOW)



    senPIRSts = GPIO.input(senPIR)

    ledRedSts = GPIO.input(ledRed)

    buzzerSts = GPIO.input(buzzer)

    ledGreenSts = GPIO.input(ledGreen)




    templateData = { 'ledRed' : ledRedSts,

                     'senPIR': senPIRSts,

    'buzzer' : buzzerSts,

    'ledGreen' : ledGreenSts }



    return render_template('index.html', **templateData )







@app.route('/camera')

def cam():

    """Video streaming home page."""

    timeNow = time.asctime(time.localtime(time.time()))

    templateData = {

        'time': timeNow

    }



    return render_template('camera.html', **templateData)











def gen(camera):

    """Video streaming generator function."""



    while True:

        frame = camera.get_frame()

        yield (b'--frame\r\n'

               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')











@app.route('/video_feed')

def video_feed():



    """Video streaming route. Put this in the src attribute of an img tag."""



    return Response(gen(Camera()),



                    mimetype='multipart/x-mixed-replace; boundary=frame')






if __name__ == "__main__":

    app.run(host = '0.0.0.0', debug=True,threaded=True)





