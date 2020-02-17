from flask import Flask, render_template
import socket
import platform
from datetime import datetime

app = Flask(__name__)
# client = docker.from_env()
# container_list = client.containers.list()
host_name = socket.gethostname() 
host_ip = socket.gethostbyname(host_name)
now = datetime. now() 
os_name = platform.system()
os_version = platform.release()
current_time = now.strftime("%d/%m/%Y %H:%M:%S")

@app.route("/")
def hello():
    return render_template('index.html', host_name=host_name, host_ip=host_ip, os_name=os_name, \
        os_version=os_version)

if __name__ == "__main__":      #means this current file. In this case, it will be app.py. This current file will represent my web application.
    #app.run(debug=True,host='0.0.0.0')
    app.run(port=5000)