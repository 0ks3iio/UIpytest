import configparser
import os


class ReadIni:

    def __init__(self):
        self.cf = configparser.ConfigParser()
        self.file_name = os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)) + '/config.ini'
        self.cf.read(self.file_name)

    def get_value(self, node, key):
        data = self.cf.get(node, key)
        return data

    def config_options(self, section):
        '''读取配置文件某section下所有键'''
        data = dict(self.cf.items(section))
        return data




