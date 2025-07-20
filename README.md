# 💼 Employee Salary Predictor 🔮

[![Python](https://img.shields.io/badge/Python-3.10-blue?logo=python)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-Web%20Framework-lightgrey?logo=flask)](https://flask.palletsprojects.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> 🔎 A smart web app that predicts employee salaries based on Age, Role, and Experience using Machine Learning!

---

## 📸 Live Preview

<img src="preview.png" alt="App Preview" width="700"/>

---

## 🧠 Features

✨ Clean, user-friendly interface  
📊 ML model for salary prediction  
📥 Form inputs: Name, Age, Role, Experience  
⚡ Instant result display  
🌐 Fully responsive design  
🧩 Easy to integrate and extend  

---

## 📁 Project Structure

employee-salary-predictor/
├── app.py # Flask server and routing
├── model.pkl # Trained salary prediction ML model
├── trainmodel.py # Script to train and export the model
├── salary.csv # Dataset for training
├── templates/
│ └── index.html # Frontend HTML form
├── static/
│ └── style.css # Styling for the form
└── README.md # Project overview and instructions


## ⚙️ Tech Stack

| Frontend     | Backend     | ML/Model     |
|--------------|-------------|--------------|
| HTML5, CSS3  | Python, Flask | scikit-learn, pandas |

---

## 🚀 Getting Started

### 🔧 Prerequisites

- Python 3.10+
- pip (Python package manager)

### 📦 Install Requirements

```bash
pip install flask pandas scikit-learn
▶️ Run the App
bash
Copy
Edit
python app.py
Then open your browser at:
👉 http://127.0.0.1:8080/predict

🔁 How It Works
User fills out Name, Age, Role, and Experience

Flask sends this data to the ML model

Model predicts the salary using the trained .pkl file

The result is shown below the form in green with a ₹ symbol

🔄 Changing the Port
In app.py, modify the last line:

python
Copy
Edit
app.run(debug=True, port=8080)
Change 8080 to any other port if needed.

🧪 Train the Model (Optional)
To retrain or customize the ML model:

bash
Copy
Edit
python trainmodel.py
Ensure your salary.csv has valid format:

python-repl
Copy
Edit
Name, Age, Role, Experience, Salary
John, 30, Developer, 5, 50000
...



🙋‍♀️ About the Author
Made with 💖 by Zeenath Kousar Shaik
🔗 LinkedIn • 🌐 GitHub
