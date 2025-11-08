def getBusClassNameFor(classId, functionId):
  if (classId==16 and functionId==201):
    return "pyhausbus.de.hausbus.homeassistant.proxy.taster.data.EvClicked"
  if (classId==16 and functionId==202):
    return "pyhausbus.de.hausbus.homeassistant.proxy.taster.data.EvDoubleClick"
  if (classId==16 and functionId==203):
    return "pyhausbus.de.hausbus.homeassistant.proxy.taster.data.EvHoldStart"
  if (classId==16 and functionId==204):
    return "pyhausbus.de.hausbus.homeassistant.proxy.taster.data.EvHoldEnd"
  if (classId==16 and functionId==0):
    return "pyhausbus.de.hausbus.homeassistant.proxy.taster.commands.GetConfiguration"
  if (classId==16 and functionId==1):
    return "pyhausbus.de.hausbus.homeassistant.proxy.taster.commands.SetConfiguration"
  if (classId==16 and functionId==128):
    return "pyhausbus.de.hausbus.homeassistant.proxy.taster.data.Configuration"
  if (classId==16 and functionId==200):
    return "pyhausbus.de.hausbus.homeassistant.proxy.taster.data.EvCovered"
  if (classId==16 and functionId==205):
    return "pyhausbus.de.hausbus.homeassistant.proxy.taster.data.EvFree"
  if (classId==16 and functionId==255):
    return "pyhausbus.de.hausbus.homeassistant.proxy.taster.data.EvError"
  if (classId==16 and functionId==2):
    return "pyhausbus.de.hausbus.homeassistant.proxy.taster.commands.EnableEvents"
  if (classId==16 and functionId==3):
    return "pyhausbus.de.hausbus.homeassistant.proxy.taster.commands.GetStatus"
  if (classId==16 and functionId==129):
    return "pyhausbus.de.hausbus.homeassistant.proxy.taster.data.Status"
  if (classId==16 and functionId==206):
    return "pyhausbus.de.hausbus.homeassistant.proxy.taster.data.EvEnabled"
  if (classId==16 and functionId==130):
    return "pyhausbus.de.hausbus.homeassistant.proxy.taster.data.Enabled"
  if (classId==16 and functionId==4):
    return "pyhausbus.de.hausbus.homeassistant.proxy.taster.commands.GetEnabled"
  if (classId==16 and functionId==5):
    return "pyhausbus.de.hausbus.homeassistant.proxy.taster.commands.TriggerStatusEvent"
  if (classId==32 and functionId==200):
    return "pyhausbus.de.hausbus.homeassistant.proxy.temperatursensor.data.EvCold"
  if (classId==32 and functionId==201):
    return "pyhausbus.de.hausbus.homeassistant.proxy.temperatursensor.data.EvWarm"
  if (classId==32 and functionId==202):
    return "pyhausbus.de.hausbus.homeassistant.proxy.temperatursensor.data.EvHot"
  if (classId==32 and functionId==0):
    return "pyhausbus.de.hausbus.homeassistant.proxy.temperatursensor.commands.GetConfiguration"
  if (classId==32 and functionId==128):
    return "pyhausbus.de.hausbus.homeassistant.proxy.temperatursensor.data.Configuration"
  if (classId==32 and functionId==1):
    return "pyhausbus.de.hausbus.homeassistant.proxy.temperatursensor.commands.SetConfiguration"
  if (classId==32 and functionId==2):
    return "pyhausbus.de.hausbus.homeassistant.proxy.temperatursensor.commands.GetStatus"
  if (classId==32 and functionId==203):
    return "pyhausbus.de.hausbus.homeassistant.proxy.temperatursensor.data.EvStatus"
  if (classId==32 and functionId==255):
    return "pyhausbus.de.hausbus.homeassistant.proxy.temperatursensor.data.EvError"
  if (classId==32 and functionId==129):
    return "pyhausbus.de.hausbus.homeassistant.proxy.temperatursensor.data.Status"
  if (classId==19 and functionId==4):
    return "pyhausbus.de.hausbus.homeassistant.proxy.schalter.commands.Toggle"
  if (classId==19 and functionId==3):
    return "pyhausbus.de.hausbus.homeassistant.proxy.schalter.commands.On"
  if (classId==19 and functionId==2):
    return "pyhausbus.de.hausbus.homeassistant.proxy.schalter.commands.Off"
  if (classId==19 and functionId==201):
    return "pyhausbus.de.hausbus.homeassistant.proxy.schalter.data.EvOn"
  if (classId==19 and functionId==200):
    return "pyhausbus.de.hausbus.homeassistant.proxy.schalter.data.EvOff"
  if (classId==19 and functionId==5):
    return "pyhausbus.de.hausbus.homeassistant.proxy.schalter.commands.GetStatus"
  if (classId==19 and functionId==129):
    return "pyhausbus.de.hausbus.homeassistant.proxy.schalter.data.Status"
  if (classId==19 and functionId==255):
    return "pyhausbus.de.hausbus.homeassistant.proxy.schalter.data.EvError"
  if (classId==19 and functionId==202):
    return "pyhausbus.de.hausbus.homeassistant.proxy.schalter.data.EvToggle"
  if (classId==19 and functionId==128):
    return "pyhausbus.de.hausbus.homeassistant.proxy.schalter.data.Configuration"
  if (classId==19 and functionId==0):
    return "pyhausbus.de.hausbus.homeassistant.proxy.schalter.commands.GetConfiguration"
  if (classId==19 and functionId==1):
    return "pyhausbus.de.hausbus.homeassistant.proxy.schalter.commands.SetConfiguration"
  if (classId==19 and functionId==203):
    return "pyhausbus.de.hausbus.homeassistant.proxy.schalter.data.EvCmdDelay"
  if (classId==19 and functionId==204):
    return "pyhausbus.de.hausbus.homeassistant.proxy.schalter.data.EvDisabled"
  if (classId==19 and functionId==6):
    return "pyhausbus.de.hausbus.homeassistant.proxy.schalter.commands.ToggleByDuty"
  if (classId==19 and functionId==205):
    return "pyhausbus.de.hausbus.homeassistant.proxy.schalter.data.EvToggleByDuty"
  if (classId==17 and functionId==201):
    return "pyhausbus.de.hausbus.homeassistant.proxy.dimmer.data.EvOn"
  if (classId==17 and functionId==1):
    return "pyhausbus.de.hausbus.homeassistant.proxy.dimmer.commands.SetConfiguration"
  if (classId==17 and functionId==0):
    return "pyhausbus.de.hausbus.homeassistant.proxy.dimmer.commands.GetConfiguration"
  if (classId==17 and functionId==2):
    return "pyhausbus.de.hausbus.homeassistant.proxy.dimmer.commands.SetBrightness"
  if (classId==17 and functionId==128):
    return "pyhausbus.de.hausbus.homeassistant.proxy.dimmer.data.Configuration"
  if (classId==17 and functionId==200):
    return "pyhausbus.de.hausbus.homeassistant.proxy.dimmer.data.EvOff"
  if (classId==17 and functionId==202):
    return "pyhausbus.de.hausbus.homeassistant.proxy.dimmer.data.EvStart"
  if (classId==17 and functionId==3):
    return "pyhausbus.de.hausbus.homeassistant.proxy.dimmer.commands.Start"
  if (classId==17 and functionId==4):
    return "pyhausbus.de.hausbus.homeassistant.proxy.dimmer.commands.Stop"
  if (classId==17 and functionId==5):
    return "pyhausbus.de.hausbus.homeassistant.proxy.dimmer.commands.GetStatus"
  if (classId==17 and functionId==129):
    return "pyhausbus.de.hausbus.homeassistant.proxy.dimmer.data.Status"
  if (classId==17 and functionId==255):
    return "pyhausbus.de.hausbus.homeassistant.proxy.dimmer.data.EvError"
  if (classId==0 and functionId==2):
    return "pyhausbus.de.hausbus.homeassistant.proxy.controller.commands.GetModuleId"
  if (classId==0 and functionId==5):
    return "pyhausbus.de.hausbus.homeassistant.proxy.controller.commands.GetConfiguration"
  if (classId==0 and functionId==128):
    return "pyhausbus.de.hausbus.homeassistant.proxy.controller.data.ModuleId"
  if (classId==0 and functionId==131):
    return "pyhausbus.de.hausbus.homeassistant.proxy.controller.data.Configuration"
  if (classId==0 and functionId==3):
    return "pyhausbus.de.hausbus.homeassistant.proxy.controller.commands.GetRemoteObjects"
  if (classId==0 and functionId==129):
    return "pyhausbus.de.hausbus.homeassistant.proxy.controller.data.RemoteObjects"
  if (classId==0 and functionId==0):
    return "pyhausbus.de.hausbus.homeassistant.proxy.controller.commands.GenerateRandomDeviceId"
  if (classId==0 and functionId==1):
    return "pyhausbus.de.hausbus.homeassistant.proxy.controller.commands.Reset"
  if (classId==0 and functionId==4):
    return "pyhausbus.de.hausbus.homeassistant.proxy.controller.commands.GetUnusedMemory"
  if (classId==0 and functionId==6):
    return "pyhausbus.de.hausbus.homeassistant.proxy.controller.commands.SetConfiguration"
  if (classId==0 and functionId==130):
    return "pyhausbus.de.hausbus.homeassistant.proxy.controller.data.UnusedMemory"
  if (classId==0 and functionId==7):
    return "pyhausbus.de.hausbus.homeassistant.proxy.controller.commands.ReadMemory"
  if (classId==0 and functionId==8):
    return "pyhausbus.de.hausbus.homeassistant.proxy.controller.commands.WriteMemory"
  if (classId==0 and functionId==127):
    return "pyhausbus.de.hausbus.homeassistant.proxy.controller.commands.Ping"
  if (classId==0 and functionId==199):
    return "pyhausbus.de.hausbus.homeassistant.proxy.controller.data.Pong"
  if (classId==0 and functionId==132):
    return "pyhausbus.de.hausbus.homeassistant.proxy.controller.data.MemoryData"
  if (classId==0 and functionId==133):
    return "pyhausbus.de.hausbus.homeassistant.proxy.controller.data.MemoryStatus"
  if (classId==0 and functionId==9):
    return "pyhausbus.de.hausbus.homeassistant.proxy.controller.commands.WriteRules"
  if (classId==0 and functionId==10):
    return "pyhausbus.de.hausbus.homeassistant.proxy.controller.commands.ReadRules"
  if (classId==0 and functionId==134):
    return "pyhausbus.de.hausbus.homeassistant.proxy.controller.data.RulesData"
  if (classId==0 and functionId==200):
    return "pyhausbus.de.hausbus.homeassistant.proxy.controller.data.EvTime"
  if (classId==0 and functionId==201):
    return "pyhausbus.de.hausbus.homeassistant.proxy.controller.data.EvNewDeviceId"
  if (classId==0 and functionId==202):
    return "pyhausbus.de.hausbus.homeassistant.proxy.controller.data.EvStarted"
  if (classId==0 and functionId==255):
    return "pyhausbus.de.hausbus.homeassistant.proxy.controller.data.EvError"
  if (classId==0 and functionId==126):
    return "pyhausbus.de.hausbus.homeassistant.proxy.controller.commands.GetTime"
  if (classId==0 and functionId==125):
    return "pyhausbus.de.hausbus.homeassistant.proxy.controller.commands.SetTime"
  if (classId==0 and functionId==198):
    return "pyhausbus.de.hausbus.homeassistant.proxy.controller.data.Time"
  if (classId==0 and functionId==12):
    return "pyhausbus.de.hausbus.homeassistant.proxy.controller.commands.GetRuleState"
  if (classId==0 and functionId==11):
    return "pyhausbus.de.hausbus.homeassistant.proxy.controller.commands.SetRuleState"
  if (classId==0 and functionId==13):
    return "pyhausbus.de.hausbus.homeassistant.proxy.controller.commands.TriggerRuleElement"
  if (classId==0 and functionId==135):
    return "pyhausbus.de.hausbus.homeassistant.proxy.controller.data.RuleState"
  if (classId==0 and functionId==14):
    return "pyhausbus.de.hausbus.homeassistant.proxy.controller.commands.SetUnitGroupState"
  if (classId==0 and functionId==203):
    return "pyhausbus.de.hausbus.homeassistant.proxy.controller.data.EvGroupOn"
  if (classId==0 and functionId==205):
    return "pyhausbus.de.hausbus.homeassistant.proxy.controller.data.EvGroupOff"
  if (classId==0 and functionId==204):
    return "pyhausbus.de.hausbus.homeassistant.proxy.controller.data.EvGroupUndefined"
  if (classId==0 and functionId==136):
    return "pyhausbus.de.hausbus.homeassistant.proxy.controller.data.TriggeredRule"
  if (classId==0 and functionId==124):
    return "pyhausbus.de.hausbus.homeassistant.proxy.controller.commands.SetDebugOptions"
  if (classId==0 and functionId==197):
    return "pyhausbus.de.hausbus.homeassistant.proxy.controller.data.TimeD  ifference"
  if (classId==0 and functionId==206):
    return "pyhausbus.de.hausbus.homeassistant.proxy.controller.data.EvDay"
  if (classId==0 and functionId==207):
    return "pyhausbus.de.hausbus.homeassistant.proxy.controller.data.EvNight"
  if (classId==0 and functionId==15):
    return "pyhausbus.de.hausbus.homeassistant.proxy.controller.commands.SetSunTimes"
  if (classId==0 and functionId==16):
    return "pyhausbus.de.hausbus.homeassistant.proxy.controller.commands.SetSystemVariable"
  if (classId==0 and functionId==17):
    return "pyhausbus.de.hausbus.homeassistant.proxy.controller.commands.GetSystemVariable"
  if (classId==0 and functionId==137):
    return "pyhausbus.de.hausbus.homeassistant.proxy.controller.data.SystemVariable"
  if (classId==0 and functionId==18):
    return "pyhausbus.de.hausbus.homeassistant.proxy.controller.commands.GetUnitGroupStatus"
  if (classId==0 and functionId==138):
    return "pyhausbus.de.hausbus.homeassistant.proxy.controller.data.UnitGroupStatus"
  if (classId==0 and functionId==250):
    return "pyhausbus.de.hausbus.homeassistant.proxy.controller.data.EvConsole"
  if (classId==0 and functionId==208):
    return "pyhausbus.de.hausbus.homeassistant.proxy.controller.data.EvResetW  ifi"
  if (classId==0 and functionId==209):
    return "pyhausbus.de.hausbus.homeassistant.proxy.controller.data.EvZeroCrossData"
  if (classId==0 and functionId==19):
    return "pyhausbus.de.hausbus.homeassistant.proxy.controller.commands.EnableFeature"
  if (classId==0 and functionId==210):
    return "pyhausbus.de.hausbus.homeassistant.proxy.controller.data.EvSystemVariableChanged"
  if (classId==0 and functionId==20):
    return "pyhausbus.de.hausbus.homeassistant.proxy.controller.commands.ResetOneWireManager"
  if (classId==0 and functionId==21):
    return "pyhausbus.de.hausbus.homeassistant.proxy.controller.commands.SetWatchDogTime"
  if (classId==18 and functionId==0):
    return "pyhausbus.de.hausbus.homeassistant.proxy.rollladen.commands.GetConfiguration"
  if (classId==18 and functionId==2):
    return "pyhausbus.de.hausbus.homeassistant.proxy.rollladen.commands.MoveToPosition"
  if (classId==18 and functionId==3):
    return "pyhausbus.de.hausbus.homeassistant.proxy.rollladen.commands.Start"
  if (classId==18 and functionId==4):
    return "pyhausbus.de.hausbus.homeassistant.proxy.rollladen.commands.Stop"
  if (classId==18 and functionId==128):
    return "pyhausbus.de.hausbus.homeassistant.proxy.rollladen.data.Configuration"
  if (classId==18 and functionId==200):
    return "pyhausbus.de.hausbus.homeassistant.proxy.rollladen.data.EvClosed"
  if (classId==18 and functionId==201):
    return "pyhausbus.de.hausbus.homeassistant.proxy.rollladen.data.EvStart"
  if (classId==18 and functionId==5):
    return "pyhausbus.de.hausbus.homeassistant.proxy.rollladen.commands.GetStatus"
  if (classId==18 and functionId==129):
    return "pyhausbus.de.hausbus.homeassistant.proxy.rollladen.data.Status"
  if (classId==18 and functionId==1):
    return "pyhausbus.de.hausbus.homeassistant.proxy.rollladen.commands.SetConfiguration"
  if (classId==18 and functionId==255):
    return "pyhausbus.de.hausbus.homeassistant.proxy.rollladen.data.EvError"
  if (classId==18 and functionId==6):
    return "pyhausbus.de.hausbus.homeassistant.proxy.rollladen.commands.SetPosition"
  if (classId==18 and functionId==202):
    return "pyhausbus.de.hausbus.homeassistant.proxy.rollladen.data.EvOpen"
  if (classId==18 and functionId==251):
    return "pyhausbus.de.hausbus.homeassistant.proxy.rollladen.data.EvNewMainState"
  if (classId==18 and functionId==252):
    return "pyhausbus.de.hausbus.homeassistant.proxy.rollladen.data.EvNewSubState"
  if (classId==15 and functionId==0):
    return "pyhausbus.de.hausbus.homeassistant.proxy.digitalPort.commands.GetConfiguration"
  if (classId==15 and functionId==1):
    return "pyhausbus.de.hausbus.homeassistant.proxy.digitalPort.commands.SetConfiguration"
  if (classId==15 and functionId==128):
    return "pyhausbus.de.hausbus.homeassistant.proxy.digitalPort.data.Configuration"
  if (classId==15 and functionId==255):
    return "pyhausbus.de.hausbus.homeassistant.proxy.digitalPort.data.EvError"
  if (classId==20 and functionId==0):
    return "pyhausbus.de.hausbus.homeassistant.proxy.logicalButton.commands.GetConfiguration"
  if (classId==20 and functionId==1):
    return "pyhausbus.de.hausbus.homeassistant.proxy.logicalButton.commands.SetConfiguration"
  if (classId==20 and functionId==128):
    return "pyhausbus.de.hausbus.homeassistant.proxy.logicalButton.data.Configuration"
  if (classId==20 and functionId==255):
    return "pyhausbus.de.hausbus.homeassistant.proxy.logicalButton.data.EvError"
  if (classId==20 and functionId==200):
    return "pyhausbus.de.hausbus.homeassistant.proxy.logicalButton.data.EvOff"
  if (classId==20 and functionId==201):
    return "pyhausbus.de.hausbus.homeassistant.proxy.logicalButton.data.EvOn"
  if (classId==20 and functionId==202):
    return "pyhausbus.de.hausbus.homeassistant.proxy.logicalButton.data.EvBlink"
  if (classId==20 and functionId==2):
    return "pyhausbus.de.hausbus.homeassistant.proxy.logicalButton.commands.Off"
  if (classId==20 and functionId==3):
    return "pyhausbus.de.hausbus.homeassistant.proxy.logicalButton.commands.On"
  if (classId==20 and functionId==4):
    return "pyhausbus.de.hausbus.homeassistant.proxy.logicalButton.commands.Blink"
  if (classId==20 and functionId==129):
    return "pyhausbus.de.hausbus.homeassistant.proxy.logicalButton.data.Status"
  if (classId==20 and functionId==5):
    return "pyhausbus.de.hausbus.homeassistant.proxy.logicalButton.commands.GetStatus"
  if (classId==20 and functionId==11):
    return "pyhausbus.de.hausbus.homeassistant.proxy.logicalButton.commands.SetButtonConfiguration"
  if (classId==20 and functionId==12):
    return "pyhausbus.de.hausbus.homeassistant.proxy.logicalButton.commands.SetLedConfiguration"
  if (classId==20 and functionId==6):
    return "pyhausbus.de.hausbus.homeassistant.proxy.logicalButton.commands.SetMinBrightness"
  if (classId==20 and functionId==7):
    return "pyhausbus.de.hausbus.homeassistant.proxy.logicalButton.commands.GetMinBrightness"
  if (classId==21 and functionId==0):
    return "pyhausbus.de.hausbus.homeassistant.proxy.led.commands.GetConfiguration"
  if (classId==21 and functionId==1):
    return "pyhausbus.de.hausbus.homeassistant.proxy.led.commands.SetConfiguration"
  if (classId==21 and functionId==3):
    return "pyhausbus.de.hausbus.homeassistant.proxy.led.commands.On"
  if (classId==21 and functionId==4):
    return "pyhausbus.de.hausbus.homeassistant.proxy.led.commands.Blink"
  if (classId==21 and functionId==5):
    return "pyhausbus.de.hausbus.homeassistant.proxy.led.commands.GetStatus"
  if (classId==21 and functionId==128):
    return "pyhausbus.de.hausbus.homeassistant.proxy.led.data.Configuration"
  if (classId==21 and functionId==129):
    return "pyhausbus.de.hausbus.homeassistant.proxy.led.data.Status"
  if (classId==21 and functionId==200):
    return "pyhausbus.de.hausbus.homeassistant.proxy.led.data.EvOff"
  if (classId==21 and functionId==201):
    return "pyhausbus.de.hausbus.homeassistant.proxy.led.data.EvOn"
  if (classId==21 and functionId==202):
    return "pyhausbus.de.hausbus.homeassistant.proxy.led.data.EvBlink"
  if (classId==21 and functionId==255):
    return "pyhausbus.de.hausbus.homeassistant.proxy.led.data.EvError"
  if (classId==21 and functionId==2):
    return "pyhausbus.de.hausbus.homeassistant.proxy.led.commands.Off"
  if (classId==21 and functionId==6):
    return "pyhausbus.de.hausbus.homeassistant.proxy.led.commands.SetMinBrightness"
  if (classId==21 and functionId==203):
    return "pyhausbus.de.hausbus.homeassistant.proxy.led.data.EvCmdDelay"
  if (classId==21 and functionId==7):
    return "pyhausbus.de.hausbus.homeassistant.proxy.led.commands.GetMinBrightness"
  if (classId==21 and functionId==130):
    return "pyhausbus.de.hausbus.homeassistant.proxy.led.data.MinBrightness"
  if (classId==33 and functionId==0):
    return "pyhausbus.de.hausbus.homeassistant.proxy.iRSensor.commands.Off"
  if (classId==33 and functionId==1):
    return "pyhausbus.de.hausbus.homeassistant.proxy.iRSensor.commands.On"
  if (classId==33 and functionId==202):
    return "pyhausbus.de.hausbus.homeassistant.proxy.iRSensor.data.EvClicked"
  if (classId==33 and functionId==200):
    return "pyhausbus.de.hausbus.homeassistant.proxy.iRSensor.data.EvOff"
  if (classId==33 and functionId==201):
    return "pyhausbus.de.hausbus.homeassistant.proxy.iRSensor.data.EvOn"
  if (classId==33 and functionId==203):
    return "pyhausbus.de.hausbus.homeassistant.proxy.iRSensor.data.EvHoldStart"
  if (classId==33 and functionId==204):
    return "pyhausbus.de.hausbus.homeassistant.proxy.iRSensor.data.EvHoldEnd"
  if (classId==160 and functionId==0):
    return "pyhausbus.de.hausbus.homeassistant.proxy.daliLine.commands.GetConfiguration"
  if (classId==160 and functionId==1):
    return "pyhausbus.de.hausbus.homeassistant.proxy.daliLine.commands.SetConfiguration"
  if (classId==160 and functionId==2):
    return "pyhausbus.de.hausbus.homeassistant.proxy.daliLine.commands.AllOff"
  if (classId==160 and functionId==3):
    return "pyhausbus.de.hausbus.homeassistant.proxy.daliLine.commands.AllOn"
  if (classId==160 and functionId==4):
    return "pyhausbus.de.hausbus.homeassistant.proxy.daliLine.commands.SendCommand"
  if (classId==160 and functionId==128):
    return "pyhausbus.de.hausbus.homeassistant.proxy.daliLine.data.Configuration"
  if (classId==160 and functionId==129):
    return "pyhausbus.de.hausbus.homeassistant.proxy.daliLine.data.Status"
  if (classId==160 and functionId==255):
    return "pyhausbus.de.hausbus.homeassistant.proxy.daliLine.data.EvError"
  if (classId==162 and functionId==2):
    return "pyhausbus.de.hausbus.homeassistant.proxy.ethernet.commands.WakeUpDevice"
  if (classId==162 and functionId==128):
    return "pyhausbus.de.hausbus.homeassistant.proxy.ethernet.data.Configuration"
  if (classId==162 and functionId==1):
    return "pyhausbus.de.hausbus.homeassistant.proxy.ethernet.commands.SetConfiguration"
  if (classId==162 and functionId==0):
    return "pyhausbus.de.hausbus.homeassistant.proxy.ethernet.commands.GetConfiguration"
  if (classId==162 and functionId==255):
    return "pyhausbus.de.hausbus.homeassistant.proxy.ethernet.data.EvError"
  if (classId==162 and functionId==129):
    return "pyhausbus.de.hausbus.homeassistant.proxy.ethernet.data.CurrentIp"
  if (classId==162 and functionId==3):
    return "pyhausbus.de.hausbus.homeassistant.proxy.ethernet.commands.GetCurrentIp"
  if (classId==34 and functionId==200):
    return "pyhausbus.de.hausbus.homeassistant.proxy.feuchtesensor.data.EvDry"
  if (classId==34 and functionId==201):
    return "pyhausbus.de.hausbus.homeassistant.proxy.feuchtesensor.data.EvConfortable"
  if (classId==34 and functionId==202):
    return "pyhausbus.de.hausbus.homeassistant.proxy.feuchtesensor.data.EvWet"
  if (classId==34 and functionId==255):
    return "pyhausbus.de.hausbus.homeassistant.proxy.feuchtesensor.data.EvError"
  if (classId==34 and functionId==0):
    return "pyhausbus.de.hausbus.homeassistant.proxy.feuchtesensor.commands.GetConfiguration"
  if (classId==34 and functionId==1):
    return "pyhausbus.de.hausbus.homeassistant.proxy.feuchtesensor.commands.SetConfiguration"
  if (classId==34 and functionId==2):
    return "pyhausbus.de.hausbus.homeassistant.proxy.feuchtesensor.commands.GetStatus"
  if (classId==34 and functionId==128):
    return "pyhausbus.de.hausbus.homeassistant.proxy.feuchtesensor.data.Configuration"
  if (classId==34 and functionId==203):
    return "pyhausbus.de.hausbus.homeassistant.proxy.feuchtesensor.data.EvStatus"
  if (classId==34 and functionId==129):
    return "pyhausbus.de.hausbus.homeassistant.proxy.feuchtesensor.data.Status"
  if (classId==1 and functionId==0):
    return "pyhausbus.de.hausbus.homeassistant.proxy.pCServer.commands.Exec"
  if (classId==1 and functionId==126):
    return "pyhausbus.de.hausbus.homeassistant.proxy.pCServer.commands.SetVariable"
  if (classId==1 and functionId==11):
    return "pyhausbus.de.hausbus.homeassistant.proxy.pCServer.commands.Shutdown"
  if (classId==1 and functionId==12):
    return "pyhausbus.de.hausbus.homeassistant.proxy.pCServer.commands.Restart"
  if (classId==1 and functionId==20):
    return "pyhausbus.de.hausbus.homeassistant.proxy.pCServer.commands.Quit"
  if (classId==1 and functionId==200):
    return "pyhausbus.de.hausbus.homeassistant.proxy.pCServer.data.EvOnline"
  if (classId==1 and functionId==201):
    return "pyhausbus.de.hausbus.homeassistant.proxy.pCServer.data.EvOffline"
  if (classId==1 and functionId==10):
    return "pyhausbus.de.hausbus.homeassistant.proxy.pCServer.commands.Standby"
  if (classId==1 and functionId==13):
    return "pyhausbus.de.hausbus.homeassistant.proxy.pCServer.commands.ReloadUserPlugin"
  if (classId==2 and functionId==5):
    return "pyhausbus.de.hausbus.homeassistant.proxy.wetter.commands.GetWeather"
  if (classId==2 and functionId==128):
    return "pyhausbus.de.hausbus.homeassistant.proxy.wetter.data.Weather"
  if (classId==176 and functionId==255):
    return "pyhausbus.de.hausbus.homeassistant.proxy.gateway.data.EvError"
  if (classId==176 and functionId==0):
    return "pyhausbus.de.hausbus.homeassistant.proxy.gateway.commands.GetConfiguration"
  if (classId==176 and functionId==1):
    return "pyhausbus.de.hausbus.homeassistant.proxy.gateway.commands.SetConfiguration"
  if (classId==176 and functionId==3):
    return "pyhausbus.de.hausbus.homeassistant.proxy.gateway.commands.GetMinIdleTime"
  if (classId==176 and functionId==129):
    return "pyhausbus.de.hausbus.homeassistant.proxy.gateway.data.MinIdleTime"
  if (classId==176 and functionId==128):
    return "pyhausbus.de.hausbus.homeassistant.proxy.gateway.data.Configuration"
  if (classId==176 and functionId==4):
    return "pyhausbus.de.hausbus.homeassistant.proxy.gateway.commands.SetMinIdleTime"
  if (classId==176 and functionId==5):
    return "pyhausbus.de.hausbus.homeassistant.proxy.gateway.commands.GetConnectedDevices"
  if (classId==176 and functionId==130):
    return "pyhausbus.de.hausbus.homeassistant.proxy.gateway.data.ConnectedDevices"
  if (classId==176 and functionId==200):
    return "pyhausbus.de.hausbus.homeassistant.proxy.gateway.data.EvGatewayLoad"
  if (classId==176 and functionId==2):
    return "pyhausbus.de.hausbus.homeassistant.proxy.gateway.commands.SetPreferLoxone"
  if (classId==35 and functionId==0):
    return "pyhausbus.de.hausbus.homeassistant.proxy.counter.commands.GetConfiguration"
  if (classId==35 and functionId==1):
    return "pyhausbus.de.hausbus.homeassistant.proxy.counter.commands.SetConfiguration"
  if (classId==35 and functionId==2):
    return "pyhausbus.de.hausbus.homeassistant.proxy.counter.commands.GetStatus"
  if (classId==35 and functionId==3):
    return "pyhausbus.de.hausbus.homeassistant.proxy.counter.commands.SetCount"
  if (classId==35 and functionId==128):
    return "pyhausbus.de.hausbus.homeassistant.proxy.counter.data.Configuration"
  if (classId==35 and functionId==255):
    return "pyhausbus.de.hausbus.homeassistant.proxy.counter.data.EvError"
  if (classId==35 and functionId==129):
    return "pyhausbus.de.hausbus.homeassistant.proxy.counter.data.Status"
  if (classId==35 and functionId==200):
    return "pyhausbus.de.hausbus.homeassistant.proxy.counter.data.EvStatus"
  if (classId==3 and functionId==0):
    return "pyhausbus.de.hausbus.homeassistant.proxy.systemTime.commands.GetTime"
  if (classId==3 and functionId==1):
    return "pyhausbus.de.hausbus.homeassistant.proxy.systemTime.commands.SetTime"
  if (classId==3 and functionId==128):
    return "pyhausbus.de.hausbus.homeassistant.proxy.systemTime.data.Time"
  if (classId==3 and functionId==255):
    return "pyhausbus.de.hausbus.homeassistant.proxy.systemTime.data.EvError"
  if (classId==90 and functionId==3):
    return "pyhausbus.de.hausbus.homeassistant.proxy.currentReader.commands.SetConfiguration"
  if (classId==90 and functionId==4):
    return "pyhausbus.de.hausbus.homeassistant.proxy.currentReader.commands.GetConfiguration"
  if (classId==90 and functionId==129):
    return "pyhausbus.de.hausbus.homeassistant.proxy.currentReader.data.Configuration"
  if (classId==90 and functionId==200):
    return "pyhausbus.de.hausbus.homeassistant.proxy.currentReader.data.EvSignal"
  if (classId==90 and functionId==1):
    return "pyhausbus.de.hausbus.homeassistant.proxy.currentReader.commands.GetCurrent"
  if (classId==90 and functionId==201):
    return "pyhausbus.de.hausbus.homeassistant.proxy.currentReader.data.EvCurrent"
  if (classId==90 and functionId==130):
    return "pyhausbus.de.hausbus.homeassistant.proxy.currentReader.data.Power"
  if (classId==90 and functionId==128):
    return "pyhausbus.de.hausbus.homeassistant.proxy.currentReader.data.Current"
  if (classId==90 and functionId==6):
    return "pyhausbus.de.hausbus.homeassistant.proxy.currentReader.commands.GetSignalCount"
  if (classId==90 and functionId==131):
    return "pyhausbus.de.hausbus.homeassistant.proxy.currentReader.data.SignalCount"
  if (classId==90 and functionId==7):
    return "pyhausbus.de.hausbus.homeassistant.proxy.currentReader.commands.ClearSignalCount"
  if (classId==90 and functionId==2):
    return "pyhausbus.de.hausbus.homeassistant.proxy.currentReader.commands.SetSignalCount"
  if (classId==90 and functionId==5):
    return "pyhausbus.de.hausbus.homeassistant.proxy.currentReader.commands.GetPower"
  if (classId==90 and functionId==9):
    return "pyhausbus.de.hausbus.homeassistant.proxy.currentReader.commands.IncSignalCount"
  if (classId==90 and functionId==10):
    return "pyhausbus.de.hausbus.homeassistant.proxy.currentReader.commands.DecSignalCount"
  if (classId==90 and functionId==210):
    return "pyhausbus.de.hausbus.homeassistant.proxy.currentReader.data.EvDebug"
  if (classId==90 and functionId==211):
    return "pyhausbus.de.hausbus.homeassistant.proxy.currentReader.data.EvInterrupt"
  if (classId==90 and functionId==255):
    return "pyhausbus.de.hausbus.homeassistant.proxy.currentReader.data.EvError"
  if (classId==91 and functionId==1):
    return "pyhausbus.de.hausbus.homeassistant.proxy.tcpClient.commands.AnnounceServer"
  if (classId==91 and functionId==2):
    return "pyhausbus.de.hausbus.homeassistant.proxy.tcpClient.commands.GetCurrentIp"
  if (classId==91 and functionId==128):
    return "pyhausbus.de.hausbus.homeassistant.proxy.tcpClient.data.CurrentIp"
  if (classId==91 and functionId==200):
    return "pyhausbus.de.hausbus.homeassistant.proxy.tcpClient.data.EvWhoIsServer"
  if (classId==164 and functionId==255):
    return "pyhausbus.de.hausbus.homeassistant.proxy.wiFi.data.EvError"
  if (classId==164 and functionId==0):
    return "pyhausbus.de.hausbus.homeassistant.proxy.wiFi.commands.GetConfiguration"
  if (classId==164 and functionId==2):
    return "pyhausbus.de.hausbus.homeassistant.proxy.wiFi.commands.WakeUpDevice"
  if (classId==164 and functionId==1):
    return "pyhausbus.de.hausbus.homeassistant.proxy.wiFi.commands.SetConfiguration"
  if (classId==164 and functionId==128):
    return "pyhausbus.de.hausbus.homeassistant.proxy.wiFi.data.Configuration"
  if (classId==164 and functionId==3):
    return "pyhausbus.de.hausbus.homeassistant.proxy.wiFi.commands.GetCurrentIp"
  if (classId==164 and functionId==129):
    return "pyhausbus.de.hausbus.homeassistant.proxy.wiFi.data.CurrentIp"
  if (classId==39 and functionId==203):
    return "pyhausbus.de.hausbus.homeassistant.proxy.helligkeitssensor.data.EvStatus"
  if (classId==39 and functionId==200):
    return "pyhausbus.de.hausbus.homeassistant.proxy.helligkeitssensor.data.EvDark"
  if (classId==39 and functionId==201):
    return "pyhausbus.de.hausbus.homeassistant.proxy.helligkeitssensor.data.EvLight"
  if (classId==39 and functionId==202):
    return "pyhausbus.de.hausbus.homeassistant.proxy.helligkeitssensor.data.EvBright"
  if (classId==39 and functionId==0):
    return "pyhausbus.de.hausbus.homeassistant.proxy.helligkeitssensor.commands.GetConfiguration"
  if (classId==39 and functionId==1):
    return "pyhausbus.de.hausbus.homeassistant.proxy.helligkeitssensor.commands.SetConfiguration"
  if (classId==39 and functionId==2):
    return "pyhausbus.de.hausbus.homeassistant.proxy.helligkeitssensor.commands.GetStatus"
  if (classId==39 and functionId==128):
    return "pyhausbus.de.hausbus.homeassistant.proxy.helligkeitssensor.data.Configuration"
  if (classId==39 and functionId==255):
    return "pyhausbus.de.hausbus.homeassistant.proxy.helligkeitssensor.data.EvError"
  if (classId==39 and functionId==129):
    return "pyhausbus.de.hausbus.homeassistant.proxy.helligkeitssensor.data.Status"
  if (classId==41 and functionId==200):
    return "pyhausbus.de.hausbus.homeassistant.proxy.powerMeter.data.EvLowPower"
  if (classId==41 and functionId==201):
    return "pyhausbus.de.hausbus.homeassistant.proxy.powerMeter.data.EvMediumPower"
  if (classId==41 and functionId==202):
    return "pyhausbus.de.hausbus.homeassistant.proxy.powerMeter.data.EvHighPower"
  if (classId==41 and functionId==255):
    return "pyhausbus.de.hausbus.homeassistant.proxy.powerMeter.data.EvError"
  if (classId==41 and functionId==0):
    return "pyhausbus.de.hausbus.homeassistant.proxy.powerMeter.commands.GetConfiguration"
  if (classId==41 and functionId==1):
    return "pyhausbus.de.hausbus.homeassistant.proxy.powerMeter.commands.SetConfiguration"
  if (classId==41 and functionId==2):
    return "pyhausbus.de.hausbus.homeassistant.proxy.powerMeter.commands.GetStatus"
  if (classId==41 and functionId==128):
    return "pyhausbus.de.hausbus.homeassistant.proxy.powerMeter.data.Configuration"
  if (classId==41 and functionId==129):
    return "pyhausbus.de.hausbus.homeassistant.proxy.powerMeter.data.Status"
  if (classId==41 and functionId==203):
    return "pyhausbus.de.hausbus.homeassistant.proxy.powerMeter.data.EvStatus"
  if (classId==22 and functionId==200):
    return "pyhausbus.de.hausbus.homeassistant.proxy.rGBDimmer.data.EvOff"
  if (classId==22 and functionId==201):
    return "pyhausbus.de.hausbus.homeassistant.proxy.rGBDimmer.data.EvOn"
  if (classId==22 and functionId==2):
    return "pyhausbus.de.hausbus.homeassistant.proxy.rGBDimmer.commands.SetColor"
  if (classId==22 and functionId==0):
    return "pyhausbus.de.hausbus.homeassistant.proxy.rGBDimmer.commands.GetConfiguration"
  if (classId==22 and functionId==1):
    return "pyhausbus.de.hausbus.homeassistant.proxy.rGBDimmer.commands.SetConfiguration"
  if (classId==22 and functionId==5):
    return "pyhausbus.de.hausbus.homeassistant.proxy.rGBDimmer.commands.GetStatus"
  if (classId==22 and functionId==128):
    return "pyhausbus.de.hausbus.homeassistant.proxy.rGBDimmer.data.Configuration"
  if (classId==22 and functionId==129):
    return "pyhausbus.de.hausbus.homeassistant.proxy.rGBDimmer.data.Status"
  if (classId==42 and functionId==200):
    return "pyhausbus.de.hausbus.homeassistant.proxy.taupunkt.data.EvLow"
  if (classId==42 and functionId==201):
    return "pyhausbus.de.hausbus.homeassistant.proxy.taupunkt.data.EvInRange"
  if (classId==42 and functionId==202):
    return "pyhausbus.de.hausbus.homeassistant.proxy.taupunkt.data.EvAbove"
  if (classId==42 and functionId==255):
    return "pyhausbus.de.hausbus.homeassistant.proxy.taupunkt.data.EvError"
  if (classId==42 and functionId==0):
    return "pyhausbus.de.hausbus.homeassistant.proxy.taupunkt.commands.GetConfiguration"
  if (classId==42 and functionId==1):
    return "pyhausbus.de.hausbus.homeassistant.proxy.taupunkt.commands.SetConfiguration"
  if (classId==42 and functionId==2):
    return "pyhausbus.de.hausbus.homeassistant.proxy.taupunkt.commands.GetStatus"
  if (classId==42 and functionId==128):
    return "pyhausbus.de.hausbus.homeassistant.proxy.taupunkt.data.Configuration"
  if (classId==42 and functionId==203):
    return "pyhausbus.de.hausbus.homeassistant.proxy.taupunkt.data.EvStatus"
  if (classId==42 and functionId==129):
    return "pyhausbus.de.hausbus.homeassistant.proxy.taupunkt.data.Status"
  if (classId==43 and functionId==200):
    return "pyhausbus.de.hausbus.homeassistant.proxy.rFIDReader.data.EvConnected"
  if (classId==43 and functionId==255):
    return "pyhausbus.de.hausbus.homeassistant.proxy.rFIDReader.data.EvError"
  if (classId==43 and functionId==0):
    return "pyhausbus.de.hausbus.homeassistant.proxy.rFIDReader.commands.GetConfiguration"
  if (classId==43 and functionId==1):
    return "pyhausbus.de.hausbus.homeassistant.proxy.rFIDReader.commands.SetConfiguration"
  if (classId==43 and functionId==129):
    return "pyhausbus.de.hausbus.homeassistant.proxy.rFIDReader.data.State"
  if (classId==43 and functionId==201):
    return "pyhausbus.de.hausbus.homeassistant.proxy.rFIDReader.data.EvData"
  if (classId==43 and functionId==3):
    return "pyhausbus.de.hausbus.homeassistant.proxy.rFIDReader.commands.GetLastData"
  if (classId==43 and functionId==130):
    return "pyhausbus.de.hausbus.homeassistant.proxy.rFIDReader.data.LastData"
  if (classId==43 and functionId==128):
    return "pyhausbus.de.hausbus.homeassistant.proxy.rFIDReader.data.Configuration"
  if (classId==43 and functionId==2):
    return "pyhausbus.de.hausbus.homeassistant.proxy.rFIDReader.commands.GetState"
  if (classId==44 and functionId==0):
    return "pyhausbus.de.hausbus.homeassistant.proxy.pIDController.commands.GetConfiguration"
  if (classId==44 and functionId==1):
    return "pyhausbus.de.hausbus.homeassistant.proxy.pIDController.commands.SetConfiguration"
  if (classId==44 and functionId==128):
    return "pyhausbus.de.hausbus.homeassistant.proxy.pIDController.data.Configuration"
  if (classId==44 and functionId==2):
    return "pyhausbus.de.hausbus.homeassistant.proxy.pIDController.commands.SetTargetValue"
  if (classId==44 and functionId==3):
    return "pyhausbus.de.hausbus.homeassistant.proxy.pIDController.commands.Enable"
  if (classId==44 and functionId==200):
    return "pyhausbus.de.hausbus.homeassistant.proxy.pIDController.data.EvOn"
  if (classId==44 and functionId==255):
    return "pyhausbus.de.hausbus.homeassistant.proxy.pIDController.data.EvError"
  if (classId==44 and functionId==201):
    return "pyhausbus.de.hausbus.homeassistant.proxy.pIDController.data.EvOff"
  if (classId==45 and functionId==2):
    return "pyhausbus.de.hausbus.homeassistant.proxy.modBusMaster.commands.GetRegisterConfiguration"
  if (classId==45 and functionId==3):
    return "pyhausbus.de.hausbus.homeassistant.proxy.modBusMaster.commands.SetRegisterConfiguration"
  if (classId==45 and functionId==129):
    return "pyhausbus.de.hausbus.homeassistant.proxy.modBusMaster.data.RegisterConfiguration"
  if (classId==45 and functionId==130):
    return "pyhausbus.de.hausbus.homeassistant.proxy.modBusMaster.data.GenericResponse"
  if (classId==45 and functionId==4):
    return "pyhausbus.de.hausbus.homeassistant.proxy.modBusMaster.commands.GenericCommand"
  if (classId==45 and functionId==0):
    return "pyhausbus.de.hausbus.homeassistant.proxy.modBusMaster.commands.GetConfiguration"
  if (classId==45 and functionId==1):
    return "pyhausbus.de.hausbus.homeassistant.proxy.modBusMaster.commands.SetConfiguration"
  if (classId==45 and functionId==128):
    return "pyhausbus.de.hausbus.homeassistant.proxy.modBusMaster.data.Configuration"
  if (classId==45 and functionId==255):
    return "pyhausbus.de.hausbus.homeassistant.proxy.modBusMaster.data.EvError"
  if (classId==36 and functionId==200):
    return "pyhausbus.de.hausbus.homeassistant.proxy.analogEingang.data.EvLow"
  if (classId==36 and functionId==201):
    return "pyhausbus.de.hausbus.homeassistant.proxy.analogEingang.data.EvInRange"
  if (classId==36 and functionId==202):
    return "pyhausbus.de.hausbus.homeassistant.proxy.analogEingang.data.EvHigh"
  if (classId==36 and functionId==203):
    return "pyhausbus.de.hausbus.homeassistant.proxy.analogEingang.data.EvStatus"
  if (classId==36 and functionId==0):
    return "pyhausbus.de.hausbus.homeassistant.proxy.analogEingang.commands.GetConfiguration"
  if (classId==36 and functionId==1):
    return "pyhausbus.de.hausbus.homeassistant.proxy.analogEingang.commands.SetConfiguration"
  if (classId==36 and functionId==2):
    return "pyhausbus.de.hausbus.homeassistant.proxy.analogEingang.commands.GetStatus"
  if (classId==36 and functionId==128):
    return "pyhausbus.de.hausbus.homeassistant.proxy.analogEingang.data.Configuration"
  if (classId==36 and functionId==129):
    return "pyhausbus.de.hausbus.homeassistant.proxy.analogEingang.data.Status"
  if (classId==165 and functionId==255):
    return "pyhausbus.de.hausbus.homeassistant.proxy.pCA9555.data.EvError"
  if (classId==48 and functionId==200):
    return "pyhausbus.de.hausbus.homeassistant.proxy.drucksensor.data.EvLow"
  if (classId==48 and functionId==201):
    return "pyhausbus.de.hausbus.homeassistant.proxy.drucksensor.data.EvInRange"
  if (classId==48 and functionId==202):
    return "pyhausbus.de.hausbus.homeassistant.proxy.drucksensor.data.EvHigh"
  if (classId==48 and functionId==203):
    return "pyhausbus.de.hausbus.homeassistant.proxy.drucksensor.data.EvStatus"
  if (classId==48 and functionId==0):
    return "pyhausbus.de.hausbus.homeassistant.proxy.drucksensor.commands.GetConfiguration"
  if (classId==48 and functionId==1):
    return "pyhausbus.de.hausbus.homeassistant.proxy.drucksensor.commands.SetConfiguration"
  if (classId==48 and functionId==2):
    return "pyhausbus.de.hausbus.homeassistant.proxy.drucksensor.commands.GetStatus"
  if (classId==48 and functionId==128):
    return "pyhausbus.de.hausbus.homeassistant.proxy.drucksensor.data.Configuration"
  if (classId==48 and functionId==129):
    return "pyhausbus.de.hausbus.homeassistant.proxy.drucksensor.data.Status"
  if (classId==49 and functionId==200):
    return "pyhausbus.de.hausbus.homeassistant.proxy.pT1000.data.EvLow"
  if (classId==49 and functionId==201):
    return "pyhausbus.de.hausbus.homeassistant.proxy.pT1000.data.EvInRange"
  if (classId==49 and functionId==202):
    return "pyhausbus.de.hausbus.homeassistant.proxy.pT1000.data.EvHigh"
  if (classId==49 and functionId==203):
    return "pyhausbus.de.hausbus.homeassistant.proxy.pT1000.data.EvStatus"
  if (classId==49 and functionId==255):
    return "pyhausbus.de.hausbus.homeassistant.proxy.pT1000.data.EvError"
  if (classId==49 and functionId==0):
    return "pyhausbus.de.hausbus.homeassistant.proxy.pT1000.commands.GetConfiguration"
  if (classId==49 and functionId==1):
    return "pyhausbus.de.hausbus.homeassistant.proxy.pT1000.commands.SetConfiguration"
  if (classId==49 and functionId==2):
    return "pyhausbus.de.hausbus.homeassistant.proxy.pT1000.commands.GetStatus"
  if (classId==49 and functionId==128):
    return "pyhausbus.de.hausbus.homeassistant.proxy.pT1000.data.Configuration"
  if (classId==49 and functionId==129):
    return "pyhausbus.de.hausbus.homeassistant.proxy.pT1000.data.Status"

  return "pyhausbus.GenericBusData"

