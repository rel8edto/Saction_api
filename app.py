from flask import Flask,request,jsonify
from trade_saction_api import tradGov




# http://10.8.1.34:2023/?name=FOZ FOR TRADING




app=Flask(__name__)

@app.route('/')




def index():



 


    data=request.args
    name=data.get('name')



    # raise Exception('page error')

    data=tradGov(name)
    
    return jsonify(data)
    # return df.to_html()
    # return resp

app.run(host='0.0.0.0',port='2023')
