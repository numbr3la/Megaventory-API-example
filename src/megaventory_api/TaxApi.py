from src.model.ConfigFile import ConfigFile
import src.megaventory_api.MegaventoryApiRequest as api


def taxUpdate(configFile, tax):

    request = api.MegaventoryApiRequest(configFile, '/Tax/TaxUpdate', method='POST')
    request.appendToRequest('mvTax', tax.encodeToJSON())
    request.appendToRequest('mvRecordAction', 'Insert')
    response = request.sendRequest()

    return response