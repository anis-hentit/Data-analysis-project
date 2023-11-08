from flask import Flask, render_template, request
import xgboost as xgb  # Ensure XGBoost is installed
import pandas as pd

app = Flask(__name__)

# Load the XGBoost model
model = xgb.Booster()
model.load_model('XGboost_Model.model')  

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == "POST":
        # Get form data
        feature_dict = request.form.to_dict()
        print(feature_dict)
        
        try:
            prediction = preprocessDataAndPredict(feature_dict)
            print(prediction)
            return render_template('predict.html', prediction=prediction)
        except Exception as e:
            return "Error: " + str(e)

def preprocessDataAndPredict(feature_dict):
    # Create a DataFrame from the input data
    test_data = pd.DataFrame({k: [float(v)] for k, v in feature_dict.items()})
    test_data = pd.DataFrame(test_data)
    print(test_data.dtypes)
    # Features to standardize
    features_to_standardize = ["Customer_Value", "Frequency_of_Sms", "Frequency_of_Use", "Seconds_of_Use", "Subscription_Length", "Call_Failure", "Distinct_Called_Numbers"]

    # Means and standard deviations for standardization
    means = [470.97291587, 73.17492063, 69.46063492, 4472.45968254, 32.54190476, 7.62793651, 23.50984127]
    stds = [516.93336034, 112.21974279, 57.4041938, 4197.2422989, 8.57212108, 7.26273248, 17.21460431]

    # Standardize the specified features
    for feature, mean, std in zip(features_to_standardize, means, stds):
        test_data[feature] = (test_data[feature] - mean) / std

    # Use XGBoost model to make predictions
    prediction = model.predict(xgb.DMatrix(test_data))[0]
   
      # Apply a threshold to get the binary prediction (0 or 1)
    threshold = 0.5
    prediction = 1 if prediction >= threshold else 0
    print(prediction)

    return prediction


if __name__ == '__main__':
    app.run(debug=True)
