from sqlalchemy import Column, Numeric, String


class Product:
    SKU = Column(String)
    description = Column(String)
    salesPrice = Column(Numeric)
    purchasePrice = Column(Numeric)

    def __init__(self, SKU="", description="", salesPrice=0, purchasePrice=0):
        self.SKU = SKU
        self.description = description
        self.salesPrice = salesPrice
        self.purchasePrice = purchasePrice


    def encodeToJSON(self):
        return {
            'ProductSKU': self.SKU,
            'ProductDescription': self.description,
            'ProductSellingPrice': self.salesPrice,
            'ProductPurchasePrice': self.purchasePrice
        }
