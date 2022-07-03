from src.model.ConfigFile import ConfigFile
import src.megaventory_api.MegaventoryApiRequest as api


def supplierClientUpdate(configFile, supplierClient):

    request = api.MegaventoryApiRequest(configFile, '/SupplierClient/SupplierClientUpdate', method='POST')
    request.appendToRequest('mvSupplierClient', supplierClient.encodeToJSON())
    request.appendToRequest('mvRecordAction', 'Insert')
    response = request.sendRequest()

    return response