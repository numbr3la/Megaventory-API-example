from flask import Flask
from src.model.ConfigFile import ConfigFile
from src.RestApiController import *


from src.megaventory_api.ProductApi import productUpdate


app = Flask(__name__,
            static_url_path='', 
            static_folder='web/static',
            template_folder='web/templates')
            
app.register_blueprint(website)

appConfiguration = ConfigFile('config.ini')



def setAndRunApp():

    host = appConfiguration.get('GENERAL', 'host')
    port = appConfiguration.get('GENERAL', 'port')

    app.run(debug=True)
    app.run(host=host, port=port)




if __name__ == '__main__':

    print('Load config file...')
    appConfiguration.load()

    print('Starting server...')
    setAndRunApp()