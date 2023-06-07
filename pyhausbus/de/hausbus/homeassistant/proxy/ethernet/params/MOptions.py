import pyhausbus.HausBusUtils as HausBusUtils
class MOptions:

  def setHomeautomationOnlyMode(self, setValue:bool):
    self.value = HausBusUtils.setBit(setValue, 0, self.value)
    return self;

  def isHomeautomationOnlyMode(self):
    return HausBusUtils.isBitSet(0, self.value)
  def setModBusTcp(self, setValue:bool):
    self.value = HausBusUtils.setBit(setValue, 1, self.value)
    return self;

  def isModBusTcp(self):
    return HausBusUtils.isBitSet(1, self.value)
  def setDHCP(self, setValue:bool):
    self.value = HausBusUtils.setBit(setValue, 2, self.value)
    return self;

  def isDHCP(self):
    return HausBusUtils.isBitSet(2, self.value)
  def setSNMP(self, setValue:bool):
    self.value = HausBusUtils.setBit(setValue, 3, self.value)
    return self;

  def isSNMP(self):
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
    return MOptions(HausBusUtils.bytesToInt(data, offset))



  def getValue(self):
    return self.value
  def getEntryNames(self):
    result = []
    result.append("HomeautomationOnlyMode")
    result.append("ModBusTcp")
    result.append("DHCP")
    result.append("SNMP")
    result.append("Reserved1")
    result.append("Reserved2")
    result.append("Reserved3")
    result.append("Reserved4")
    return result
  def setEntry(self,name:str, setValue:bool):
    if (name == "HomeautomationOnlyMode"):
      self.setHomeautomationOnlyMode(setValue)
    if (name == "ModBusTcp"):
      self.setModBusTcp(setValue)
    if (name == "DHCP"):
      self.setDHCP(setValue)
    if (name == "SNMP"):
      self.setSNMP(setValue)
    if (name == "Reserved1"):
      self.setReserved1(setValue)
    if (name == "Reserved2"):
      self.setReserved2(setValue)
    if (name == "Reserved3"):
      self.setReserved3(setValue)
    if (name == "Reserved4"):
      self.setReserved4(setValue)

  def __str__(self):
    return f"MOptions(HomeautomationOnlyMode = {self.isHomeautomationOnlyMode()}, ModBusTcp = {self.isModBusTcp()}, DHCP = {self.isDHCP()}, SNMP = {self.isSNMP()}, Reserved1 = {self.isReserved1()}, Reserved2 = {self.isReserved2()}, Reserved3 = {self.isReserved3()}, Reserved4 = {self.isReserved4()})"



