# This module should be imported from REPL, not run from command line.
import socket
import uos
import network
import uwebsocket
import websocket_helper
import time
import json

NAME = 'PicoW'
AP_PASSWORD = "123456789"
STA_NAME = "MakerStarsHall"
STA_PASSWORD = "sunfounder" 
SWITCH_MODE = "sta" # Change the values to "ap" or "sta" to select the operating mode


class WS_Server():
    
    # read -- <function>
    # readinto -- <function>
    # readline -- <function>
    # write -- <function>
    # ioctl -- <function>
    # close -- <function>
    send_dict = {
        'Name':NAME,
        'Type':'Blank',
        'Check':'SunFounder Controller',
        }

    def __init__(self, port):
        self.port = port
        self.listen_s = None
        self.client_s = None
        self.ws = None
        self.wlan = None
    
    def setup_conn(self, accept_handler):
        self.listen_s = socket.socket()
        self.listen_s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        ai = socket.getaddrinfo("0.0.0.0", self.port)
        addr = ai[0][4]

        self.listen_s.bind(addr)
        self.listen_s.listen(5)
        if accept_handler:
            self.listen_s.setsockopt(socket.SOL_SOCKET, 20, accept_handler)
        for i in (network.AP_IF, network.STA_IF):
            iface = network.WLAN(i)
            if iface.active():
                print("WebServer started on ws://%s:%d" % (iface.ifconfig()[0], self.port))
        return self.listen_s

    def accept_conn(self, listen_sock):
        cl, remote_addr = listen_sock.accept()
        print("\nWebSocket connection from:", remote_addr)
        self.client_s = cl
        websocket_helper.server_handshake(cl)
        self.ws = uwebsocket.websocket(cl, True)
        self.ws.write(json.dumps(self.send_dict))
        print("have sended!")
        cl.setblocking(False)

    def read(self):
        if self.ws == None:
            return None
        recv = self.ws.read()
        if recv != None and recv != b"":
            recv = recv.decode()
            # print("accept_conn: %s" % recv)
            try:
                recv=json.loads(recv)
                return recv
            except ValueError:
                pass
        return None

    def transfer(self):
        result = self.read()
        if result != None:
            status = True
            self.write()
        else:
            status = False    
        return status,result

    def write(self):
        try:
            value=json.dumps(self.send_dict)
            value = value.encode(value)
            self.ws.write(value)
        except AttributeError:
            pass
            

    def stop(self):
        if self.client_s:
            self.client_s.close()
        if self.listen_s:
            self.listen_s.close()
        self.wlan.active(False)

    def start(self):
        # self.stop()
        if SWITCH_MODE == "ap":
            self.wlan = network.WLAN(network.AP_IF)
            #self.wlan.config(essid=NAME, authmode=4, password=AP_PASSWORD)
            self.wlan.config(essid=NAME, password=AP_PASSWORD)
            self.wlan.active(True)  # turning on the hotspot
        elif SWITCH_MODE == "sta":
            self.wlan = network.WLAN(network.STA_IF)
            self.wlan.active(True)
            self.wlan.connect(STA_NAME, STA_PASSWORD)
            for _ in range(5):
                if self.wlan.isconnected():
                    print('network config:', self.wlan.ifconfig())
                    break
                time.sleep(1)
            if not self.wlan.isconnected():
                print("wifi connected fail ")
        self.setup_conn(self.accept_conn)

    def start_foreground(self):
        self.stop()
        s = self.setup_conn(None)
        self.accept_conn(s)
