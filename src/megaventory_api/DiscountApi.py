from src.model.ConfigFile import ConfigFile
import src.megaventory_api.MegaventoryApiRequest as api


def discountUpdate(configFile, discount):

    request = api.MegaventoryApiRequest(configFile, '/Discount/DiscountUpdate', method='POST')
    request.appendToRequest('mvDiscount', discount.encodeToJSON())
    request.appendToRequest('mvRecordAction', 'Insert')
    response = request.sendRequest()

    return response