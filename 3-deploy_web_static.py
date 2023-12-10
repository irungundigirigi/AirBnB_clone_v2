#!/usr/bin/python3
import os.path
from datetime import datetime
from fabric.api import env, local, put, run

env.hosts = ['54.162.46.205', '107.23.64.101']

def do_pack():
    """Create a tar gzipped archive of the directory web_static."""
    # Get the current UTC time
    dt = datetime.utcnow()
    # Generate a unique file name based on the timestamp
    file = "versions/web_static_{}{}{}{}{}{}.tgz".format(dt.year,
                                                         dt.month,
                                                         dt.day,
                                                         dt.hour,
                                                         dt.minute,
                                                         dt.second)
    # Create the 'versions' directory if it doesn't exist
    if os.path.isdir("versions") is False:
        # Create the 'versions' directory and handle failure
        if local("mkdir -p versions").failed is True:
            return None
    # Create a tar gzipped archive of the 'web_static' directory
    if local("tar -cvzf {} web_static".format(file)).failed is True:
        return None
    # Return the path to the created archive
    return file

def do_deploy(archive_path):
    """Distribute an archive to a web server."""
    # Check if the specified archive file exists
    if os.path.isfile(archive_path) is False:
        return False
    # Extract file and directory names from the archive path
    file = archive_path.split("/")[-1]
    name = file.split(".")[0]

    # Upload the archive to the remote server
    if put(archive_path, "/tmp/{}".format(file)).failed is True:
        return False
    # Remove the existing directory with the same name on the remote server
    if run("rm -rf /data/web_static/releases/{}/".format(name)).failed is True:
        return False
    # Create a new directory on the remote server for the new release
    if run("mkdir -p /data/web_static/releases/{}/".format(name)).failed is True:
        return False
    # Extract the contents of the archive to the new release directory
    if run("tar -xzf /tmp/{} -C /data/web_static/releases/{}/".format(file, name)).failed is True:
        return False
    # Remove the temporary archive file on the remote server
    if run("rm /tmp/{}".format(file)).failed is True:
        return False
    # Move the contents of the 'web_static' directory to the new release directory
    if run("mv /data/web_static/releases/{}/web_static/* /data/web_static/releases/{}/".format(name, name)).failed is True:
        return False
    # Remove the now-empty 'web_static' directory from the new release directory
    if run("rm -rf /data/web_static/releases/{}/web_static".format(name)).failed is True:
        return False
    # Remove the existing symbolic link to 'current'
    if run("rm -rf /data/web_static/current").failed is True:
        return False
    # Create a new symbolic link 'current' pointing to the new release directory
    if run("ln -s /data/web_static/releases/{}/ /data/web_static/current".format(name)).failed is True:
        return False
    # Return True on successful deployment
    return True

def deploy():
    """Create and distribute an archive to a web server."""
    # Create an archive
    file = do_pack()
    # If archive creation fails, return False
    if file is None:
        return False
    # Deploy the created archive
    return do_deploy(file)

