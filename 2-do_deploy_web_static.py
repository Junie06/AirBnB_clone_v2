#!/usr/bin/python3
"""
A module for Fabric script that generates a .tgz archive.
"""
import os
from datetime import datetime
from fabric.api import local, runs_once


@runs_once
def do_pack():
    """Archives the static files"""
    if not os.path.isdir("versions"):
        os.mkdir("versions")
    dt = datetime.now()
    fab_file = "versions/web_static_{}{}{}{}{}{}.tgz".format(
        dt.year,
        dt.month,
        dt.day,
        dt.hour,
        dt.minute,
        dt.second
    )
    try:
        print("Packing web_static to {}".format(fab_file))
        local("tar -cvzf {} web_static".format(fab_file))
        size = os.stat(fab_file).st_size
        print("web_static packed: {} -> {} Bytes".format(fab_file, size))
    except Exception:
        output = None
    return output

def do_deploy(archive_path):
    """Deploys the static files to the host servers
    """
    if not os.path.exists(archive_path):
        return False
    file_name = os.path.basename(archive_path)
    folder_name = file_name.replace(".tgz", "")
    folder_path = "/data/web_static/releases/{}/".format(folder_name)
    success = False
    try:
        put(archive_path, "/tmp/{}".format(file_name))
        run("sudo mkdir -p {}".format(folder_path))
        run("sudo tar -xzf /tmp/{} -C {}".format(file_name, folder_path))
        run("sudo rm -rf /tmp/{}".format(file_name))
        run("sudo mv {}web_static/* {}".format(folder_path, folder_path))
        run("sudo rm -rf {}web_static".format(folder_path))
        run("sudo rm -rf /data/web_static/current")
        run("sudo ln -s {} /data/web_static/current".format(folder_path))
        print('New version deployed!')
        success = True
    except Exception:
        success = False
    return success
