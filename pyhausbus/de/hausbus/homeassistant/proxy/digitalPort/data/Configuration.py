from pyhausbus.de.hausbus.homeassistant.proxy.digitalPort.params.EPin import EPin
import pyhausbus.HausBusUtils as HausBusUtils

class Configuration:
  CLASS_ID = 15
  FUNCTION_ID = 128

  def __init__(self,pin0:EPin, pin1:EPin, pin2:EPin, pin3:EPin, pin4:EPin, pin5:EPin, pin6:EPin, pin7:EPin):
    self.pin0=pin0
    self.pin1=pin1
    self.pin2=pin2
    self.pin3=pin3
    self.pin4=pin4
    self.pin5=pin5
    self.pin6=pin6
    self.pin7=pin7


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return Configuration(EPin._fromBytes(dataIn, offset), EPin._fromBytes(dataIn, offset), EPin._fromBytes(dataIn, offset), EPin._fromBytes(dataIn, offset), EPin._fromBytes(dataIn, offset), EPin._fromBytes(dataIn, offset), EPin._fromBytes(dataIn, offset), EPin._fromBytes(dataIn, offset))

def getPin(self, id:int):
  if id==0:
    return pin0
  if id==1:
    return pin1
  if id==2:
    return pin2
  if id==3:
    return pin3
  if id==4:
    return pin4
  if id==5:
    return pin5
  if id==6:
    return pin6
  if id==7:
    return pin7
  return null

def setPin(self, id:int, pin:EPin):
  if id==0:
    pin0 = pin
  if id==1:
    pin1 = pin
  if id==2:
    pin2 = pin
  if id==3:
    pin3 = pin
  if id==4:
    pin4 = pin
  if id==5:
    pin5 = pin
  if id==6:
    pin6 = pin
  if id==7:
    pin7 = pin


  def __str__(self):
    return f"Configuration(pin0={self.pin0}, pin1={self.pin1}, pin2={self.pin2}, pin3={self.pin3}, pin4={self.pin4}, pin5={self.pin5}, pin6={self.pin6}, pin7={self.pin7})"

  '''
  @param pin0 .
  '''
  def getPin0(self):
    return self.pin0

  '''
  @param pin1 .
  '''
  def getPin1(self):
    return self.pin1

  '''
  @param pin2 .
  '''
  def getPin2(self):
    return self.pin2

  '''
  @param pin3 .
  '''
  def getPin3(self):
    return self.pin3

  '''
  @param pin4 .
  '''
  def getPin4(self):
    return self.pin4

  '''
  @param pin5 .
  '''
  def getPin5(self):
    return self.pin5

  '''
  @param pin6 .
  '''
  def getPin6(self):
    return self.pin6

  '''
  @param pin7 .
  '''
  def getPin7(self):
    return self.pin7



