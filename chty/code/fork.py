from flask import Flask, render_template, request, session
from flask_session import Session
from orti import get_chatbot_reply
import asyncio

app = Flask(__name__)

@app.route("/" , methods=["GET", "POST"])
def index():
    response=""
    if request.method=="POST":
        user_message=request.form["message"]
        category=request.form.get("category","auto")
        response=asyncio.run(get_chatbot_reply(user_message, category))
    return render_template("chatbot.html", response=response)    

if __name__ == "__main__":
    app.run(debug=True)        

