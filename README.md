# 🤖 Flask-Based Chatbot System

A modular chatbot system built using Flask for routing and OpenAI agents for dynamic conversation handling. The backend integrates multiple specialized agents to handle diverse queries, while the front-end uses a simple HTML form for user interaction. This project demonstrates how to serve and manage agent-based conversations through Flask with session-based message history tracking.

---

## ✨ Features

- ✅ Flask routing with session-based chat history
- 🧠 Multi-agent backend using OpenAI API
- 📡 Interactive front-end via a lightweight HTML page
- 💬 Persistent chat history until page refresh
- 🔐 Securely integrated with OpenAI API key
- 🛠️ Simple setup, highly extendable

---

## 🖼️ Demo UI Preview

<p align="center">
  <img src="./code/ttt.PNG" width="700" alt="Chatbot UI Preview">
</p>

---

## 🚀 How It Works

1. The user types a message in the web interface.
2. Flask receives the input via a route and passes it to a Python backend.
3. The backend uses OpenAI agents (defined in `hotelsys.py`) to determine the appropriate response.
4. The reply is added to the session and displayed back in the browser.

---

## 📂 Project Structure

```plaintext
.
├── code/
│   └── ttt.PNG          # UI preview image saved inside 'code' folder
├── app.py               # Main Flask app with routing and session logic
├── hotelsys.py          # Backend logic using OpenAI multi-agent system
├── templates/
│   └── bot.html         # Frontend UI for chat interface
├── static/
├── requirements.txt     # Dependencies
└── README.md            # You're here!
