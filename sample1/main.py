from flask import Flask, request, render_template
import requests

app = Flask(__name__)
  
@app.route('/', methods =["GET", "POST"])
def index(): 
    Ctemp = ''
    error = 0
    Temperature = ''
    if request.method == "POST":       
        Temperature= request.form.get("Temperature")  
        if temperature:
            Ctemp=Temperature/96
        else:
            error = 1    
    return render_template('index.html', data = Ctemp, Temperature=Temperature, error = error)
if __name__ == "__main__":
    app.run(host='127.0.0.1',port=8000,debug=True)
