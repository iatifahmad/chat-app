# 🗨️ Real-Time Chat App with Django & Channels

A modern real-time chat application built with **Django**, **Django Channels**, and **WebSockets**.

---

✨ **Features:**

* User authentication with custom user model (email, first & last name) using  allauth library
* Real-time, end-to-end user-to-user messaging
* Message history persisted in the database
* Clean, responsive UI inspired by modern chat apps
* Online user list to pick who to chat with

---

## 🚀 Getting Started

### 1️⃣ Clone the repository

```bash
git clone https://github.com/iatifahmad/chat-app
cd chatapp
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
daphne chat_project.asgi:application
