import pyhausbus.HausBusUtils as HausBusUtils
class MGroupMask:

  def setGruppe1(self, setValue:bool):
    self.value = HausBusUtils.setBit(setValue, 0, self.value)
    return self;

  def isGruppe1(self):
    return HausBusUtils.isBitSet(0, self.value)
  def setGruppe2(self, setValue:bool):
    self.value = HausBusUtils.setBit(setValue, 1, self.value)
    return self;

  def isGruppe2(self):
    return HausBusUtils.isBitSet(1, self.value)
  def setGruppe3(self, setValue:bool):
    self.value = HausBusUtils.setBit(setValue, 2, self.value)
    return self;

  def isGruppe3(self):
    return HausBusUtils.isBitSet(2, self.value)
  def setGruppe4(self, setValue:bool):
    self.value = HausBusUtils.setBit(setValue, 3, self.value)
    return self;

  def isGruppe4(self):
    return HausBusUtils.isBitSet(3, self.value)
  def setGruppe5(self, setValue:bool):
    self.value = HausBusUtils.setBit(setValue, 4, self.value)
    return self;

  def isGruppe5(self):
    return HausBusUtils.isBitSet(4, self.value)
  def setGruppe6(self, setValue:bool):
    self.value = HausBusUtils.setBit(setValue, 5, self.value)
    return self;

  def isGruppe6(self):
    return HausBusUtils.isBitSet(5, self.value)
  def setGruppe7(self, setValue:bool):
    self.value = HausBusUtils.setBit(setValue, 6, self.value)
    return self;

  def isGruppe7(self):
    return HausBusUtils.isBitSet(6, self.value)
  def setGruppe8(self, setValue:bool):
    self.value = HausBusUtils.setBit(setValue, 7, self.value)
    return self;

  def isGruppe8(self):
    return HausBusUtils.isBitSet(7, self.value)
  def __init__(self, value:int):
    self.value = value

  @staticmethod
  def _fromBytes(data:bytearray, offset):
    return MGroupMask(HausBusUtils.bytesToInt(data, offset))



  def getValue(self):
    return self.value
  def getEntryNames(self):
    result = []
    result.append("Gruppe1")
    result.append("Gruppe2")
    result.append("Gruppe3")
    result.append("Gruppe4")
    result.append("Gruppe5")
    result.append("Gruppe6")
    result.append("Gruppe7")
    result.append("Gruppe8")
    return result
  def setEntry(self,name:str, setValue:bool):
    if (name == "Gruppe1"):
      self.setGruppe1(setValue)
    if (name == "Gruppe2"):
      self.setGruppe2(setValue)
    if (name == "Gruppe3"):
      self.setGruppe3(setValue)
    if (name == "Gruppe4"):
      self.setGruppe4(setValue)
    if (name == "Gruppe5"):
      self.setGruppe5(setValue)
    if (name == "Gruppe6"):
      self.setGruppe6(setValue)
    if (name == "Gruppe7"):
      self.setGruppe7(setValue)
    if (name == "Gruppe8"):
      self.setGruppe8(setValue)

  def __str__(self):
    return f"MGroupMask(Gruppe1 = {self.isGruppe1()}, Gruppe2 = {self.isGruppe2()}, Gruppe3 = {self.isGruppe3()}, Gruppe4 = {self.isGruppe4()}, Gruppe5 = {self.isGruppe5()}, Gruppe6 = {self.isGruppe6()}, Gruppe7 = {self.isGruppe7()}, Gruppe8 = {self.isGruppe8()})"



