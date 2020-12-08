import sqlite3
from flask import Flask, render_template
from flask_socketio import SocketIO, send

# Initialize sockets and app
app = Flask(__name__)
app.config["SECRET_KEY"] = "secret"
socket = SocketIO(app)
db = sqlite3.connect("chat.sqlite3", check_same_thread = False)
cursor = db.cursor()

@app.route("/")
def index():



@app.route("/chat")
def chat():
	return render_template("chat.html")

# Listen to a event named message
@socket.on("message")
def handle_message(msg):
	print("Message:", msg)
	send(msg, broadcast = True)


if __name__ == '__main__':
	socket.run(app, debug = True)