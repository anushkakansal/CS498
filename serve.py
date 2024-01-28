from flask import Flask, request
import subprocess
import socket

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def handle_request():
    if request.method == "POST":
        # Handling POST request
        start_cpu_stress()
        return "Stressing CPU..."

    elif request.method == "GET":
        # Handling GET request
        private_ip = get_private_ip()
        return private_ip

def start_cpu_stress():
    # Run "stress_cpu.py" in a separate process
    subprocess.Popen(["python3", "stress_cpu.py"])

def get_private_ip():
    # Get the private IP address of the EC2 instance
    private_ip = socket.gethostbyname(socket.gethostname())
    return private_ip

if __name__ == "__main__":
    # Run the Flask app on port 5000 (you can change it as needed)
    app.run(host="0.0.0.0", port=5000)
