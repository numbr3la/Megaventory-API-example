from src.model.ConfigFile import ConfigFile
import src.megaventory_api.MegaventoryApiRequest as api


def salesOrderUpdate(configFile, salesOrder):

    request = api.MegaventoryApiRequest(configFile, '/SalesOrder/SalesOrderUpdate', method='POST')
    request.appendToRequest('mvSalesOrder', salesOrder.encodeToJSON())
    request.appendToRequest('mvRecordAction', 'Insert')
    response = request.sendRequest()

    return response