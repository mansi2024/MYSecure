# ✔️MYSecure : Microsoft Engage Project'22( With Face Recognition Technology)

### MY-SECURE is the Web Application that helps you manage your passwords as we generally have many passwords for different websites. So, It becomes difficult for us to remember them all, and storing it anywhere is not secure at all. So, Here's MY-SECURE to help you to save and manage your passwords.

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
- Firstly, It's a two-step Authentication application where first you need to register and log in with your face and email ID.
- After logging in with your face you will get access to the MY-SECURE Password-Manager tool.
- Again You need to sign up and then sign in Then you will be able to store all your confidential passwords in your account of MY-SECURE.
- You can add details of different websites' passwords, usernames, emails, and website links with MY-SECURE.
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
 You can register from here and then log in.
![Screenshot (49)](https://user-images.githubusercontent.com/87639872/195309749-53db1774-f7a1-4632-a961-895c30307d24.png)
 
#### - Registration Page (UI of Login Page is just similar)
![Screenshot (36)](https://user-images.githubusercontent.com/87639872/195307551-09f4ccb8-d1e4-4d91-af56-07ae7f695d0d.png)
&nbsp;
![Screenshot (37)](https://user-images.githubusercontent.com/87639872/195309839-dee2f363-603b-4780-8151-198221c57004.png)

### - Password Manager (Access)
Now you have access to Password Manager tool
![Screenshot (40)](https://user-images.githubusercontent.com/87639872/195309789-28ce87fc-a3c0-4e50-8b74-685280b015d5.png)


### - Sign-Up and then Sign-in

![Screenshot (41)](https://user-images.githubusercontent.com/87639872/195309781-563a98b6-4c51-47d2-8839-b258609ba124.png)
![Screenshot (42)](https://user-images.githubusercontent.com/87639872/195309779-49d22202-7615-4c73-9196-254721632d19.png)

### - Add Password
![Screenshot (45)](https://user-images.githubusercontent.com/87639872/195309762-6de0634c-d579-4eb7-a15d-e78ef8af111d.png)


### - Your Account
Here you can add passwords, and update your account details by clicking on Account.
![Screenshot (44)](https://user-images.githubusercontent.com/87639872/195309767-4dd48d41-f6d9-4d25-907b-5bb91d30cb19.png)

### - Your Dashboard
Here all your Saved Password is where you can also update, and delete your website details.
![Screenshot (51)](https://user-images.githubusercontent.com/87639872/195309738-9d584376-bf82-4851-a774-6bb24d44b6e7.png)

<a id="challengthe es"></a>
## Challenges Faced and Learnings
- I don't know Flask and never built any application on it, So firstly I learned Flask through LinkedIn Learning completed the Flask essential training, made the URL shortener small application to understand it more, and then started to build MY-SECURE.
- I have faced problems in using Face Recognition Library but read the documentation and was successfully able to implement it.
- I have faced a lot of issues and errors while making a login system using Flask but reading the documentation of Flask-login and some YouTube videos helped alot.
- After I had made two separate models face recognition and password manager thinking that I would be able to merge it but faced the issue and many errors due to a version related issue, This has taken a lot of time and even up to 3-4 days. after that, I got the idea to host the password manager and embed the link in my first application.
- I have learned a lot during the Engage program and fell in love with development and problem-solving. It's overall a great experience.




