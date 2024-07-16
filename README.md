# DuckBot
Description:
This project is a web-based chatbot application developed as the final project for CS50x. The chatbot uses Flask as the web framework and DialoGPT for generating conversational responses. The project includes several key features:

# Features
User Registration and Login: 
Users can create an account and log in to access the chatbot. User authentication is implemented to ensure secure access.

Chat Interface: An interactive chat interface allows users to communicate with the chatbot. Messages are exchanged in real-time, and the chatbot responds using DialoGPT.

SQLite Database Integration: The application uses SQLite to store user data and chat history. This ensures that users can view their past interactions with the chatbot.

Chat History: A separate page displays the chat history, allowing users to review their previous conversations. The navigation bar facilitates easy access to this feature.

# Project Files:
app.py: The main Flask application file initializes the web server and defines the routes for user registration, login, chat interface, and chat history.

templates/: Directory containing HTML templates for the chat interface, registration, login, and chat history pages.

chat.html: The main chat interface where users interact with the chatbot.

history.html: The page displays the user's chat history.

register.html: The registration page for new users.

login.html: The login page for returning users.

static/: Directory containing static files such as CSS and JavaScript.

requirements.txt: Lists the Python dependencies required to run the application.

# Key Design Choices:
Flask Framework: Chosen for its simplicity and flexibility in building web applications.

DialoGPT: Selected for its advanced conversational capabilities, enhancing the user experience with realistic and engaging responses.

SQLite: SQLite is used for its lightweight nature and ease of integration with Flask, making it ideal for this project.

# How to Run the Project:
Install Dependencies: Please make sure you have Python installed, then run pip install -r Requirements.txt to install the necessary libraries.

Set Up the Database: Run the database initialization script to create the required tables.
```
CREATE TABLE users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    password TEXT NOT NULL
);
CREATE TABLE sqlite_sequence(name,seq);
CREATE TABLE chat_logs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    username TEXT NOT NULL,
    user_chat TEXT NOT NULL,
    bot_chat TEXT NOT NULL,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

Run the Application: Execute flask run to start the web server and access the chatbot through your web browser.
```
python app.py
```

