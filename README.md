
# To Do List with user authentication and API

## My Website: <https://todolist-production-2fac.up.railway.app/>

### 下面有簡短的中文說明，可直接至下方觀看喔~

## Hompage

 ![ToDoList Homepage](To%20Do%20List%20Homepage.png "Homepage after login")

## Video Demo:  <URL HERE>(P.S. 剪輯影片，上傳YT後加入網址)

## Introduction

 This is an Web based To-Do-List application built with Python and its well known framework Django.

 There are 2 main applications in it. One of which is called "task" that perform CRUD functionalities to allow users to add task, view task, update task, and delete task, it also perform user authentications and password reset functionalities. Another application is called "api" that serialize all the tasks and then allow other programmers to access the data from FrontEnd through JSON format.

 As for the views, I combine both function-based views(FBV) and class-based views(CBV). I use function-based views(FBV) to create my CRUD functions, built in class-based views(CBV) for password reset functionalities, and the user authentication system that comes with Django.

## Motivation

 I found that I tend to have many tasks at hand, which I need a place for me to remember it, so that it won't take up too much of my mental space. Hence I created this app where I can just write down all my to-dos, and at thee same time learn more about Python and Django:)

## Learning Points

    - Python classes and inheritance
    - Django Framework
    - Django REST Framework(Serialization, Response, Request...)
    - How to build an API
    - How to interact with API through Postman
    - How to deploy project to Railway
    - setup environment variables

## Features

 1. CRUD functionalities:

    - Create Task
    - Read Task
    - Update Task
    - Delete Task

 2. User Authentication:

    - Login
    - Register
    - Logout

 3. Password Reset
  
## Installation

## The next version

    - Add a table for every category created
    - Search for task feature
    - create mobile app

## 專案說明

 這是一個用Django和Python寫的附使用者驗證功能的待辦清單app，它能讓使用者添加待辦事項、檢視待辦事項、更新待辦事項以及刪除待辦事項（CRUD），另外亦有密碼重設的功能，當使用著遞交需要重設密碼的需求後，系統會寄送重設密碼的信件至使用者的信箱以利密碼重設。
