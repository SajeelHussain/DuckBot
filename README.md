
# DuckBot
#### Video Demo:  <https://youtu.be/eFlqBhqp83M>
#### Description:


This project is a web-based chatbot application developed as the final project for CS50x. The chatbot uses Flask as the web framework and DialoGPT for generating conversational responses. The project includes several key features designed to enhance user interaction and provide a seamless chat experience.

# Features
## User Registration and Login
Users can create an account and log in to access the chatbot. User authentication is implemented to ensure secure access. During registration, users provide a username and password, which are stored securely in the SQLite database. The login system checks these credentials to grant access to the chat interface.

## Chat Interface
An interactive chat interface allows users to communicate with the chatbot. Messages are exchanged in real-time, and the chatbot responds using DialoGPT. The interface is designed to be intuitive and user-friendly, with messages displayed in a conversation-like format. Users can type their queries, and the bot responds almost instantaneously.

## SQLite Database Integration
The application uses SQLite to store user data and chat history. This ensures that users can view their past interactions with the chatbot. The database is lightweight yet powerful enough to handle multiple users and their respective chat logs. Each user’s chat history is linked to their account, providing personalized access.

## Chat History
A separate page displays the chat history, allowing users to review their previous conversations. The navigation bar facilitates easy access to this feature. Users can see a chronological list of their interactions with the chatbot, which can be useful for recalling previous information or continuing a past conversation.

# Project Files
## app.py
The main Flask application file initializes the web server and defines the routes for user registration, login, chat interface, and chat history. It handles the logic for each route, processes user input, and communicates with the database and DialoGPT to generate responses.

## templates/
This directory contains HTML templates for the chat interface, registration, login, and chat history pages. Each HTML file is designed to render dynamically with user-specific data, creating a personalized experience.

# chat.html: 
chat.html serves as the main interface where users engage in conversations with the chatbot. It's designed to provide a seamless and intuitive user experience, leveraging HTML, CSS, and JavaScript to facilitate real-time interaction.

## Key Features:

Message Display: Messages exchanged between the user and the chatbot are dynamically displayed in a conversation-style format. Each message includes timestamps for clarity and order.

User Input: A text input field allows users to type their messages and submit them to the chatbot. The interface supports various input types, including text, emojis, and basic formatting.

Bot Responses: Responses from the chatbot are asynchronously fetched and displayed in the chat interface. This ensures a responsive user experience without page reloads.

Interactive Elements: Depending on the application's design, interactive elements such as buttons, links, or forms may be integrated to enhance user engagement and interaction flow.
# history.html: 
history.html provides users with access to their past interactions with the chatbot, offering a chronological view of previous conversations.

## Key Features:

Chat History Display: Chat logs are presented in a structured manner, typically organized by date or conversation thread. Each entry may include user messages, bot responses, and timestamps.

Navigation Controls: Users can navigate through their chat history using pagination, infinite scrolling, or a timeline-based interface. 
# register.html: 
history.html provides users with access to their past interactions with the chatbot, offering a chronological view of previous conversations.

## Key Features:

Chat History Display: Chat logs are presented in a structured manner, typically organized by date or conversation thread. Each entry may include user messages, bot responses, and timestamps.

Navigation Controls: Users can navigate through their chat history using pagination, infinite scrolling, or a timeline-based interface. 

## Key Features:

User Registration Form: The form collects essential user information, typically including username, password, email address, and optional profile details. Input fields may feature client-side validation to ensure data integrity before submission.
# login.html:
login.html provides a secure gateway for returning users to authenticate themselves and access the chatbot application.

##Key Features:

User Authentication Form: Users input their credentials (username and password) to verify their identity. The form includes mechanisms for securely transmitting sensitive information, such as HTTPS encryption.
# static/
This directory contains static files such as CSS for styling the web pages. The CSS files ensure that the application has a clean and modern look, improving the overall user experience.

## requirements.txt
This file lists the Python dependencies required to run the application. It includes Flask, DialoGPT, and other necessary libraries. Installing these dependencies ensures that the application runs smoothly.

# Key Design Choices
# Flask Framework
Flask was chosen for its simplicity and flexibility in building web applications. It provides a solid foundation for routing and handling HTTP requests while being lightweight and easy to work with.

## DialoGPT
DialoGPT was selected for its advanced conversational capabilities, enhancing the user experience with realistic and engaging responses. Its pre-trained model allows for sophisticated dialogue generation, making the chatbot feel more natural and interactive.

## SQLite
SQLite is used for its lightweight nature and ease of integration with Flask, making it ideal for this project. It is a self-contained, serverless database engine that provides all the functionalities needed for user authentication and chat history management without the overhead of more complex database systems.

# How to Run the Project
## Install Dependencies
Ensure you have Python installed on your system. Then, run the following command to install the necessary libraries:
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

