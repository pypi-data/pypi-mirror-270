# -*- encoding: utf-8 -*-
import configparser
import os

class My_Parser(configparser.ConfigParser):

    def as_dict(self, section_name):
        key_dict = {}
        key_list = self.items(section_name)
        for key in key_list:
            key_dict[key[0]] = key[1]
        return key_dict

def get_config():
    config_path="config.ini"
    if not os.path.exists(config_path): print('没有配置文件')
    con = My_Parser()
    con.read(config_path, encoding='utf-8')
    return con

