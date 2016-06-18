from . import _core


def getCheckins(access_token=None, latitude=None, longitude=None,
                place=None, user_id=None, offset=None, count=None,
                timestamp=None, friends_only=None, need_places=None):

    params_dict = _core.params_dict_from_locals(locals())
    result = _core.vdr('places.getCheckins', params_dict)

    return result
