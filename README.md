KBC-Style Game
Overview
This project is a KBC-style game where players can join through their mobile devices. The game displays questions on a computer screen, and players can answer them from their phones. When a player answers correctly, a congratulatory message is shown on the computer.

Features
Display Questions: The computer screen shows the current question and a QR code for players to join.
Mobile Interface: Players scan the QR code, enter their names, and see the same question on their devices.
Answer Validation: If a player submits the correct answer, a congratulations message appears on the computer screen. If the answer is wrong, the player receives an error message on their phone.
Sample Questions: The game includes five sample questions to play with.
Technologies Used
Flask: For building the web application.
Socket.IO: For real-time communication between the computer and mobile devices.
QRCode Library: To generate QR codes that players can scan.
Setup Instructions
Clone the Repository: Download or clone the repository to your local machine.

bash
Copy code
git clone <repository-url>
Install Dependencies: Navigate to the project folder and install the required packages.

bash
Copy code
pip install -r requirements.txt
Run the Application: Start the Flask application.

bash
Copy code
python app.py
Access the Game:

Open a web browser and go to http://localhost:5000 to see the computer screen.
Scan the QR code with a mobile device to join the game.
