#  PCA Visualization Web App

A simple and interactive Flask web application that allows users to **upload a CSV file**, performs **Principal Component Analysis (PCA)**, and visualizes the result using a scatter plot.

---

##  Features

- Upload your own dataset (CSV)
- Automatically handles missing values
- Applies PCA for dimensionality reduction (2D)
- Displays a scatter plot of the first two principal components
- Clean and responsive user interface

---


## 📁 Project Structure
```
PCA/
├── app.py # Flask web server
├── model.py # PCA transformation logic
├── templates/
│ ├── index.html # Upload UI
│ └── result.html # Plot display
├── static/
│ └── style.css # CSS styling
├── uploads/ # Folder for storing uploaded files
├── dataset/
│ └── sample_data.csv # Sample file for testing
└── README.md # Project documentation
```

---

##  Sample Dataset
```
CustomerID,Age,AnnualIncome,SpendingScore
1,19,15,39
2,21,15,81
3,20,16,6
4,23,16,77
5,31,17,40
6,22,17,76
7,35,18,6
8,23,18,94
9,64,19,3
10,30,19,72

```

---

##  How to Run

1. **Clone the Repository**  
        git clone https://github.com/yourusername/pca-visualizer-flask.git
        cd pca-visualizer-flask
        Install Dependencies
        Make sure Python 3.8+ is installed.
        pip install flask pandas matplotlib scikit-learn
        Run the App
        python app.py
        Open in Browser
        Go to http://127.0.0.1:5000 in your browser.
---
File Upload Instructions
![alt text](<Screenshot 2025-08-01 144015.png>)
Click "Choose File"
![alt text](image.png)
Select a CSV file with only numerical columns (optional label column is supported)
![alt text](<Screenshot 2025-08-01 144051.png>)
Click "Submit"
View the PCA plot (PC1 vs PC2)
![alt text](<Screenshot 2025-08-01 144102.png>)

🛠 Technologies Used
    Python 3.11+
    Flask
    Pandas
    Scikit-learn (PCA)
    Matplotlib
    HTML/CSS