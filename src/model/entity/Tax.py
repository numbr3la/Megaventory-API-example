from sqlalchemy import Column, String, Float


class Tax:
    name = Column(String)
    description = Column(String)
    value = Column(Float)

    def __init__(self, name="", description="", value=0.0):
        self.name = name
        self.description = description
        self.value = value


    def encodeToJSON(self):
        return {
            'TaxName': self.name,
            'TaxDescription': self.description,
            'TaxValue': self.value,
        }

    # TODO: Implement decodeFromJSON