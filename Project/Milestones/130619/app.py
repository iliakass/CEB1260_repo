from flask import Flask, render_template, request
from sklearn.externals import joblib
import os

app = Flask(__name__, static_url_path='/static/')


@app.route('/')
def form():
    return render_template('index.html')

#@app.route('/predict_price', methods=['POST', 'GET'])
@app.route('/D_DIFF_B', methods=['POST', 'GET'])

#def predict_price():
def D_DIFF_B():
    # get the parameters
    LAST_DM = float(request.form['LAST_DM'])

    # 'LAST_DM',
    # Web app text: Month of the last extermination
    # (options: 1 thru 12)

    # Previous:: bedrooms = float(request.form['bedrooms'])

    LAST_DY = float(request.form['LAST_DY'])
    # 'LAST_DY',
    # Web app text: Year of the last extermination
    # (options: 2018 thru 2019)

    # Previous:: bathrooms = float(request.form['bathrooms'])

    EPI_DIST_1 = float(request.form['EPI_DIST_1'])
    # 'EPI_DIST_1',
    # Web app text: Distance from interesection (-73.585636, 45.527404) in Parc-Laurier, Le Plateau-Mont-Royal
    # (options in km: 2, 4, 8, 10, 12, 14)

    # Previous:: sqft_living15 = float(request.form['sqft_living15'])

    EPI_DIST_4 = float(request.form['EPI_DIST_4'])
    # 'EPI_DIST_4',
    # Web app text: Distance from interesection (-73.571239, 45.584338) in Grande-Prairie, Saint-Léonard
    # (options in km: 2, 4, 8, 10, 12, 14)

    # Previous::  grade = float(request.form['grade'])

    EPI_DIST_5 = float(request.form['EPI_DIST_5'])
    # 'EPI_DIST_5'
    # Web app text: Distance from interesection (-73.68714399999999, 45.518173) in Grenet, Saint-Laurent
    # (options in km: 2, 4, 8, 10, 12, 14)

    # Previous::  condition = float(request.form['condition'])

    # load the model and predict
    model = joblib.load('model/Random_Forest_10.pkl')
    # use \model\Random_Forest_10.pkl rather than \model\linear_regression.pkl

    prediction = model.predict([[LAST_DM, LAST_DY, EPI_DIST_1, EPI_DIST_4, EPI_DIST_5]])
    D_DIFF_B = prediction.round(1)[0]

    return render_template('results.html',
                           LAST_DM=int(LAST_DM),
                           LAST_DY=int(LAST_DY),
                           EPI_DIST_1=int(EPI_DIST_1),
                           EPI_DIST_4=int(EPI_DIST_4),
                           EPI_DIST_5=int(EPI_DIST_5),
                           D_DIFF_B="{:,}".format(D_DIFF_B)
                           # ['D_DIFF_B']
                           # Web app text: Waiting time (days) for extermination
                           )


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
