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

📦 Install Requirements
Install the required Python packages:

bash
Copy
Edit
pip install flask pandas scikit-learn
▶️ Run the App
Start the Flask app by running:

bash
Copy
Edit
python app.py
Once running, open your browser and go to:

👉 http://127.0.0.1:8080/predict

🔁 How It Works
User fills out:

Name

Age

Role

Years of Experience

Flask sends the input to the ML model.

Model predicts the salary using the trained .pkl file.

The predicted salary is displayed below the form in green with a ₹ symbol.

🔄 Change the Port (Optional)
To change the default port, update the last line of app.py:

python
Copy
Edit
app.run(debug=True, port=8080)
You can replace 8080 with any other available port.

🧪 Train the Model (Optional)
To retrain or update the machine learning model with new data:

bash
Copy
Edit
python trainmodel.py
Ensure your salary.csv file has the following structure:

c
Copy
Edit
Name,Age,Role,Experience,Salary
John,30,Developer,5,50000
Alice,28,Designer,3,40000
Bob,35,Manager,8,70000
The model will be saved as model.pkl after training.





🙋‍♀️ About the Author
Made with 💖 by Zeenath Kousar Shaik
🔗 LinkedIn • 🌐 GitHub
