import pyhausbus.HausBusUtils as HausBusUtils
class MOption:

  def setSEND_TRIGGERED_RULE_EVENT(self, setValue:bool):
    self.value = HausBusUtils.setBit(setValue, 0, self.value)
    return self;

  def isSEND_TRIGGERED_RULE_EVENT(self):
    return HausBusUtils.isBitSet(0, self.value)
  def setREAD_ONLY_GATEWAYS(self, setValue:bool):
    self.value = HausBusUtils.setBit(setValue, 1, self.value)
    return self;

  def isREAD_ONLY_GATEWAYS(self):
    return HausBusUtils.isBitSet(1, self.value)
  def setREPORT_GATEWAY_LOAD(self, setValue:bool):
    self.value = HausBusUtils.setBit(setValue, 2, self.value)
    return self;

  def isREPORT_GATEWAY_LOAD(self):
    return HausBusUtils.isBitSet(2, self.value)
  def setREPORT_INTERNAL_TEMPERATURE(self, setValue:bool):
    self.value = HausBusUtils.setBit(setValue, 3, self.value)
    return self;

  def isREPORT_INTERNAL_TEMPERATURE(self):
    return HausBusUtils.isBitSet(3, self.value)
  def setSEND_ZERO_CROSS_DATA(self, setValue:bool):
    self.value = HausBusUtils.setBit(setValue, 4, self.value)
    return self;

  def isSEND_ZERO_CROSS_DATA(self):
    return HausBusUtils.isBitSet(4, self.value)
  def setReserved1(self, setValue:bool):
    self.value = HausBusUtils.setBit(setValue, 5, self.value)
    return self;

  def isReserved1(self):
    return HausBusUtils.isBitSet(5, self.value)
  def setReserved2(self, setValue:bool):
    self.value = HausBusUtils.setBit(setValue, 6, self.value)
    return self;

  def isReserved2(self):
    return HausBusUtils.isBitSet(6, self.value)
  def setReserved3(self, setValue:bool):
    self.value = HausBusUtils.setBit(setValue, 7, self.value)
    return self;

  def isReserved3(self):
    return HausBusUtils.isBitSet(7, self.value)
  def __init__(self, value:int):
    self.value = value

  @staticmethod
  def _fromBytes(data:bytearray, offset):
    return MOption(HausBusUtils.bytesToInt(data, offset))



  def getValue(self):
    return self.value
  def getEntryNames(self):
    result = []
    result.append("SEND_TRIGGERED_RULE_EVENT")
    result.append("READ_ONLY_GATEWAYS")
    result.append("REPORT_GATEWAY_LOAD")
    result.append("REPORT_INTERNAL_TEMPERATURE")
    result.append("SEND_ZERO_CROSS_DATA")
    result.append("Reserved1")
    result.append("Reserved2")
    result.append("Reserved3")
    return result
  def setEntry(self,name:str, setValue:bool):
    if (name == "SEND_TRIGGERED_RULE_EVENT"):
      self.setSEND_TRIGGERED_RULE_EVENT(setValue)
    if (name == "READ_ONLY_GATEWAYS"):
      self.setREAD_ONLY_GATEWAYS(setValue)
    if (name == "REPORT_GATEWAY_LOAD"):
      self.setREPORT_GATEWAY_LOAD(setValue)
    if (name == "REPORT_INTERNAL_TEMPERATURE"):
      self.setREPORT_INTERNAL_TEMPERATURE(setValue)
    if (name == "SEND_ZERO_CROSS_DATA"):
      self.setSEND_ZERO_CROSS_DATA(setValue)
    if (name == "Reserved1"):
      self.setReserved1(setValue)
    if (name == "Reserved2"):
      self.setReserved2(setValue)
    if (name == "Reserved3"):
      self.setReserved3(setValue)

  def __str__(self):
    return f"MOption(SEND_TRIGGERED_RULE_EVENT = {self.isSEND_TRIGGERED_RULE_EVENT()}, READ_ONLY_GATEWAYS = {self.isREAD_ONLY_GATEWAYS()}, REPORT_GATEWAY_LOAD = {self.isREPORT_GATEWAY_LOAD()}, REPORT_INTERNAL_TEMPERATURE = {self.isREPORT_INTERNAL_TEMPERATURE()}, SEND_ZERO_CROSS_DATA = {self.isSEND_ZERO_CROSS_DATA()}, Reserved1 = {self.isReserved1()}, Reserved2 = {self.isReserved2()}, Reserved3 = {self.isReserved3()})"



