import pyhausbus.HausBusUtils as HausBusUtils
class MOptions:

  def setInvertDirection(self, setValue:bool):
    self.value = HausBusUtils.setBit(setValue, 0, self.value)
    return self;

  def isInvertDirection(self):
    return HausBusUtils.isBitSet(0, self.value)
  def setIndependent(self, setValue:bool):
    self.value = HausBusUtils.setBit(setValue, 1, self.value)
    return self;

  def isIndependent(self):
    return HausBusUtils.isBitSet(1, self.value)
  def setInvertOutputs(self, setValue:bool):
    self.value = HausBusUtils.setBit(setValue, 2, self.value)
    return self;

  def isInvertOutputs(self):
    return HausBusUtils.isBitSet(2, self.value)
  def setSoftStartDCMotor(self, setValue:bool):
    self.value = HausBusUtils.setBit(setValue, 3, self.value)
    return self;

  def isSoftStartDCMotor(self):
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
  def setEnableTracing(self, setValue:bool):
    self.value = HausBusUtils.setBit(setValue, 7, self.value)
    return self;

  def isEnableTracing(self):
    return HausBusUtils.isBitSet(7, self.value)
  def __init__(self, value:int):
    self.value = value

  @staticmethod
  def _fromBytes(data:bytearray, offset):
    return MOptions(HausBusUtils.bytesToInt(data, offset))



  def getValue(self):
    return self.value
  def getEntryNames(self):
    result = []
    result.append("InvertDirection")
    result.append("Independent")
    result.append("InvertOutputs")
    result.append("SoftStartDCMotor")
    result.append("Reserved1")
    result.append("Reserved2")
    result.append("Reserved3")
    result.append("EnableTracing")
    return result
  def setEntry(self,name:str, setValue:bool):
    if (name == "InvertDirection"):
      self.setInvertDirection(setValue)
    if (name == "Independent"):
      self.setIndependent(setValue)
    if (name == "InvertOutputs"):
      self.setInvertOutputs(setValue)
    if (name == "SoftStartDCMotor"):
      self.setSoftStartDCMotor(setValue)
    if (name == "Reserved1"):
      self.setReserved1(setValue)
    if (name == "Reserved2"):
      self.setReserved2(setValue)
    if (name == "Reserved3"):
      self.setReserved3(setValue)
    if (name == "EnableTracing"):
      self.setEnableTracing(setValue)

  def __str__(self):
    return f"MOptions(InvertDirection = {self.isInvertDirection()}, Independent = {self.isIndependent()}, InvertOutputs = {self.isInvertOutputs()}, SoftStartDCMotor = {self.isSoftStartDCMotor()}, Reserved1 = {self.isReserved1()}, Reserved2 = {self.isReserved2()}, Reserved3 = {self.isReserved3()}, EnableTracing = {self.isEnableTracing()})"



