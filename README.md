# chat-app
A modern real-time chat application built with Django, Django Channels, and WebSockets.
# 🗨️ Real-Time Chat App with Django & Channels

A modern real-time chat application built with Django, Django Channels, and WebSockets.

✨ Features:

    User authentication with custom user model (email, first & last name)

    Real-time, end-to-end user-to-user messaging

    Message history persisted in the database

    Clean, responsive UI inspired by modern chat apps

    Online user list to pick who to chat with

    # 1️⃣ Clone the repository
git clone https://github.com/yourusername/chatapp.git
cd chatapp

# 2️⃣ Create and activate a virtual environment
python -m venv venv
# On Windows
venv\Scripts\activate
# On Linux/macOS
source venv/bin/activate

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Apply database migrations
python manage.py migrate

# 5️⃣ Create a superuser account
python manage.py createsuperuser

# 6️⃣ Run the development server (quick test)
python manage.py runserver

# 🔧 Or run with Daphne (for real ASGI + WebSockets)
daphne chat_project.asgi:application

