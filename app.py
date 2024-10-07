from flask import Flask, render_template, request, redirect, url_for
from flask_socketio import SocketIO, emit
import qrcode
import io
import base64

app = Flask(__name__)
socketio = SocketIO(app)

# Sample questions for the KBC game
questions = [
    {"question": "What is the capital of India?", "answer": "Delhi"},
    {"question": "What is 2 + 2?", "answer": "4"},
    {"question": "What is the color of Human Blood?", "answer": "Red"},
    {"question": "What is the largest planet?", "answer": "Jupiter"},
    {"question": "What year did World War II end?", "answer": "1945"}
]

current_question = 0  

@app.route('/')
def home():
    return render_template('computer.html', question=questions[current_question]['question'], qr_code=generate_qr())

@app.route('/mobile')
def mobile_view():
    return render_template('mobile.html', question=questions[current_question]['question'])

@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    global current_question
    player_answer = request.form['answer']
    player_name = request.form['name']
    
    if player_answer.strip().lower() == questions[current_question]['answer'].lower():
        socketio.emit('correct_answer', {'name': player_name})
        current_question += 1
        if current_question >= len(questions):
            current_question = 0  
        return render_template('mobile.html', message="Congratulations, your answer is correct!", question=questions[current_question]['question'])
    else:
    
        return render_template('mobile.html', message="Wrong answer, please try again!", question=questions[current_question]['question'])

def generate_qr():
    """Generate QR code linking to the mobile view"""
    local_ip = 'http://192.168.29.210:5000/mobile'  # My IP adress [Enter your IP adress here]
    img = qrcode.make(local_ip)
    buf = io.BytesIO()
    img.save(buf)
    buf.seek(0)
    img_base64 = base64.b64encode(buf.read()).decode('ascii')
    return f"data:image/png;base64,{img_base64}"

@socketio.on('connect')
def handle_connect():
    print("A player connected!")

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)
