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

---

### 📦 Install Requirements

Install all required dependencies using pip:


pip install flask pandas scikit-learn
▶️ Run the Application



-Start the Flask server by running:

py app.py
Then, open your browser and navigate to:

👉 http://127.0.0.1:8080/predict

---

🔁 How It Works
User fills out a form with:

💠Name
💠Age
💠Role
💠Years of Experience




-The form data is sent to the backend via Flask.



-A pre-trained machine learning model (model.pkl) processes the input and predicts the salary.



-The predicted salary is shown below the form in green with a ₹ symbol.

---



🔄 Change the Port (Optional)
-If you want to run the app on a different port, modify the last line of app.py:

app.run(debug=True, port=8080)



-Replace 8080 with any available port of your choice (e.g., 5000, 3000, etc.).

---

🧪 Train the Model (Optional)
-To train or update the model with new data:

python trainmodel.py



▪Ensure that salary.csv is formatted like this:

-Name,Age,Role,Experience,Salary



-John,30,Developer,5,50000


-Alice,28,Designer,3,40000


-Bob,35,Manager,8,70000


After running the training script, a new model.pkl file will be generated.

---

🙋‍♀️ About the Author
Made with 💖 by Zeenath Kousar Shaik

🔗 LinkedIn • 🌐 GitHub

