#!/usr/bin/python3
""" Generates a .tgz archive from contents in web_static
utilizing function do_pack """

from fabric.api import local
from datetime import datetime


def do_pack():
    """ Compress to .tgz files """
    try:
        local("mkdir -p versions")
        now = datetime.now()
        date = now.strftime("%Y%m%d%H%M%S")
        file_name = "versions/web_static_{}.tgz".format(date)
        local("tar -cvzf {} web_static".format(file_name))
        return file_name
    except:
        return None
