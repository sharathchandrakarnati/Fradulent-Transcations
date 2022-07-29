#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import numpy as np
import pickle
import joblib
from flask import Flask, request, render_template

app = Flask(__name__)
#model = pickle.load(open("model.pkl", 'rb'))
with open('model.pkl','rb') as f:
        model=joblib.load(f)

@app.route('/')
def index():
    return render_template(
        'index.html',
        data=[{'typeid': "Type"}, {'typeid': "CASH_IN"}, {'typeid': "CASH_OUT"}, {'typeid': "DEBIT"},
               {'typeid': 'PAYMENT'}, {'typeid': "TRANSFER"}])


@app.route("/predict", methods=['GET', 'POST'])
def predict():
    input_data = list(request.form.values())
    
    if input_data[0].isdigit() == True & input_data[1].isdigit() == True & input_data[2].isdigit() == True & input_data[3].isdigit() == True & input_data[4].isdigit() == True:
        pass
    else:
        print(ValueError)

    if input_data[5] == 'CASH_IN':
        input_data[5] = 0
    elif input_data[5] == 'CASH_OUT':
        input_data[5] = 1
    elif input_data[5] == 'DEBIT':
        input_data[5] = 2
    elif input_data[5] == 'PAYMENT':
        input_data[5] = 3
    elif input_data[5] == 'TRANSFER':
        input_data[5] = 4    
    else:
        print(ValueError)

    input_values = [x for x in input_data]
    y=float(input_values[0])
    w=float(input_values[1])
    z=float(input_values[2])
    a=float(input_values[3])
    b=float(input_values[4])
    c=float(input_values[5])
    #arr_val = [np.array(input_values)]
    #arr_val = np.array([input_values]).reshape(1,-1)
    
    arr_val=np.array([y,w,z,a,b,c]).reshape(1,-1)
    prediction = model.predict(arr_val)
    
    if prediction == 0:
        output ="Not_Fraud"
    else:
        output ="Fraud"
    
    return render_template('index.html', prediction_text=" The predicted transaction is {}".format(output),
                           data=[{'typeid': "Type"}, {'typeid': "CASH_IN"}, {'typeid': "CASH_OUT"}, {'typeid': "DEBIT"},
                                 {'typeid': 'PAYMENT'}, {'typeid': "TRANSFER"}])


if __name__ == '__main__':
    app.run(debug=True)

