# inspired by https://github.com/pimylifeup/MFRC522-python/blob/master/mfrc522/SimpleMFRC522.py

from .mfrc522 import MFRC522

def uidToString(uid):
    mystring = ""
    for i in uid:
        mystring = "%02X" % i + mystring
    return mystring

class SimpleMFRC522:

  KEY = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]
  BLOCK_ADDRS = [8, 9, 10]
  
  def __init__(self, spi_id=0, sck=2, miso=4, mosi=3, cs=5, rst=0):
    self.reader = MFRC522(spi_id=spi_id, sck=sck, miso=miso, mosi=mosi, cs=cs, rst=rst)
  
  def read(self):
      id, text = self.read_no_block()
      while not id:
          id, text = self.read_no_block()
      return id, text

  def read_id(self):
    id = self.read_id_no_block()
    while not id:
      id = self.read_id_no_block()
    return id

  def read_id_no_block(self):
      self.reader.init()
      (status, tag_type) = self.reader.request(self.reader.REQIDL)
      if status != self.reader.OK:
          return None
      (status, uid) = self.reader.anticoll(self.reader.PICC_ANTICOLL1)
      if status != self.reader.OK:
          return None
      return self.uid_to_num(uid)
  
  def read_no_block(self):
    id = None
    text_read = ""
    self.reader.init()
    (stat, tag_type) = self.reader.request(self.reader.REQIDL)
    if stat != self.reader.OK:
        return None, None
    (stat, uid) = self.reader.SelectTagSN()
    if stat != self.reader.OK:
        return None, None
    id = uidToString(uid)
    for absoluteBlock in self.BLOCK_ADDRS:
        status = self.reader.authKeys(uid,absoluteBlock,self.KEY, None)
        if status != self.reader.OK:
            print("Authentication error")
            return None, None
        status, block = self.reader.read(absoluteBlock)
        if status == self.reader.ERR:
            print("Error reading block %i" % absoluteBlock)
            break
        for value in block:
            text_read += chr(value)
    return id, text_read
    
  def write(self, text):
      id, text_in = self.write_no_block(text)
      while not id:
          id, text_in = self.write_no_block(text)
      return id, text_in

  def write_no_block(self, text):
        self.reader.init()
        (status, tag_type) = self.reader.request(self.reader.REQIDL)
        if status != self.reader.OK:
            return None, None
        (status, uid) = self.reader.SelectTagSN()
        if status != self.reader.OK:
            return None, None
        id = uidToString(uid)
        print("Card detected %s" % id)
    
        data = bytearray()
        for i in range(len(text), len(self.BLOCK_ADDRS) * 16):
            text += " "
        data.extend(bytearray(text.encode('ascii')))
        i = 0
        for block_num in self.BLOCK_ADDRS:
            status = self.reader.auth(self.reader.AUTHENT1A, 11, self.KEY, uid)
            if status != self.reader.OK:
                print("Authentication error")
                return None, None
            self.reader.write(block_num, data[(i*16):(i+1)*16])
            i += 1
        self.reader.stop_crypto1()
        return id, text[0:(len(self.BLOCK_ADDRS) * 16)]
      
  def uid_to_num(self, uid):
      n = 0
      for i in range(0, 5):
          n = n * 256 + uid[i]
      return n
