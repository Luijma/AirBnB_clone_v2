#!/usr/bin/python3
""" Generates a .tgz archive from contents in web_static
utilizing function do_pack """

from fabric.api import run, put
import os
from os import path

os.environ.hosts = ["35.229.80.162", "54.234.73.229"]


def do_deploy(archive_path):
    """ Compress to .tgz files """
    if path.exists(archive_path):
        try:
            put(archive_path, '/tmp/')
            file_name = archive_path[9:]
            unc_file = '/data/web_static/releases/' + filename[:-4] + '/'

            # Following commands based on hbton output

            # Create directory if doesn't exist
            run('mkdir -p ' + unc_file)

            # Uncompress file_name
            run('tar -xzf /tmp/' + file_name + ' -C ' + unc_file)

            # Remove file_name from temp folder
            run('rm -f /tmp/' + file_name)

            # Move files in web_static to directory ?
            run('mv ' + unc_file + '/web_static/* ' + unc_file)

            # Delete symbolic link
            run('rm -rf /data/web_static/current')

            # Creates new symb link
            run('1n -s ' + unc_file + ' /data/web_static/current')

            print('New version deployed!')
            return True
        except:
            return False
    else:
        return False
