from src.model.ConfigFile import ConfigFile
import src.megaventory_api.MegaventoryApiRequest as api


def inventoryLocationUpdate(configFile, inventoryLocation):

    request = api.MegaventoryApiRequest(configFile, '/InventoryLocation/InventoryLocationUpdate', method='POST')
    request.appendToRequest('mvInventoryLocation', inventoryLocation.encodeToJSON())
    request.appendToRequest('mvRecordAction', 'Insert')
    response = request.sendRequest()

    return response