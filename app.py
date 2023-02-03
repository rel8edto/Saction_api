from flask import Flask,request,jsonify
from trade_saction_api import tradGov
from ofac_sanction import searchOfac


# http://10.8.1.34:2023/?name=FOZ FOR TRADING&source=ofac




app=Flask(__name__)

@app.route('/')




def index():



    functiondict={"trade":tradGov,"ofac":searchOfac}

    


    data=request.args
    name=data.get('name')
    source=data.get('source')
    count=data.get('count')


    try:
        count=int(count)
        if count>25:
            count=25

    except Exception as e:
        count=10

    searchfunction=functiondict.get(source)



    # raise Exception('page error')

    data=searchfunction(name,count)
    
    return jsonify(data)
    # return df.to_html()
    # return resp

app.run(host='0.0.0.0',port='2023')
