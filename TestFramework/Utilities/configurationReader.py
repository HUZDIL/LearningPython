import configparser


class Reader:

    def reader(self):
        config = configparser.ConfigParser()
        config.read('config.properties')
        print(config.get('URLSection', 'url'))