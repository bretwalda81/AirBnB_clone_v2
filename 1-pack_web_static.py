#!/usr/bin/python3

from fabric.api import local
import datetime


def do_pack():
    current_time = datetime.datetime.now()
    archive_name = ('web_static_' + str(current_time.year) +
                    str(current_time.month) + str(time.day) +
                    str(time.hour) + str(time.minute) +
                    str(time.second) + '.tgz')

    local('mkdir -p versions')
    if local('tar -czvf versions/{} web_static'.format('archive_name')):
        return 'versions/{}'.format(archive_name)
    else:
        return None
