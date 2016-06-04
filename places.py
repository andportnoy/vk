from . import core


def getCheckins(latitude=None, longitude=None, place=None, user_id=None, offset=None,
                count=None, timestamp=None, friends_only=None, need_places=None):

    params_dict = core.params_dict_from_locals(locals())
    result = core.vdr('places.getCheckins', params_dict)

    return result
