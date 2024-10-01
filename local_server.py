import sys
from PySide6.QtNetwork import QUdpSocket, QHostAddress
from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QWidget

class MulticastSender(QWidget):
    def __init__(self):
        super().__init__()

        # Set up the GUI
        self.send_button = QPushButton("Send Multicast Message")
        layout = QVBoxLayout()
        layout.addWidget(self.send_button)
        self.setLayout(layout)

        # Create a QUdpSocket
        self.udp_socket = QUdpSocket(self)
        
        # Define the multicast group address and port
        self.multicast_group = QHostAddress("239.255.255.250")  # Example multicast address
        self.port = 60000

        # Connect the button to the send function
        self.send_button.clicked.connect(self.sendMulticastMessage)

    def sendMulticastMessage(self):
        # Define the message to be sent
        message = "Hello from the multicast sender!"

        # Convert the message to bytes and send it to the multicast group
        self.udp_socket.writeDatagram(message.encode(), self.multicast_group, self.port)
        print(f"Sent message to multicast group {self.multicast_group.toString()} on port {self.port}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    sender = MulticastSender()
    sender.setWindowTitle("Multicast Sender")
    sender.resize(300, 100)
    sender.show()
    
    sys.exit(app.exec())
