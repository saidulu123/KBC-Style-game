# KBC-Style Game

This project is a KBC-style game where questions are displayed on a computer screen. Players can scan a QR code with their mobile devices to join the game. They enter their names and answers on their mobile devices, and if they answer correctly, a congratulations message appears on the computer screen.

## Features

- Display questions on the computer screen.
- QR code generation for mobile access.
- Player name input on mobile.
- Answer submission from mobile.
- Feedback for correct and incorrect answers.
- Automatic progression to the next question.

## Technology Used

- **Flask**: For the backend web framework.
- **Socket.IO**: For real-time communication.
- **QR Code**: For generating codes to join the game.

## Setup Instructions

1. **Clone the Repository**
   ```bash
   git clone <repository-url>
   cd kbc-game
2. **Install Requirements**
   ```bash
   pip install -r requirements.txt
3. **Run the Application**
   ```bash
   python app.py

Access the Game Note: Open your browser and go to http://localhost:5000 to view the computer screen. Scan the QR code to join the game on your mobile device.

##Questions
The game includes the following questions:

1.What is the capital of France?

2.What is 2 + 2?

3.Who wrote 'Hamlet'?

4.What is the largest planet?

5.What year did World War II end?
