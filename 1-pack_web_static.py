<<<<<<< HEAD
#!/usr/bin/python3
"""Generates a .tgz archive from the
contents of the web_static folder"""

from fabric.operations import local
from datetime import datetime


def do_pack():
    """Function to compress files"""
    local("mkdir -p versions")
    result = local("tar -cvzf versions/web_static_{}.tgz web_static"
                   .format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")),
                   capture=True)
    if result.failed:
        return None
    return result
=======
bric script that generates a .tgz archive from contents
of the web_static folder.
All files in the folder web_static must be added to the final archive
name of the archive created must be
web_static_<year><month><day><hour><minute><second>.tgz
The function do_pack must return the archive path if
the archive has been correctly generated.
Otherwise, it should return None
"""
import time
from fabric.api import local


def do_pack():
    """generates a .tgz archive"""
    try:
        local("mkdir -p versions")
        local("tar -cvzf versions/web_static_{:s}.tgz web_static/".
              format(time.strftime("%Y%m%d%H%M%S")))
        return "versions/web_static_{:s}.tgz".\
            format(time.strftime("%Y%m%d%H%M%S"))
    except BaseException:
        return None
>>>>>>> d9300d757dec339740964d514bd5966b2aa4deb5
