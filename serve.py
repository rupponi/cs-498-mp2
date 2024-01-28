from flask import Flask
import subprocess
import socket

app = Flask(__name__)

@app.route('/', methods = ['POST'])
def run_stress_test():
    subprocess.Popen(['python3','stress_cpu.py'],stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    return "Created new stress process"

@app.route('/', methods = ['GET'])
def get_ip():
    return str(socket.gethostname())

if __name__ == '__main__':
    app.run(host="0.0.0.0")