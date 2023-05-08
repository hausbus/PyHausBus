import pyhausbus.HausBusUtils as HausBusUtils

class SendCommand:
  CLASS_ID = 160
  FUNCTION_ID = 4

  def __init__(self,command:int, address:int):
    self.command=command
    self.address=address


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return SendCommand(HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset))

  def __str__(self):
    return f"SendCommand(command={self.command}, address={self.address})"

  '''
  @param command Dali Kommando s.Spezifikation.
  '''
  def getCommand(self):
    return self.command

  '''
  @param address Kurz- oder Gruppenadresse YAAA AAAS\r\n64 Kurzadressen           0AAA AAAS\r\n16 Gruppenadressen        100A AAAS\r\nSammelaufruf              1111 111S\r\n\r\nY: Adressenart: Y=?  ? ? ??  ?? ??? ??  ?0?  ? ? ??  ?? ??? ??  ? ? Kurzadresse.
  '''
  def getAddress(self):
    return self.address



