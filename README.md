# Raspberry_pi
라즈베리파이 리포지토리

## 파이썬과 웹을 연동하여 라즈베리파이 작동하기(평가)

---
사용자의 요청에 의해 라즈베리파이 서버에 연결된 디바이스들을 제어한다.
- Led
- Speak
- sensor
---

1. 파이썬 코드
```python
from flask import Flask, request, render_template
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

ledPin = 21
pinPiezo = 13
triggerPin = 14
echoPin = 4

GPIO.setmode(GPIO.BCM)
GPIO.setup(triggerPin, GPIO.OUT)
GPIO.setup(echoPin, GPIO.IN)
GPIO.setup(pinPiezo, GPIO.OUT)
GPIO.setup(ledPin, GPIO.OUT)

Buzz = GPIO.PWM(pinPiezo, 440)
p = GPIO.PWM(ledPin, 255)

def alerm(t):
        Buzz.start(50)
        time.sleep(t)
        Buzz.stop()

@app.route('/')
def home():
        return render_template("allpack.html")

@app.route('/data', methods = ['POST'])
def data():
        data = request.form['led']
        if data =='on':
                GPIO.output(ledPin, True)
                return home()
        elif data == 'off':
                GPIO.output(ledPin, False)
                return home()
@app.route('/mod', methods = ['GET'])
def mod():
        p.start(0)
        while True:
                d = request.args.get('mod')
                duty = int(d)

                if (duty == 100):
                        p.stop()
                        return home()
                else:
                        p.ChangeDutyCycle(duty)
        return home()
@app.route('/sound', methods = ['POST'])
def sound():
        count = 0
        while count != 5:
                alerm(1)
                count = count + 1

        return home()
@app.route('/sonic', methods = ['POST'])
def sonic():
        count = 0
	res = []
        while count != 10:
                time.sleep(0.2)
                GPIO.output(triggerPin, GPIO.LOW)
                time.sleep(0.00001)
                GPIO.output(triggerPin, GPIO.HIGH)

                while GPIO.input(echoPin) == 0:
        		start = time.time()
                while GPIO.input(echoPin) == 1:
                        stop = time.time()

                rtTotime = stop - start
                distance = rtTotime * 34000 / 2
		distance = round(distance, 2)
 		res.append(distance)
                print("distance : %.2f cm" % distance)

                count = count + 1
 return render_template("allpack.html", data=res)


if __name__ == '__main__':
        app.run(host = '0.0.0.0', port='8080')
```
2. 웹 코드
```html
<!DOCTYPE html>
<html>
<head>
        <meta charset="UTF-8">
        <title> HOME IOT NETWORK </title>
</head>
<body>
        <h1> IOT allpackage </h1>
        <form action = /data method = 'post'>
                <p> 버튼 on 누르면 불 켜짐 off 누르면 불 꺼짐</p><br/>
                <input type="submit" name="led" value="on"/>
                <input type="submit" name="led" value="off"/>
        </form>
        <form action = /mod method = 'get'>
                <p> 숫자를 입력하세요 (0~99) 100을 입력하면 꺼집니다</p><br/>
                <input type="text" name="mod" value="입력"/>
        </form>
        <form action = /sound method = 'post'>
                <p> 버튼 on 누르면 소리 나옴 </p><br/>
 		<input type="submit" name="sound" value="on"/>
        </form>
        <form action = /sonic method = 'post'>
                <p> 버튼 on 누르면 초음파 탐지 </p><br/>
                <input type="submit" name="sonic" value="on"/>
        </form>
 		<h3> 초음파 탐지 값  </h3>
                {% for i in data %}
                        {{i}} cm </br>
                {% endfor %}

</body>
</html>
```
