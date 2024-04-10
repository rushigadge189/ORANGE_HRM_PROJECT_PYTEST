import configparser

config=configparser.RawConfigParser();

filepath = "D:\\PYTHON CT15\\ORANGEH_PROJECT\\configuration\\config.ini" ;

config.read(filepath) ;

class ReadConfig():

    @staticmethod
    def getUserName():
        username=config.get('common data', 'username')
        return username ;

    @staticmethod
    def getPassword():
        password=config.get('common data', 'password') ;
        return password ;