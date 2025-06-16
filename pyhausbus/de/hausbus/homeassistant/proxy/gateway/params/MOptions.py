import pyhausbus.HausBusUtils as HausBusUtils
class MOptions:

  def setEnabled(self, setValue:bool):
    self.value = HausBusUtils.setBit(setValue, 0, self.value)
    return self;

  def isEnabled(self):
    return HausBusUtils.isBitSet(0, self.value)
  def setPreferLoxone(self, setValue:bool):
    self.value = HausBusUtils.setBit(setValue, 1, self.value)
    return self;

  def isPreferLoxone(self):
    return HausBusUtils.isBitSet(1, self.value)
  def setEnableConsole(self, setValue:bool):
    self.value = HausBusUtils.setBit(setValue, 2, self.value)
    return self;

  def isEnableConsole(self):
    return HausBusUtils.isBitSet(2, self.value)
  def setMaster(self, setValue:bool):
    self.value = HausBusUtils.setBit(setValue, 3, self.value)
    return self;

  def isMaster(self):
    return HausBusUtils.isBitSet(3, self.value)
  def setReserved4(self, setValue:bool):
    self.value = HausBusUtils.setBit(setValue, 4, self.value)
    return self;

  def isReserved4(self):
    return HausBusUtils.isBitSet(4, self.value)
  def setReserved5(self, setValue:bool):
    self.value = HausBusUtils.setBit(setValue, 5, self.value)
    return self;

  def isReserved5(self):
    return HausBusUtils.isBitSet(5, self.value)
  def setReserved6(self, setValue:bool):
    self.value = HausBusUtils.setBit(setValue, 6, self.value)
    return self;

  def isReserved6(self):
    return HausBusUtils.isBitSet(6, self.value)
  def setReserved7(self, setValue:bool):
    self.value = HausBusUtils.setBit(setValue, 7, self.value)
    return self;

  def isReserved7(self):
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
    result.append("Enabled")
    result.append("PreferLoxone")
    result.append("EnableConsole")
    result.append("Master")
    result.append("Reserved4")
    result.append("Reserved5")
    result.append("Reserved6")
    result.append("Reserved7")
    return result
  def setEntry(self,name:str, setValue:bool):
    if (name == "Enabled"):
      self.setEnabled(setValue)
    if (name == "PreferLoxone"):
      self.setPreferLoxone(setValue)
    if (name == "EnableConsole"):
      self.setEnableConsole(setValue)
    if (name == "Master"):
      self.setMaster(setValue)
    if (name == "Reserved4"):
      self.setReserved4(setValue)
    if (name == "Reserved5"):
      self.setReserved5(setValue)
    if (name == "Reserved6"):
      self.setReserved6(setValue)
    if (name == "Reserved7"):
      self.setReserved7(setValue)

  def __str__(self):
    return f"MOptions(Enabled = {self.isEnabled()}, PreferLoxone = {self.isPreferLoxone()}, EnableConsole = {self.isEnableConsole()}, Master = {self.isMaster()}, Reserved4 = {self.isReserved4()}, Reserved5 = {self.isReserved5()}, Reserved6 = {self.isReserved6()}, Reserved7 = {self.isReserved7()})"



