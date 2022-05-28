# ✔️MYSecure : Microsoft Engage Project'22( With Face Recognition Technology)

### MY-SECURE is the Web Application which helps you to manage your passwords as we generally have many passwords for different websites. So, It become difficult for us to remember them all and storing it any where is not secure at all. So, Here's MY-SECURE to help you to save and manage your passwords.

#### 🔗 Demo Video Link: https://youtu.be/DCnqAczzKlk
#### 🔗 Web Application(Hosted): https://mysecure1.herokuapp.com/
&nbsp;

#### ✂️ Note : As I was getting issue while merging the code of password manager and face recognition system as firstly I have made them seprately so I have hosted the password manager and then the link embeded in the face  recognition application. So, the code of passwd Manager is in another repository. You can access it through the link below 👇.
#### 🔗 Password-Manager2 Github Repository link: https://github.com/mansi2024/PasswdManager
&nbsp;

## 📃Table of Contents
📌 [Features](#features)<br>
📌 [Tech Stack Used](#tech-stack)<br>
📌 [Getting Started](#getting-started)<br>
📌 [Application Flow](#flow)<br>
📌 [Challanges faced and learnings](#challenges)<br>
📌 [Resources](#resources)<br>

<a id="features"></a>
## ✈️Features
- Firstly, It's a two step Authentication application where first you need to register and login with your face and email id.
- After, Logging-in with your face you will get access to MY-SECURE Password-Manager tool.
- Again You need to sign-up and then sign-in then you will be able to store all your confidential and password in your account of MY-SECURE.
- You can add details of different websites password, username, emails and website link with MY-SECURE.
- You can update your password and other information anytime.
- You can also delete your website details anytime.
- [Add more Features](#scope)
&nbsp;

<a id="tech-stack"></a>
## 💻Tech Stack Used
🔧Flask + 🔧Python - for Server-Side development.<br>
🔧JavaScript + 🔧HTML + 🔧CSS + 🔧Bootstrap5 - for frontend development.<br>
🔧VisualStudioCode - IDE Used for development.<br>
&nbsp;

<a id="getting-started"></a>
## 🚀Getting Started
- Clone the git repository.
```
  git clone git@github.com:mansi2024/MYSecure.git.
```
- Creating the Virtual Environment.
```
  pipenv shell
  
```
- Installing All the requirements
```
  pip install -r requirements.txt
```
- Setting up the environment.
```
   $env:FLASK_APP="app.py"
   $env:FLASK_ENV="development"
   
```
- Run the Application.
```
   flask run
```

<a id="flow"></a>
## 📋Application Flow

#### - Welcome to MY-SECURE(First Page) 
 You can register from here and then login.
 
<img width="1432" alt="pic1" src="https://github.com/mansi2024/Images/blob/main/Screenshot%20(49).png">
 
#### - Registeration Page (UI of Login Page is just similar)

<img width="1432"  alt="pic2" src="https://github.com/mansi2024/Images/blob/main/Screenshot%20(36).png">
&nbsp;
<img width="1432" alt="pic3" src="https://github.com/mansi2024/Images/blob/main/Screenshot%20(37).png">

### - Password Manager (Access)
Now you have access to Password Manager tool

<img width="1432" alt="pic4" src="https://github.com/mansi2024/Images/blob/main/Screenshot%20(40).png">

### - Sign-Up and then Sign-in


<img width="1432" alt="pic5" src="https://github.com/mansi2024/Images/blob/main/Screenshot%20(41).png">
<img width="1432" alt="pic01" src="https://github.com/mansi2024/Images/blob/main/Screenshot%20(42).png">

### - Add Password

<img width="1432" alt="pic" src="https://github.com/mansi2024/Images/blob/main/Screenshot%20(45).png">

### - Your Account
Here you can add passwords , update your account deatails by clicking on Account.

<img width="1432" alt="pic6" src="https://github.com/mansi2024/Images/blob/main/Screenshot%20(44).png">

### - Your Dashboard
Here all your Saved Password is where you can also update , delete your website details.

<img width="1432" alt="pic7" src="https://github.com/mansi2024/Images/blob/main/Screenshot%20(51).png">

<a id="challenges"></a>
## Challenges Faced and Learnings
- I don't know Flask and never built any application on it, So firstly I have learned Flask through Linkedln learning completed the flask essential training, made the URL shortener small application to understand it more and then started to build MY-SECURE.
- I have faced problem in using Face Recognition Library but read documentation and successfully able to implement it.
- I have faced a lot issues and errors while making login system using Flask but read the doocumentation of flask-login and some youtube videos really helped alot.
- After I have made two seperate models like face recognition and password manager by thinking that I will be able to merge it but faced the issue and many errors due to may be version related issue, This has taken my lot of time and even upto 3-4 days. after that I have gotten the idea to host the password manager and embed the link in my first application.
- I have learned a lot during Engage programm and fall in love with development and problem solving. It's overall a great experience.




