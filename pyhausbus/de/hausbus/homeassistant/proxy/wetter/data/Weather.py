from pyhausbus.WeekTime import WeekTime
import pyhausbus.HausBusUtils as HausBusUtils

class Weather:
  CLASS_ID = 2
  FUNCTION_ID = 128

  def __init__(self,humidity:int, pressure:int, temp:int, sunrise:WeekTime, sunset:WeekTime, text:str):
    self.humidity=humidity
    self.pressure=pressure
    self.temp=temp
    self.sunrise=sunrise
    self.sunset=sunset
    self.text=text


  @staticmethod
  def _fromBytes(dataIn:bytearray, offset):
    return Weather(HausBusUtils.bytesToInt(dataIn, offset), HausBusUtils.bytesToWord(dataIn, offset), HausBusUtils.bytesToInt(dataIn, offset), WeekTime._fromBytes(dataIn, offset), WeekTime._fromBytes(dataIn, offset), HausBusUtils.bytesToString(dataIn, offset))

  def __str__(self):
    return f"Weather(humidity={self.humidity}, pressure={self.pressure}, temp={self.temp}, sunrise={self.sunrise}, sunset={self.sunset}, text={self.text})"

  '''
  @param humidity Luftfeuchtigkeit.
  '''
  def getHumidity(self):
    return self.humidity

  '''
  @param pressure Luftdruck.
  '''
  def getPressure(self):
    return self.pressure

  '''
  @param temp Temperatur.
  '''
  def getTemp(self):
    return self.temp

  '''
  @param sunrise Zeitpunkt vom Sonnenaufgang.
  '''
  def getSunrise(self):
    return self.sunrise

  '''
  @param sunset Zeitpunkt vom Sonnenuntergang.
  '''
  def getSunset(self):
    return self.sunset

  '''
  @param text Beschreibung.
  '''
  def getText(self):
    return self.text



