<<<<<<< HEAD
#!/usr/bin/python3
"""
do_pack(): Generates a .tgz archive from the
contents of the web_static folder
do_deploy(): Distributes an archive to a web server
deploy (): Creates and distributes an archive to a web server
"""

from fabric.operations import local, run, put
from datetime import datetime
import os
from fabric.api import env
import re


env.hosts = ['54.152.60.141', '100.25.183.111']


def do_pack():
    """Function to compress files in an archive"""
    local("mkdir -p versions")
    filename = "versions/web_static_{}.tgz".format(datetime.strftime(
                                                   datetime.now(),
                                                   "%Y%m%d%H%M%S"))
    result = local("tar -cvzf {} web_static"
                   .format(filename))
    if result.failed:
        return None
    return filename


def do_deploy(archive_path):
    """Function to distribute an archive to a server"""
    if not os.path.exists(archive_path):
        return False
    rex = r'^versions/(\S+).tgz'
    match = re.search(rex, archive_path)
    filename = match.group(1)
    res = put(archive_path, "/tmp/{}.tgz".format(filename))
    if res.failed:
        return False
    res = run("mkdir -p /data/web_static/releases/{}/".format(filename))
    if res.failed:
        return False
    res = run("tar -xzf /tmp/{}.tgz -C /data/web_static/releases/{}/"
              .format(filename, filename))
    if res.failed:
        return False
    res = run("rm /tmp/{}.tgz".format(filename))
    if res.failed:
        return False
    res = run("mv /data/web_static/releases/{}"
              "/web_static/* /data/web_static/releases/{}/"
              .format(filename, filename))
    if res.failed:
        return False
    res = run("rm -rf /data/web_static/releases/{}/web_static"
              .format(filename))
    if res.failed:
        return False
    res = run("rm -rf /data/web_static/current")
    if res.failed:
        return False
    res = run("ln -s /data/web_static/releases/{}/ /data/web_static/current"
              .format(filename))
    if res.failed:
        return False
    print('New version deployed!')
    return True


def deploy():
    """Creates and distributes an archive to a web server"""
    filepath = do_pack()
    if filepath is None:
        return False
    d = do_deploy(filepath)
    return d
=======
bric script (based on the file 1-pack_web_static.py)
that distributes an archive to your web servers,
using the function do_deploy
"""
import time
import os
from fabric.api import *
from fabric.operations import run, put


env.hosts = ['34.138.195.126', '35.185.8.133']
env.user = 'ubuntu'
env.key_filename = '~/.ssh/id_rsa'


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


def do_deploy(archive_path):
    """distributes an archive to my web servers"""
    if not os.path.exists(archive_path):
        return False
    try:
        # Upload archive
        put(archive_path, '/tmp/')

        # Create a target dir without the file extension
        timestamp = time.strftime("%Y%m%d%H%M%S")
        run(
            'sudo mkdir -p /data/web_static/releases/web_static_{:s}/'.
            format(timestamp))

        # uncompress archive to the targed dir
        run('sudo tar xzvf /tmp/web_static_{:s}.tgz --directory\
            /data/web_static/releases/web_static_{:s}/'.
            format(timestamp, timestamp))

        # delete the archive from the web server
        run('sudo rm /tmp/web_static_{:s}.tgz'.format(timestamp))

        # move contents into host web_static
        run('sudo mv /data/web_static/releases/web_static_{:s}/web_static/*\
            /data/web_static/releases/web_static_{}/'.format(
            timestamp, timestamp))

        # remove irrelevant web_static dir
        run('sudo rm -rf /data/web_static/releases/web_static_{}/web_static'.
            format(timestamp))

        # delete the initial symbolic link from the web server
        run('sudo rm -rf /data/web_static/current')

        # create a new symbolic link
        run('sudo ln -s /data/web_static/releases/web_static_{:s}/ \
            /data/web_static/current'.format(
                timestamp))
    except BaseException:
        return False
    # if all that succeeded, return True
    return True

def deploy():
    """
    creates and distributes an archive to my web servers
    """
    created_archive = do_pack()
    if not created_archive:
        return False
    return do_deploy(created_archive)
>>>>>>> d9300d757dec339740964d514bd5966b2aa4deb5
