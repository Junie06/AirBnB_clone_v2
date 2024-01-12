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
