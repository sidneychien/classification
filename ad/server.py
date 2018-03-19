#-*- coding: utf-8 -*-
from flask import Flask, request, Response
import algorithms.ouhandlehelper as ouh
import util.dom as dom
import json
import operator

app = Flask(__name__)


# load OUhelper into memory
from tgrocery import Grocery
OUHelper = Grocery('C:/Users/24613Desktop/aASADd/algorithms/handleHelper')
OUHelper.load()


@app.route('/ouhandlehelper', methods=['POST'])
def api_ouhandlehelper():
    if request.headers['Content-Type'] == 'application/json':
        json_data = json.loads(request.data, encoding='utf-8')
        text = ouh.analyze_json(json_data)
        grocery_predict = OUHelper.predict(text)
        dec_values = grocery_predict.dec_values
        sorted_dec = sorted(dec_values.iteritems(), key=operator.itemgetter(1), reverse=True)
        base = 0.
        for i in range(5): base += sorted_dec[i][1]
        rst = []
        for i in range(5):
            if base == 0.:
                rst.append({"OUName":sorted_dec[i][0], "Probability":sorted_dec[i][1]})
            else:
                rst.append({"OUName":sorted_dec[i][0], "Probability":sorted_dec[i][1]/base})
        return json.dumps({"DecValues": rst})
    else:
        return "Wrong Content-Type or wrong method, please check API document carefully. """


if __name__ == "__main__":
    config_host, config_port = dom.get_config('config/config.xml')
    app.run(host=config_host, port=config_port, debug=True)
