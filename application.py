from flask import Flask, request, render_template
import numpy as np
import pandas as pd

from src.pipeline.predict_pipeline import CustomData, PredictPipeline

application = Flask(__name__)
app = application


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/predictdata', methods=['GET', 'POST'])
def predict_datapoint():

    if request.method == 'GET':
        return render_template('home.html')

    try:
        data = CustomData(
            gender=request.form.get('gender', '').strip(),
            race_ethnicity=request.form.get('ethnicity', '').strip(),
            parental_level_of_education=request.form.get('parental_level_of_education', '').strip(),
            lunch=request.form.get('lunch', '').strip(),
            test_preparation_course=request.form.get('test_preparation_course', '').strip(),
            reading_score=float(request.form.get('reading_score')),
            writing_score=float(request.form.get('writing_score'))
        )

        pred_df = data.get_data_as_data_frame()
        print("\nInput DF:\n", pred_df)

        predict_pipeline = PredictPipeline()
        results = predict_pipeline.predict(pred_df)

        return render_template('home.html', results=results[0])

    except Exception as e:
        print("Prediction Error:", e)
        return render_template('home.html', results="Invalid Input")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