def getBusClassNameForClass(classId):
  if (classId==16):
    return "pyhausbus.de.hausbus.homeassistant.proxy.Taster"
  if (classId==32):
    return "pyhausbus.de.hausbus.homeassistant.proxy.Temperatursensor"
  if (classId==19):
    return "pyhausbus.de.hausbus.homeassistant.proxy.Schalter"
  if (classId==17):
    return "pyhausbus.de.hausbus.homeassistant.proxy.Dimmer"
  if (classId==0):
    return "pyhausbus.de.hausbus.homeassistant.proxy.Controller"
  if (classId==18):
    return "pyhausbus.de.hausbus.homeassistant.proxy.Rollladen"
  if (classId==15):
    return "pyhausbus.de.hausbus.homeassistant.proxy.DigitalPort"
  if (classId==20):
    return "pyhausbus.de.hausbus.homeassistant.proxy.LogicalButton"
  if (classId==21):
    return "pyhausbus.de.hausbus.homeassistant.proxy.Led"
  if (classId==33):
    return "pyhausbus.de.hausbus.homeassistant.proxy.IRSensor"
  if (classId==160):
    return "pyhausbus.de.hausbus.homeassistant.proxy.DaliLine"
  if (classId==162):
    return "pyhausbus.de.hausbus.homeassistant.proxy.Ethernet"
  if (classId==34):
    return "pyhausbus.de.hausbus.homeassistant.proxy.Feuchtesensor"
  if (classId==1):
    return "pyhausbus.de.hausbus.homeassistant.proxy.PCServer"
  if (classId==2):
    return "pyhausbus.de.hausbus.homeassistant.proxy.Wetter"
  if (classId==14):
    return "pyhausbus.de.hausbus.homeassistant.proxy.ModbusSlave"
  if (classId==176):
    return "pyhausbus.de.hausbus.homeassistant.proxy.Gateway"
  if (classId==35):
    return "pyhausbus.de.hausbus.homeassistant.proxy.Counter"
  if (classId==163):
    return "pyhausbus.de.hausbus.homeassistant.proxy.SnmpAgent"
  if (classId==3):
    return "pyhausbus.de.hausbus.homeassistant.proxy.SystemTime"
  if (classId==90):
    return "pyhausbus.de.hausbus.homeassistant.proxy.CurrentReader"
  if (classId==91):
    return "pyhausbus.de.hausbus.homeassistant.proxy.TcpClient"
  if (classId==164):
    return "pyhausbus.de.hausbus.homeassistant.proxy.WiFi"
  if (classId==39):
    return "pyhausbus.de.hausbus.homeassistant.proxy.Helligkeitssensor"
  if (classId==41):
    return "pyhausbus.de.hausbus.homeassistant.proxy.PowerMeter"
  if (classId==22):
    return "pyhausbus.de.hausbus.homeassistant.proxy.RGBDimmer"
  if (classId==42):
    return "pyhausbus.de.hausbus.homeassistant.proxy.Taupunkt"
  if (classId==43):
    return "pyhausbus.de.hausbus.homeassistant.proxy.RFIDReader"
  if (classId==44):
    return "pyhausbus.de.hausbus.homeassistant.proxy.PIDController"
  if (classId==45):
    return "pyhausbus.de.hausbus.homeassistant.proxy.ModBusMaster"
  if (classId==36):
    return "pyhausbus.de.hausbus.homeassistant.proxy.AnalogEingang"
  if (classId==165):
    return "pyhausbus.de.hausbus.homeassistant.proxy.PCA9555"
  if (classId==48):
    return "pyhausbus.de.hausbus.homeassistant.proxy.Drucksensor"
  if (classId==49):
    return "pyhausbus.de.hausbus.homeassistant.proxy.PT1000"

  return "pyhausbus.GenericBusData"

