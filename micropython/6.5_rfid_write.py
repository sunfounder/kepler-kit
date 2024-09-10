from mfrc522 import SimpleMFRC522

reader = SimpleMFRC522(spi_id=0,sck=18,miso=16,mosi=19,cs=17,rst=9)

def write():
    to_write = input("Please enter the message: ")
    print("Writing...Please place the card...")
    id, text = reader.write(to_write)
    print("ID: %s\nText: %s" % (id,text))

write()