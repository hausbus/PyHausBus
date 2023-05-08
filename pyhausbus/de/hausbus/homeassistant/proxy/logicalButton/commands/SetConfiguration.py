import pyhausbus.HausBusUtils as HausBusUtils

class SetConfiguration:
  CLASS_ID = 20
  FUNCTION_ID = 1

  def __init__(self,button1:int, button2:int, button3:int, button4:int, button5:int, button6:int, button7:int, button8:int, led1:int, led2:int, led3:int, led4:int, led5:int, led6:int, led7:int, led8:int):
    self.button1=button1
    self.button2=button2
    self.button3=button3
    self.button4=button4
    self.button5=button5
    self.button6=button6
    self.button7=button7
    self.button8=button8
    self.led1=led1
    self.led2=led2
    self.led3=led3
    self.led4=led4
    self.led5=led5
    self.led6=led6
    self.led7=led7
    self.led8=led8


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return SetConfiguration(HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset))

  def __str__(self):
    return f"SetConfiguration(button1={self.button1}, button2={self.button2}, button3={self.button3}, button4={self.button4}, button5={self.button5}, button6={self.button6}, button7={self.button7}, button8={self.button8}, led1={self.led1}, led2={self.led2}, led3={self.led3}, led4={self.led4}, led5={self.led5}, led6={self.led6}, led7={self.led7}, led8={self.led8})"

  '''
  @param button1 instanzId des 1.Tasters.
  '''
  def getButton1(self):
    return self.button1

  '''
  @param button2 instanzId des 2.Tasters.
  '''
  def getButton2(self):
    return self.button2

  '''
  @param button3 .
  '''
  def getButton3(self):
    return self.button3

  '''
  @param button4 .
  '''
  def getButton4(self):
    return self.button4

  '''
  @param button5 .
  '''
  def getButton5(self):
    return self.button5

  '''
  @param button6 .
  '''
  def getButton6(self):
    return self.button6

  '''
  @param button7 .
  '''
  def getButton7(self):
    return self.button7

  '''
  @param button8 .
  '''
  def getButton8(self):
    return self.button8

  '''
  @param led1 .
  '''
  def getLed1(self):
    return self.led1

  '''
  @param led2 .
  '''
  def getLed2(self):
    return self.led2

  '''
  @param led3 .
  '''
  def getLed3(self):
    return self.led3

  '''
  @param led4 .
  '''
  def getLed4(self):
    return self.led4

  '''
  @param led5 .
  '''
  def getLed5(self):
    return self.led5

  '''
  @param led6 .
  '''
  def getLed6(self):
    return self.led6

  '''
  @param led7 .
  '''
  def getLed7(self):
    return self.led7

  '''
  @param led8 .
  '''
  def getLed8(self):
    return self.led8



