#!/usr/bin/python
from configparser import ConfigParser
#from ConfigParser import SafeConfigParser
#parser = SafeConfigParser()
 
def config(filename='/usr/local/freeswitch/scripts/database.ini', section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)
 
    # get section, default to postgresql
    db = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            db[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file. sections are:'.format(section, filename,parser.sections()))
 
    return db 
