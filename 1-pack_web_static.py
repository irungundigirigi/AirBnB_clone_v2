#!/usr/bin/python3
# creates archive from the web_static folder

from fabric.api import local
from time import strftime
from datetime import date

def do_pack():
    """ script generates archive of contents of web_static folder """
    dir_name = strftime("%Y%m%d%H%M%S")

    try:
        local("mkdir -p versions")
        local("tar -czvf versions/web_static_{}.tgz".format(dir_name))
        return "versions/web_static_{}.tgz".format(dir_name)
    except Exception as e:
        return None