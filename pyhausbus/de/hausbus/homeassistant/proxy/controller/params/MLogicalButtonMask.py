import pyhausbus.HausBusUtils as HausBusUtils
class MLogicalButtonMask:

  def setLogicalButton0(self, setValue:bool):
    self.value = HausBusUtils.setBit(setValue, 0, self.value)
    return self;

  def isLogicalButton0(self):
    return HausBusUtils.isBitSet(0, self.value)
  def setLogicalButton1(self, setValue:bool):
    self.value = HausBusUtils.setBit(setValue, 1, self.value)
    return self;

  def isLogicalButton1(self):
    return HausBusUtils.isBitSet(1, self.value)
  def setLogicalButton2(self, setValue:bool):
    self.value = HausBusUtils.setBit(setValue, 2, self.value)
    return self;

  def isLogicalButton2(self):
    return HausBusUtils.isBitSet(2, self.value)
  def setLogicalButton3(self, setValue:bool):
    self.value = HausBusUtils.setBit(setValue, 3, self.value)
    return self;

  def isLogicalButton3(self):
    return HausBusUtils.isBitSet(3, self.value)
  def setLogicalButton4(self, setValue:bool):
    self.value = HausBusUtils.setBit(setValue, 4, self.value)
    return self;

  def isLogicalButton4(self):
    return HausBusUtils.isBitSet(4, self.value)
  def setLogicalButton5(self, setValue:bool):
    self.value = HausBusUtils.setBit(setValue, 5, self.value)
    return self;

  def isLogicalButton5(self):
    return HausBusUtils.isBitSet(5, self.value)
  def setLogicalButton6(self, setValue:bool):
    self.value = HausBusUtils.setBit(setValue, 6, self.value)
    return self;

  def isLogicalButton6(self):
    return HausBusUtils.isBitSet(6, self.value)
  def setLogicalButton7(self, setValue:bool):
    self.value = HausBusUtils.setBit(setValue, 7, self.value)
    return self;

  def isLogicalButton7(self):
    return HausBusUtils.isBitSet(7, self.value)
  def __init__(self, value:int):
    self.value = value

  @staticmethod
  def _fromBytes(data:bytearray, offset):
    return MLogicalButtonMask(HausBusUtils.bytesToInt(data, offset))



  def getValue(self):
    return self.value
  def getEntryNames(self):
    result = []
    result.append("LogicalButton0")
    result.append("LogicalButton1")
    result.append("LogicalButton2")
    result.append("LogicalButton3")
    result.append("LogicalButton4")
    result.append("LogicalButton5")
    result.append("LogicalButton6")
    result.append("LogicalButton7")
    return result
  def setEntry(self,name:str, setValue:bool):
    if (name == "LogicalButton0"):
      self.setLogicalButton0(setValue)
    if (name == "LogicalButton1"):
      self.setLogicalButton1(setValue)
    if (name == "LogicalButton2"):
      self.setLogicalButton2(setValue)
    if (name == "LogicalButton3"):
      self.setLogicalButton3(setValue)
    if (name == "LogicalButton4"):
      self.setLogicalButton4(setValue)
    if (name == "LogicalButton5"):
      self.setLogicalButton5(setValue)
    if (name == "LogicalButton6"):
      self.setLogicalButton6(setValue)
    if (name == "LogicalButton7"):
      self.setLogicalButton7(setValue)

  def __str__(self):
    return f"MLogicalButtonMask(LogicalButton0 = {self.isLogicalButton0()}, LogicalButton1 = {self.isLogicalButton1()}, LogicalButton2 = {self.isLogicalButton2()}, LogicalButton3 = {self.isLogicalButton3()}, LogicalButton4 = {self.isLogicalButton4()}, LogicalButton5 = {self.isLogicalButton5()}, LogicalButton6 = {self.isLogicalButton6()}, LogicalButton7 = {self.isLogicalButton7()})"



