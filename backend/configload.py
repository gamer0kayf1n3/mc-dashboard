import configparser
import os

config = configparser.ConfigParser()
config.read('config.conf')

class Config:
    PAPER_VERSION = config.get('DEFAULT', 'PAPER_VERSION')
    PAPER_BUILD = config.get('DEFAULT', 'PAPER_BUILD')
    RCON_PORT = config.getint('DEFAULT', 'RCON_PORT')
    RCON_PASSWORD = config.get('DEFAULT', 'RCON_PASSWORD')