# 💼 Employee Salary Predictor 🔮

> A smart web app that predicts employee salaries based on **Age**, **Role**, and **Experience** using **Machine Learning**.

---

## 📸 Live Preview

![App Preview](link-to-screenshot-if-you-have-one)

---

## 🧠 Features

- ✨ Clean, user-friendly interface
- 📊 Salary prediction using ML model
- 📥 Form inputs: Name, Age, Role, Experience
- ⚡ Instant salary prediction display
- 🌐 Fully responsive design
- 🧩 Easy to integrate, customize, and extend

---

## 📁 Project Structure

employee-salary-predictor/
├── app.py # Flask server and routing
├── model.pkl # Trained ML model for prediction
├── trainmodel.py # Script to train and save the model
├── salary.csv # Dataset used for training
├── templates/
│ └── index.html # HTML form page
├── static/
│ └── style.css # CSS styling
└── README.md # Project overview and instructions

yaml
Copy
Edit

---

## ⚙️ Tech Stack

| Frontend     | Backend       | ML/Model            |
|--------------|---------------|---------------------|
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
Open your browser and go to:

👉 http://127.0.0.1:8080/predict

🔁 How It Works
User fills out:

Name

Age

Role

Years of Experience

Flask sends this input to the ML model.

The model predicts the salary using the trained model.pkl.

The predicted salary is displayed below the form in green with a ₹ symbol.

🔄 Change the Port (Optional)
To change the port, modify the last line of app.py:

python
Copy
Edit
app.run(debug=True, port=8080)
Replace 8080 with your desired port number.

🧪 Train the Model (Optional)
To retrain the model with new data:

bash
Copy
Edit
python trainmodel.py
Make sure your salary.csv follows this format:

cs
Copy
Edit
Name,Age,Role,Experience,Salary
John,30,Developer,5,50000
Alice,28,Designer,3,40000
Bob,35,Manager,8,70000
A new model.pkl file will be generated.

🙋‍♀️ About the Author
Made with 💖 by Zeenath Kousar Shaik
🔗 LinkedIn • 🌐 GitHub
