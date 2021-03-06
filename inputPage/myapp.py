from flask import Flask, render_template, request
import json



app = Flask(__name__)

@app.route('/')
def getInputs():
    return render_template('page.html')

#need to make sure all values are correct
@app.route('/submitted', methods = ['POST', 'GET'])
def packInputs():
    try:
        if request.method == 'POST':
            data = request.form
            hour = int(data['alarmHour'])
            minute = int(data['alarmMinute'])
            print("here {} {}".format(hour,minute))
            if hour > 23 or hour < 0 or minute > 59 or minute < 0:
                print("in here now for some reason")
                raise ValueError("Not a valid time")
            with open('indata.txt','w') as file:
                json.dump(data,file)
            print("here2")
            return render_template('submitted.html', result = data)
    except ValueError:
        print("here3")
        return render_template('error.html')

    
@app.route('/data')
def sendData():
    with open('indata.txt','r') as file:
        data = json.load(file)
        return data


if __name__ == '__main__':
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(debug=True)
