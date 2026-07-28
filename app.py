import numpy as np
from flask import Flask,render_template,request,jsonify
import pickle

flask_app=Flask(__name__)
bundle = pickle.load(open("Crop_Recommendation_RF.pkl", "rb"))
model = bundle["model"]
scaler = bundle["scaler"]


@flask_app.route("/")
def home():
    return render_template("login.html")


@flask_app.route("/pred", methods = ["POST"])
def pred():
    float_features=[float(x) for x in request.form.values()]
    features=[np.array(float_features)]
    scaled_features = scaler.transform(features)
    prediction=model.predict(scaled_features)
    return render_template("login.html",Prediction_Text="The Recommended Crop to grow is : {}".format(prediction[0]))

if __name__== "__main__":
    flask_app.run(debug=True)