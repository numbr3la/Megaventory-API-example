import configparser


class ConfigFile:
    def __init__(self, file_path):
        self.config = configparser.ConfigParser()
        self.file_path = file_path
        self.load()

    def load(self):
        self.config.read(self.file_path)

    def get(self, section, key):
        return self.config.get(section, key)

    def set(self, section, key, value):
        self.config.set(section, key, value)
        self.save()