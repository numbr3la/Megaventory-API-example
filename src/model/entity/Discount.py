from sqlalchemy import Column, String, Float


class Discount:
    name = Column(String)
    description = Column(String)
    value = Column(Float)

    def __init__(self, name="", description="", value=0.0):
        self.name = name
        self.description = description
        self.value = value


    def encodeToJSON(self):
        return {
            'DiscountName': self.name,
            'DiscountDescription' : self.description,
            'DiscountValue': self.value,
        }