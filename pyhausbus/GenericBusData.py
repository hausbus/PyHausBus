
class GenericBusData:

  def __init__(self, objectId: int):
    pass  # Platzhalter, sonst IndentationError
    
  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return GenericBusData()

  def __str__(self):
    return f"GenericBusData()"


