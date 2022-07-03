from sqlalchemy import Column, Float, String

from src.model.entity.Product import Product


class SalesOrderRow:
    salesOrderRowProductSKU = Column(String)
    salesOrderRowQuantity = Column(Float)
    salesOrderRowShippedQuantity = Column(Float)
    salesOrderRowInvoicedQuantity = Column(Float)
    salesOrderRowUnitPriceWithoutTaxOrDiscount = Column(Float)


    def __init__(self, salesOrderRowProductSKU="", salesOrderRowQuantity=0,
            salesOrderRowShippedQuantity=0, salesOrderRowInvoicedQuantity=0,
            salesOrderRowUnitPriceWithoutTaxOrDiscount=0):

        self.salesOrderRowProductSKU = salesOrderRowProductSKU
        self.salesOrderRowQuantity = salesOrderRowQuantity
        self.salesOrderRowShippedQuantity = salesOrderRowShippedQuantity
        self.salesOrderRowInvoicedQuantity = salesOrderRowInvoicedQuantity
        self.salesOrderRowUnitPriceWithoutTaxOrDiscount = salesOrderRowUnitPriceWithoutTaxOrDiscount



    def __init__(self, product=Product(), salesOrderRowQuantity=0,
        salesOrderRowShippedQuantity=0, salesOrderRowInvoicedQuantity=0):

        self.salesOrderRowProductSKU = product.SKU
        self.salesOrderRowQuantity = salesOrderRowQuantity
        self.salesOrderRowShippedQuantity = salesOrderRowShippedQuantity
        self.salesOrderRowInvoicedQuantity = salesOrderRowInvoicedQuantity
        self.salesOrderRowUnitPriceWithoutTaxOrDiscount = product.salesPrice



    def encodeToJSON(self):
        return {
            'SalesOrderRowProductSKU': self.salesOrderRowProductSKU,
            'SalesOrderRowQuantity' : self.salesOrderRowQuantity,
            'SalesOrderRowShippedQuantity': self.salesOrderRowShippedQuantity,
            'SalesOrderRowInvoicedQuantity': self.salesOrderRowInvoicedQuantity,
            'SalesOrderRowUnitPriceWithoutTaxOrDiscount': self.salesOrderRowUnitPriceWithoutTaxOrDiscount
        }

    # TODO: Implement decodeFromJSON