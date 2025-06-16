import pyhausbus.HausBusUtils as HausBusUtils

class EvZeroCrossData:
  CLASS_ID = 0
  FUNCTION_ID = 209

  def __init__(self,channel:int, pulseCount:int, deltaTime:int, lowTime0:int, lowTime1:int, lowTime2:int, lowTime3:int, lowTime4:int, lowTime5:int, lowTime6:int, lowTime7:int, lowTime8:int, lowTime9:int, lowTime10:int, lowTime11:int, lowTime12:int, lowTime13:int, lowTime14:int, lowTime15:int, pulsWidth0:int, pulsWidth1:int, pulsWidth2:int, pulsWidth3:int, pulsWidth4:int, pulsWidth5:int, pulsWidth6:int, pulsWidth7:int, pulsWidth8:int, pulsWidth9:int, pulsWidth10:int, pulsWidth11:int, pulsWidth12:int, pulsWidth13:int, pulsWidth14:int, pulsWidth15:int):
    self.channel=channel
    self.pulseCount=pulseCount
    self.deltaTime=deltaTime
    self.lowTime0=lowTime0
    self.lowTime1=lowTime1
    self.lowTime2=lowTime2
    self.lowTime3=lowTime3
    self.lowTime4=lowTime4
    self.lowTime5=lowTime5
    self.lowTime6=lowTime6
    self.lowTime7=lowTime7
    self.lowTime8=lowTime8
    self.lowTime9=lowTime9
    self.lowTime10=lowTime10
    self.lowTime11=lowTime11
    self.lowTime12=lowTime12
    self.lowTime13=lowTime13
    self.lowTime14=lowTime14
    self.lowTime15=lowTime15
    self.pulsWidth0=pulsWidth0
    self.pulsWidth1=pulsWidth1
    self.pulsWidth2=pulsWidth2
    self.pulsWidth3=pulsWidth3
    self.pulsWidth4=pulsWidth4
    self.pulsWidth5=pulsWidth5
    self.pulsWidth6=pulsWidth6
    self.pulsWidth7=pulsWidth7
    self.pulsWidth8=pulsWidth8
    self.pulsWidth9=pulsWidth9
    self.pulsWidth10=pulsWidth10
    self.pulsWidth11=pulsWidth11
    self.pulsWidth12=pulsWidth12
    self.pulsWidth13=pulsWidth13
    self.pulsWidth14=pulsWidth14
    self.pulsWidth15=pulsWidth15


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return EvZeroCrossData(HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset))

  def __str__(self):
    return f"EvZeroCrossData(channel={self.channel}, pulseCount={self.pulseCount}, deltaTime={self.deltaTime}, lowTime0={self.lowTime0}, lowTime1={self.lowTime1}, lowTime2={self.lowTime2}, lowTime3={self.lowTime3}, lowTime4={self.lowTime4}, lowTime5={self.lowTime5}, lowTime6={self.lowTime6}, lowTime7={self.lowTime7}, lowTime8={self.lowTime8}, lowTime9={self.lowTime9}, lowTime10={self.lowTime10}, lowTime11={self.lowTime11}, lowTime12={self.lowTime12}, lowTime13={self.lowTime13}, lowTime14={self.lowTime14}, lowTime15={self.lowTime15}, pulsWidth0={self.pulsWidth0}, pulsWidth1={self.pulsWidth1}, pulsWidth2={self.pulsWidth2}, pulsWidth3={self.pulsWidth3}, pulsWidth4={self.pulsWidth4}, pulsWidth5={self.pulsWidth5}, pulsWidth6={self.pulsWidth6}, pulsWidth7={self.pulsWidth7}, pulsWidth8={self.pulsWidth8}, pulsWidth9={self.pulsWidth9}, pulsWidth10={self.pulsWidth10}, pulsWidth11={self.pulsWidth11}, pulsWidth12={self.pulsWidth12}, pulsWidth13={self.pulsWidth13}, pulsWidth14={self.pulsWidth14}, pulsWidth15={self.pulsWidth15})"

  '''
  @param channel PWM-Kanal.
  '''
  def getChannel(self):
    return self.channel

  '''
  @param pulseCount Anzahl der guten Pulse innerhalb der letzten Messperiode 1s.
  '''
  def getPulseCount(self):
    return self.pulseCount

  '''
  @param deltaTime Falls Messperiode l?nger als 1s ist.
  '''
  def getDeltaTime(self):
    return self.deltaTime

  '''
  @param lowTime0 .
  '''
  def getLowTime0(self):
    return self.lowTime0

  '''
  @param lowTime1 .
  '''
  def getLowTime1(self):
    return self.lowTime1

  '''
  @param lowTime2 .
  '''
  def getLowTime2(self):
    return self.lowTime2

  '''
  @param lowTime3 .
  '''
  def getLowTime3(self):
    return self.lowTime3

  '''
  @param lowTime4 .
  '''
  def getLowTime4(self):
    return self.lowTime4

  '''
  @param lowTime5 .
  '''
  def getLowTime5(self):
    return self.lowTime5

  '''
  @param lowTime6 .
  '''
  def getLowTime6(self):
    return self.lowTime6

  '''
  @param lowTime7 .
  '''
  def getLowTime7(self):
    return self.lowTime7

  '''
  @param lowTime8 .
  '''
  def getLowTime8(self):
    return self.lowTime8

  '''
  @param lowTime9 .
  '''
  def getLowTime9(self):
    return self.lowTime9

  '''
  @param lowTime10 .
  '''
  def getLowTime10(self):
    return self.lowTime10

  '''
  @param lowTime11 .
  '''
  def getLowTime11(self):
    return self.lowTime11

  '''
  @param lowTime12 .
  '''
  def getLowTime12(self):
    return self.lowTime12

  '''
  @param lowTime13 .
  '''
  def getLowTime13(self):
    return self.lowTime13

  '''
  @param lowTime14 .
  '''
  def getLowTime14(self):
    return self.lowTime14

  '''
  @param lowTime15 .
  '''
  def getLowTime15(self):
    return self.lowTime15

  '''
  @param pulsWidth0 .
  '''
  def getPulsWidth0(self):
    return self.pulsWidth0

  '''
  @param pulsWidth1 .
  '''
  def getPulsWidth1(self):
    return self.pulsWidth1

  '''
  @param pulsWidth2 .
  '''
  def getPulsWidth2(self):
    return self.pulsWidth2

  '''
  @param pulsWidth3 .
  '''
  def getPulsWidth3(self):
    return self.pulsWidth3

  '''
  @param pulsWidth4 .
  '''
  def getPulsWidth4(self):
    return self.pulsWidth4

  '''
  @param pulsWidth5 .
  '''
  def getPulsWidth5(self):
    return self.pulsWidth5

  '''
  @param pulsWidth6 .
  '''
  def getPulsWidth6(self):
    return self.pulsWidth6

  '''
  @param pulsWidth7 .
  '''
  def getPulsWidth7(self):
    return self.pulsWidth7

  '''
  @param pulsWidth8 .
  '''
  def getPulsWidth8(self):
    return self.pulsWidth8

  '''
  @param pulsWidth9 .
  '''
  def getPulsWidth9(self):
    return self.pulsWidth9

  '''
  @param pulsWidth10 .
  '''
  def getPulsWidth10(self):
    return self.pulsWidth10

  '''
  @param pulsWidth11 .
  '''
  def getPulsWidth11(self):
    return self.pulsWidth11

  '''
  @param pulsWidth12 .
  '''
  def getPulsWidth12(self):
    return self.pulsWidth12

  '''
  @param pulsWidth13 .
  '''
  def getPulsWidth13(self):
    return self.pulsWidth13

  '''
  @param pulsWidth14 .
  '''
  def getPulsWidth14(self):
    return self.pulsWidth14

  '''
  @param pulsWidth15 .
  '''
  def getPulsWidth15(self):
    return self.pulsWidth15



