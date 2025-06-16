import pyhausbus.HausBusUtils as HausBusUtils
class MMode:

  def setIncrement(self, setValue:bool):
    self.value = HausBusUtils.setBit(setValue, 0, self.value)
    return self;

  def isIncrement(self):
    return HausBusUtils.isBitSet(0, self.value)
  def setFallingEdge(self, setValue:bool):
    self.value = HausBusUtils.setBit(setValue, 1, self.value)
    return self;

  def isFallingEdge(self):
    return HausBusUtils.isBitSet(1, self.value)
  def setRisingEdge(self, setValue:bool):
    self.value = HausBusUtils.setBit(setValue, 2, self.value)
    return self;

  def isRisingEdge(self):
    return HausBusUtils.isBitSet(2, self.value)
  def setActiveLow(self, setValue:bool):
    self.value = HausBusUtils.setBit(setValue, 3, self.value)
    return self;

  def isActiveLow(self):
    return HausBusUtils.isBitSet(3, self.value)
  def setReserved1(self, setValue:bool):
    self.value = HausBusUtils.setBit(setValue, 4, self.value)
    return self;

  def isReserved1(self):
    return HausBusUtils.isBitSet(4, self.value)
  def setReserved2(self, setValue:bool):
    self.value = HausBusUtils.setBit(setValue, 5, self.value)
    return self;

  def isReserved2(self):
    return HausBusUtils.isBitSet(5, self.value)
  def setReserved3(self, setValue:bool):
    self.value = HausBusUtils.setBit(setValue, 6, self.value)
    return self;

  def isReserved3(self):
    return HausBusUtils.isBitSet(6, self.value)
  def setReserved4(self, setValue:bool):
    self.value = HausBusUtils.setBit(setValue, 7, self.value)
    return self;

  def isReserved4(self):
    return HausBusUtils.isBitSet(7, self.value)
  def __init__(self, value:int):
    self.value = value

  @staticmethod
  def _fromBytes(data:bytearray, offset):
    return MMode(HausBusUtils.bytesToInt(data, offset))



  def getValue(self):
    return self.value
  def getEntryNames(self):
    result = []
    result.append("Increment")
    result.append("FallingEdge")
    result.append("RisingEdge")
    result.append("ActiveLow")
    result.append("Reserved1")
    result.append("Reserved2")
    result.append("Reserved3")
    result.append("Reserved4")
    return result
  def setEntry(self,name:str, setValue:bool):
    if (name == "Increment"):
      self.setIncrement(setValue)
    if (name == "FallingEdge"):
      self.setFallingEdge(setValue)
    if (name == "RisingEdge"):
      self.setRisingEdge(setValue)
    if (name == "ActiveLow"):
      self.setActiveLow(setValue)
    if (name == "Reserved1"):
      self.setReserved1(setValue)
    if (name == "Reserved2"):
      self.setReserved2(setValue)
    if (name == "Reserved3"):
      self.setReserved3(setValue)
    if (name == "Reserved4"):
      self.setReserved4(setValue)

  def __str__(self):
    return f"MMode(Increment = {self.isIncrement()}, FallingEdge = {self.isFallingEdge()}, RisingEdge = {self.isRisingEdge()}, ActiveLow = {self.isActiveLow()}, Reserved1 = {self.isReserved1()}, Reserved2 = {self.isReserved2()}, Reserved3 = {self.isReserved3()}, Reserved4 = {self.isReserved4()})"



