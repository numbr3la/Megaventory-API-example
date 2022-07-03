from sqlalchemy import Column, Integer, String
from src.JsonOperations import appendParamIfNotNone


class SupplierClient:
    name = Column(String)
    email = Column(String)
    shippingAddress = Column(String)
    phone = Column(String)
    clientId = Column(Integer)

    def __init__(self, name="", email="", shippingAddress="", phone=""):
        self.name = name
        self.email = email
        self.shippingAddress = shippingAddress
        self.phone = phone
        self.clientId = None


    def encodeToJSON(self):
        params = {
            'SupplierClientName': self.name,
            'SupplierClientEmail' : self.email,
            'SupplierClientShippingAddress1': self.shippingAddress,
            'SupplierClientPhone1': self.phone
        }
        appendParamIfNotNone(params, 'SupplierClientID', self.clientId)

        return params

    @staticmethod
    def decodeFromJSON(json):
        object = SupplierClient()
        object.name = json.get('SupplierClientName')
        object.email = json.get('SupplierClientEmail')
        object.shippingAddress = json.get('SupplierClientShippingAddress1')
        object.phone = json.get('SupplierClientPhone1')
        object.clientId = json.get('SupplierClientID')

        return object