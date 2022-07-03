from src.model.ConfigFile import ConfigFile
import src.megaventory_api.MegaventoryApiRequest as api


def productUpdate(configFile, product):

    request = api.MegaventoryApiRequest(configFile, '/Product/ProductUpdate', method='POST')
    request.appendToRequest('mvProduct', product.encodeToJSON())
    request.appendToRequest('mvRecordAction', 'Insert')
    response = request.sendRequest()

    return response