import os
from collections import defaultdict
from typing import List, Dict, Optional
from pyhausbus.de.hausbus.homeassistant.proxy.controller.params.EFirmwareId import EFirmwareId
from pyhausbus.HausBusUtils import LOGGER
import threading

def load_file(path: str) -> list[str]:
    try:
        with open(path, "r", encoding="latin1") as file:
            return [line.strip() for line in file if line.strip()]
    except FileNotFoundError:
        LOGGER.error(f"Datei nicht gefunden: {path}")
        return []
    except Exception as e:
        LOGGER.error(f"Fehler beim Laden der Datei {path}: {e}")
        return []

class Templates:
    template_root_dir = os.path.join(os.path.dirname(__file__), "templates")
    LOGGER.debug(f"templateRootDir = {template_root_dir}")
    filter_non_existing = True
    _instance = None
    class_mappings: Dict[str, str] = {}

    def __init__(self):
        self.module_types: Dict['ModuleType', str] = {}
        self.feature_names: Dict['ModuleType', List['FeatureEntry']] = {}

        thread = threading.Thread(target=self._load_templates, daemon=True)
        thread.start()
     
    def _load_templates(self):   
        try:
            lines = load_file(os.path.join(self.template_root_dir, "deviceTypes.def"))
            for line in lines:
                tokens = line.split(",")
                firmware_id = EFirmwareId.value_of(tokens[0])
                fcke = int(tokens[1].replace("0x", ""), 16)
                name = tokens[2]
                self.module_types[ModuleType(firmware_id, fcke)] = name


            root_dir = self.template_root_dir
            if not os.path.exists(root_dir):
                root_dir = "../JavaLib/" + self.template_root_dir

            for act_file in os.listdir(root_dir):
                if act_file.endswith(".tpl"):
                    tokens = act_file.split("_")
                    firmware_id = EFirmwareId.value_of(tokens[0])
                    fcke = int(tokens[1], 16)
                    features = []
                    self.feature_names[ModuleType(firmware_id, fcke)] = features

                    lines = load_file(os.path.join(root_dir, act_file))
                    for line in lines:
                        if line.strip():
                            features.append(FeatureEntry(line))

            '''for module_type, features in self.feature_names.items():
              print(module_type)
              for entry in features:
                print(entry)
              
            quit()'''

            lines = load_file(os.path.join(self.template_root_dir, "classMapping.def"))
            if lines:
                for line in lines:
                    tokens = line.split(",")
                    orig_name = tokens[0]
                    mapped_name = tokens[1]
                    Templates.class_mappings[orig_name] = mapped_name
            LOGGER.debug(f"module types = {len(self.module_types)}")
            LOGGER.debug(f"feature names = {len(self.feature_names)}")
        except Exception as e:
            LOGGER.error(f"Fehler beim Initialisieren der Templates: {e}")

    @classmethod
    def get_instance(cls):
        if cls._instance is None:
            cls._instance = Templates()
        return cls._instance

    def get_feature_name_from_template(self, firmware_id, fcke, class_id, instance_id) -> Optional[str]:
        if fcke != -1:
            ''' print("get_feature_name_from_template firmware_id = ",firmware_id," fcke = ",fcke," class_id = ",class_id," instance_id = ",instance_id)'''
            features = self.get_features(firmware_id, fcke)

            if features:
                for entry in features:
                    if entry.suits(class_id, instance_id):
                        return entry.name
        return None

    def getModuleName(self, firmwareId: EFirmwareId, fcke: int):
      for entry, name in self.module_types.items():
        if entry.suits(firmwareId, fcke):
            return name
      return None
    
    def get_features(self, firmware_id, fcke) -> Optional[List['FeatureEntry']]:
        for module_type, features in self.feature_names.items():
            if module_type.suits(firmware_id, fcke):
                return list(features)
        return None


class FeatureEntry:
    def __init__(self, line: str):
        tokens = line.split(",")
        self.class_id = int(tokens[0])
        self.instance_id = int(tokens[1])
        self.name = tokens[2]
        self.loxone_aktor_type = tokens[3] if len(tokens) > 3 else ""

    def suits(self, class_id: int, instance_id: int) -> bool:
        return self.class_id == class_id and self.instance_id == instance_id

    def __str__(self):
        return f"FeatureEntry(classId={self.class_id}, instanceId={self.instance_id}, name='{self.name}', loxoneAktorType='{self.loxone_aktor_type}')"


class ModuleType:
    def __init__(self, firmware_id, fcke):
        self.firmware_id = firmware_id
        self.fcke = fcke

    def suits(self, check_firmware_id, check_fcke) -> bool:
        if check_fcke != self.fcke:
            return False
        if check_firmware_id == self.firmware_id:
            return True
        if check_firmware_id.name.startswith("HB") and self.firmware_id.name.startswith("HB"):
            return True
        return False

    def __eq__(self, other):
        if not isinstance(other, ModuleType):
            return False
        return self.firmware_id == other.firmware_id and self.fcke == other.fcke

    def __hash__(self):
        return hash((self.firmware_id, self.fcke))

    def __str__(self):
        return f"ModuleType(firmwareId={self.firmware_id}, fcke={self.fcke})"
