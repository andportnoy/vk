from . import core


def get_server_time():
    return core.vdr('utils.getServerTime')
