from smartcard.System import readers
from smartcard.util import toHexString, toBytes

r = readers()
print("Available readers:", r)

connection = r[0].createConnection()
connection.connect()

print("Selecting ICCID File")
data, sw1, sw2 = connection.transmit(toBytes('00a40004022fe2'))
print("Returned data: " + str(data))
print("Returned Status Word 1: " + toHexString([sw1]))
print("Returned Status Word 2: " + toHexString([sw2]))

print("Reading ICCID")
data, sw1, sw2 = connection.transmit(toBytes('00b000000A'))
print("Returned data: " + str(data))
print("Returned Status Word 1: " + toHexString([sw1]))
print("Returned Status Word 2: " + toHexString([sw2]))