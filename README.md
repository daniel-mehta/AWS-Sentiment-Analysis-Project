# AWS Sentiment Analysis Project

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue.svg)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-2.0+-darkgreen)](https://flask.palletsprojects.com/)
[![AWS Comprehend](https://img.shields.io/badge/AWS-Comprehend-orange)](https://aws.amazon.com/comprehend/)
[![Deployed on AWS EC2](https://img.shields.io/badge/Deployed-AWS%20EC2-yellowgreen)](https://aws.amazon.com/ec2/)

This is a web-based sentiment analysis application that leverages AWS Comprehend to analyze the sentiment of user-provided text. The application is deployed on an AWS EC2 instance and built using Python (Flask), HTML, and the AWS SDK (Boto3).

> **Made for:**  
> *Machine Learning Cloud Computing (AIGC-5003)*  
> Humber Polytechnic, AI and Machine Learning Postgraduate Program

---

## 🌐 Live Demo

Watch the full application walkthrough here: [YouTube Demo](https://youtu.be/taQoIowwERg)

---

## 📌 Features

- User-friendly web interface for entering text  
- Real-time sentiment analysis using AWS Comprehend  
- Deployment-ready Flask backend on AWS EC2  
- Secure SSH access and configurable AWS Security Groups  
- Returns overall sentiment: **Positive**, **Negative**, or **Neutral**

---

## 🛠️ Technologies Used

- **Frontend:** HTML (`index.html`)  
- **Backend:** Python + Flask (`main.py`)  
- **Sentiment Analysis:** AWS Comprehend (`comprehend.py`)  
- **Deployment:** AWS EC2, SSH, Security Groups  
- **Cloud SDK:** Boto3

---

## 📂 Project Structure
```bash
.
├── main.py                  # Flask backend server
├── comprehend.py            # AWS Comprehend sentiment analysis logic
├── index.html               # Frontend UI
├── Sample Input.csv         # Sample input data
├── *.png                    # Screenshots
├── AWS Sentiment Analysis Project Documentation.pdf
└── README.md                # You're here!
```

---

## 📷 Screenshots
Screenshots provided include:
- Web UI showing sentiment results
- EC2 instance setup and SSH session
- Security Group rule allowing traffic on port 5000

---

## 🧠 How It Works

**1. User Input**  
The user enters a sentence into the input text field on the web page.

**2. Processing**  
Once the user clicks "Analyze Sentiment," the text is sent to the Flask backend. The backend uses AWS Comprehend to analyze the sentiment.

**3. Output**  
The result (Positive, Negative, or Neutral) is returned and displayed on the refreshed web page.

---

