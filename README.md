# 🎓 Student Performance Prediction

A Machine Learning project that predicts a student's academic performance based on various factors such as study hours, parental education, lunch type, test preparation course, gender, and other demographic information. The project includes data preprocessing, model training, evaluation, and deployment using Flask.

---

## 📌 Project Overview

The goal of this project is to build a machine learning model that can accurately predict a student's mathematics score using different input features. This helps educational institutions understand the factors affecting student performance and make data-driven decisions.

---

## 🚀 Features

- 📊 Exploratory Data Analysis (EDA)
- 🧹 Data Preprocessing and Feature Engineering
- 🤖 Machine Learning Model Training
- 📈 Model Evaluation
- 🌐 Flask Web Application
- 📝 User-friendly Prediction Interface
- 📦 Modular Project Structure

---

## 🛠️ Technologies Used

- Python
- Flask
- Pandas
- NumPy
- Scikit-learn
- CatBoost
- Matplotlib
- Seaborn
- HTML
- CSS

---

## 📂 Project Structure

```text
Student-Performance-Prediction/
│
├── .ebextensions/          # Deployment configuration
├── artifact/               # Saved trained models and preprocessors
├── catboost_info/          # CatBoost training logs
├── notebook/
│   └── data/               # Dataset and EDA notebooks
├── src/                    # Source code
├── templates/              # HTML templates
│
├── app.py                  # Flask application
├── application.py          # Deployment entry point
├── requirements.txt        # Required Python libraries
├── setup.py                # Project setup
├── .gitignore
└── README.md
```

---

## 📊 Dataset Features

The model uses the following features:

- Gender
- Race/Ethnicity
- Parental Level of Education
- Lunch Type
- Test Preparation Course
- Reading Score
- Writing Score

### 🎯 Target Variable

- Mathematics Score

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Student-Performance-Prediction.git
```

### 2. Navigate to the Project Folder

```bash
cd Student-Performance-Prediction
```

### 3. Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
python app.py
```

Open your browser and visit:

```
http://127.0.0.1:5000/
```

---

## 🧠 Machine Learning Workflow

1. Load the dataset
2. Perform data cleaning
3. Conduct exploratory data analysis
4. Encode categorical variables
5. Scale numerical features
6. Train multiple machine learning models
7. Evaluate model performance
8. Save the best-performing model
9. Deploy the model using Flask

---

## 📈 Model Evaluation

The model is evaluated using:

- R² Score
- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)

---

## 📷 Screenshots

You can add screenshots of your application here.

Example:

```text
screenshots/
│
├── home.png
├── prediction.png
└── result.png
```

---

## 📦 Requirements

Install all required libraries using:

```bash
pip install -r requirements.txt
```

---

## 🔮 Future Improvements

- Add User Authentication
- Improve User Interface
- Deploy on AWS, Render, or Railway
- Hyperparameter Optimization
- Add More Machine Learning Models
- Real-time Prediction API

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new feature branch
3. Commit your changes
4. Push your branch
5. Open a Pull Request



---

⭐ If you found this project useful, please consider giving it a Star on GitHub!
