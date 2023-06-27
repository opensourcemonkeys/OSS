import configparser


config = configparser.ConfigParser()
config.read('./Config/ServerConfig.cfg')
class ConfigReader:
    
    def GetServerConf(key:str):
        sectionName="ServerConfig"
        config.sections()
        result = config[sectionName][key]
        return result

    def GetServerNodeList():
        print("")