import pickle
import numpy as np
from flask import Flask, render_template, request
app = Flask(__name__)

ipe = pickle.load(open("pipe.pkl", "rb"))

@app.route('/', methods=['GET','POST'])
def predict():
    if request.method=="GET":
        form = request.form
        try:
            Company = form.get('Company')
            TypeName = form.get('TypeName')
            Inches = form.get('Inches')
            Touchscreen = form.get('Touchscreen')
            IPS = form.get('IPS')
            Cpu_Name = form.get('cpu_Name')
            cpu_type = form.get('cpu_type')
            Ram = form.get('Ram')
            Memory = form.get('Memory')
            Memory_Storage = form.get('Memory_Storage')
            Gpu_brand = form.get('Gpu_brand')
            Gpu_type = form.get('Gpu_type')
            Weight = form.get('Weight')
            os = form.get('os')
        except ValueError:
            # Handle the case where conversion to float fails
            return render_template('error.html', message="Invalid input. Please select a valid option.")
        x=np.array([Company,TypeName,Inches,Touchscreen,IPS,Cpu_Name,cpu_type,Ram,
                    Memory,Memory_Storage,Gpu_brand,Gpu_type,Weight,os])
        x=x.reshape(1,14)
        pred = str(int(np.exp(ipe.predict(x)[0])))
        return render_template('index.html',pred=pred)
    return render_template('index.html')

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=5000, debug=True)
 