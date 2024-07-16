from flask import Flask, flash, redirect, render_template, request, jsonify, session, url_for
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch
import sqlite3
from werkzeug.security import generate_password_hash, check_password_hash

# Initialize the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("microsoft/DialoGPT-medium")
model = AutoModelForCausalLM.from_pretrained("microsoft/DialoGPT-medium")

app = Flask(__name__)
app.secret_key = '1234'

Database = 'chatbot.db'

def get_db():
    conn = sqlite3.connect(Database)
    return conn

@app.route("/")
def index():
    username = session.get('username')
    return render_template('chat.html', username=username)

@app.route("/get", methods=["POST"])
def chat():
    msg = request.form["msg"]
    user_id = session.get('user_id')
    username = session.get('username')

    if user_id and username:  # Check if user is logged in
        # Get response from the chatbot
        bot_response = get_Chat_response(msg)

        # Store the chat log in the database
        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO chat_logs (user_id, username, user_chat, bot_chat) VALUES (?, ?, ?, ?)",
                       (user_id, username, msg, bot_response))
        conn.commit()
        conn.close()

        return jsonify(bot_response)
    else:
        # If user is not logged in, return bot response without storing in database
        return jsonify(get_Chat_response(msg))

def get_Chat_response(text):
    # Encode the user input
    new_user_input_ids = tokenizer.encode(text + tokenizer.eos_token, return_tensors='pt')

    # Append the new user input tokens to the chat history
    bot_input_ids = new_user_input_ids

    # Generate a response while limiting the total chat history to 1000 tokens
    chat_history_ids = model.generate(bot_input_ids, max_length=1000, pad_token_id=tokenizer.eos_token_id)

    # Decode and return the response
    response = tokenizer.decode(chat_history_ids[:, bot_input_ids.shape[-1]:][0], skip_special_tokens=True)
    return response

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username = ?", (username,))
        user = cursor.fetchone()
        conn.close()

        if user and check_password_hash(user[2], password):
            session['user_id'] = user[0]
            session['username'] = user[1]
            flash('Logged in successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password', 'danger')

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            flash('Passwords do not match!', 'danger')
            return redirect(url_for('register'))

        hashed_password = generate_password_hash(password)

        conn = get_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO users (username, password) VALUES (?, ?)", (username, hashed_password))
        conn.commit()
        conn.close()

        flash('You have successfully registered!', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/logout')
def logout():
    session.clear()
    flash('You have been logged out!', 'success')
    return redirect(url_for('index'))



@app.route('/history')
def history():
    if 'user_id' not in session:
        flash('You need to log in to view your chat history.', 'danger')
        return redirect(url_for('login'))

    user_id = session['user_id']

    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT username, user_chat, bot_chat FROM chat_logs WHERE user_id = ?", (user_id,))
    chats = cursor.fetchall()
    conn.close()

    chat_data = [{'username': chat[0], 'user_chat': chat[1], 'bot_chat': chat[2]} for chat in chats]

    return render_template('history.html', chats=chat_data)



if __name__ == '__main__':
    app.run(debug=True)
