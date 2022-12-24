from flask import Flask, jsonify, request, send_from_directory, render_template, redirect,flash,url_for
from pymodbus.client.sync import ModbusSerialClient
import serial.tools.list_ports

def create_app():
    app = Flask(__name__)
    app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

    # Home page route
    @app.route('/')
    def index():
        myports = []
        flag = False
        ports = serial.tools.list_ports.comports()
        for port, desc, hwid in sorted(ports):
            myports.append(port)
        if(len(myports)<=0):
            flag=False
        else:
            flag=True
        return render_template('index.html',length=len(myports),myports=myports,flag=flag)

    @app.route('/connect',methods=['post'])
    def connect():
        client= ModbusSerialClient(method="rtu",port="COM2",stopbits=1,bytesize=8,parity='N',baudrate=9600)
        res = client.connect()
        print(res)
        flash(res)
        client.close()
        return redirect(url_for('index'))
    #running application 
    app.run()
if __name__=="__main__":
    app = create_app()

