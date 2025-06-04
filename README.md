<h1 align="center">🤖 Multi-Agent Flask Chatbot</h1>

<p align="center">
  A smart and scalable chatbot system built with <strong>Flask</strong> that uses multiple AI agents (via OpenAI/Gemini API) to handle topic-specific conversations — from robotics to warfare tech!<br>
  <em>One route. Many minds. Infinite potential.</em>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue.svg">
  <img src="https://img.shields.io/badge/Flask-Web%20Framework-lightgrey.svg">
  <img src="https://img.shields.io/badge/OpenAI-Gemini-yellowgreen.svg">
  <img src="https://img.shields.io/badge/Status-Ongoing-brightgreen.svg">
</p>

---

## 🧠 What is This Project?

This chatbot project is designed as a **Flask web application** where a single route handles user input and dynamically responds through **specialized AI agents**. Each agent handles a distinct domain — such as robotics, construction, guns/planes, or general topics. It uses sessions to store the entire chat history so the conversation feels **fluid and continuous**, without any database required.

---

## ✨ Key Features

- 🔁 **Single Route Simplicity**  
  Handle all frontend interactions from one Flask route while keeping backend logic scalable.

- 🤖 **Multiple AI Agents**  
  Each message is routed intelligently to a category-specific agent (e.g., ConstructionBot, RoboticsBot).

- 💬 **Session-Based Chat History**  
  Chat messages persist across the conversation, only resetting when refreshed or manually cleared.

- 🔐 **API Key via `.env`**  
  Secure API access using environment variables.

- 📦 **Modular Agent System**  
  All AI logic lives in `agentsystem.py` and can be expanded easily.

---

## 🖼️ Demo UI Preview

<p align="center">
  <img src="https://i.imgur.com/DemoChatUI.png" width="700" alt="Chatbot UI Preview">
</p>

---

## 🧩 Project Structure

```bash
📦 flask-multi-agent-chatbot/
├── templates/
│   └── chatbot.html           # Stylish frontend chat UI
├── static/
│   └── style.css              # Optional: CSS styling
├── agentsystem(orti).py            # All AI agents and logic
├── app(fork).py                    # Main Flask app (single route)
├── .env                      # Stores API key securely
├── requirements.txt          # Python dependencies
└── README.md                 # You're reading it!
