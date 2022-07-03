from sqlalchemy import Column, String, Integer
from src.JsonOperations import appendParamIfNotNone


class InventoryLocation:
    abbreviation = Column(String)
    name = Column(String)
    address = Column(String)
    inventoryLocationID = Column(Integer)

    def __init__(self, abbreviation="", name="", address=""):
        self.abbreviation = abbreviation
        self.name = name
        self.address = address
        self.inventoryLocationID = None


    def encodeToJSON(self):

        params = {
        'InventoryLocationAbbreviation': self.abbreviation,
        'InventoryLocationName' : self.name,
        'InventoryLocationAddress': self.address,
        }

        return params
    

    @staticmethod
    def decodeFromJSON(json):
        object = InventoryLocation()
        object.abbreviation = json.get('InventoryLocationAbbreviation')
        object.name = json.get('InventoryLocationName')
        object.address = json.get('InventoryLocationAddress')
        object.inventoryLocationID = json.get('InventoryLocationID')
        return object