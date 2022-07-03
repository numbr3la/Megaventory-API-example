from sqlalchemy import Column, Integer, String
import src.model.entity.SalesOrderRow as SalesOrderRow
from src.JsonOperations import appendParamIfNotNone


class SalesOrder:
    salesOrderTypeId = Column(Integer)
    salesOrderClientID = Column(Integer)
    salesOrderDetails = SalesOrderRow.SalesOrderRow() # TODO: Create custom type
    salesOrderStatus =  Column(String)
    salesOrderInventoryLocationID = Column(Integer)

    def __init__(self, salesOrderTypeId=0, salesOrderClientID=0, salesOrderDetails=None):
        self.salesOrderTypeId = salesOrderTypeId
        self.salesOrderClientID = salesOrderClientID
        self.salesOrderDetails = salesOrderDetails
        self.salesOrderStatus = None
        self.salesOrderInventoryLocationID = None


    def encodeToJSON(self):

        params = {
        'SalesOrderTypeId': self.salesOrderTypeId,
        'SalesOrderClientID' : self.salesOrderClientID,
        'SalesOrderDetails': self.salesOrderDetails.encodeToJSON()
        }

        appendParamIfNotNone(params, 'SalesOrderStatus', self.salesOrderStatus)
        appendParamIfNotNone(params, 'SalesOrderInventoryLocationID', self.salesOrderInventoryLocationID)

        return params


    @staticmethod
    def decodeFromJSON(json):
        object = SalesOrder()
        object.salesOrderTypeId = json.get('SalesOrderTypeId')
        object.salesOrderClientID = json.get('SalesOrderClientID')
        object.salesOrderDetails.decodeFromJson(json.get('SalesOrderDetails'))
        object.salesOrderStatus = json.get('SalesOrderStatus')
        object.salesOrderInventoryLocationID = json.get('SalesOrderInventoryLocationID')

        return object

        