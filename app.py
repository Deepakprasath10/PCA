from flask import Flask, render_template, request
import pandas as pd
from model import apply_pca

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    file = request.files['file']
    if not file:
        return "No file uploaded."

    df = pd.read_csv(file)
    result_df = apply_pca(df)
    return render_template('results.html', tables=[result_df.to_html(classes='data')], titles=result_df.columns.values)

if __name__ == '__main__':
    app.run(debug=True)
