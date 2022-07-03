from src.model.entity.SalesOrderRow import SalesOrderRow
from src.model.ConfigFile import ConfigFile

from src.model.entity import (Product, SupplierClient, InventoryLocation,
    InventoryLocation, Tax, Discount, SalesOrder)
from src.megaventory_api import (ProductApi, SupplierClientApi,
    InventoryLocationApi, TaxApi, DiscountApi, SalesOrderApi)




class Test:

    def __init__(self):
        self.configFile = None
        self.product = None
        self.client = None
        self.inventoryLocation = None
        self.tax = None
        self.discount = None
        self.salesOrderDetails = None
        self.salesOrder = None  



    def validateResponse(self, response):
        if int(response['ResponseStatus']['ErrorCode']) != 0:
            raise Exception('Response status error code: ' +
                str(response['ResponseStatus']['ErrorCode']) + '\n' +
                str(response['ResponseStatus']['Message']))



    def createAndUpdateEntitiesByApi(self):

        try:
            # product
            self.product = Product.Product('1112256', 'Nike shoes', 99.99, 44.99)
            response = ProductApi.productUpdate(self.configFile, self.product)
            self.validateResponse(response)

            # client
            self.client = SupplierClient.SupplierClient('babis', 'babis@exampletest.com', 'Example 8, Athens', '1235698967')
            response = SupplierClientApi.supplierClientUpdate(self.configFile, self.client)
            self.validateResponse(response)
            self.client = SupplierClient.SupplierClient.decodeFromJSON(response['mvSupplierClient'])

            # location
            self.inventoryLocation = InventoryLocation.InventoryLocation('Test', 'Test Project Location', 'Example 20, Athens')
            response = InventoryLocationApi.inventoryLocationUpdate(self.configFile, self.inventoryLocation)
            self.validateResponse(response)
            self.inventoryLocation = InventoryLocation.InventoryLocation.decodeFromJSON(response['mvInventoryLocation'])

            # tax
            self.tax = Tax.Tax('VAT', 'VAT GR', 24.0)
            response = TaxApi.taxUpdate(self.configFile, self.tax)
            self.validateResponse(response)

            # discount
            self.discount = Discount.Discount('Loyalty', 'Loyalty Customer Discount', 50.0)
            response = DiscountApi.discountUpdate(self.configFile, self.discount)
            self.validateResponse(response)

            # sales order and order details
            self.salesOrderDetails = SalesOrderRow(
            product=self.product,
            salesOrderRowQuantity=1,
            salesOrderRowShippedQuantity=1,
            salesOrderRowInvoicedQuantity=1)

            self.salesOrder = SalesOrder.SalesOrder(
            salesOrderTypeId=3,
            salesOrderClientID=self.client.clientId,
            salesOrderDetails=self.salesOrderDetails)

            self.salesOrder.salesOrderInventoryLocationID = self.inventoryLocation.inventoryLocationID
            self.salesOrder.salesOrderStatus = 'Verified'
            self.validateResponse(response)

        except Exception as e:
            print('Error: ', repr(e), flush=True)


    def run(self):

        self.configFile = ConfigFile('config.ini')
        self.createAndUpdateEntitiesByApi()