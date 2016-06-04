from . import core


def get(access_token=None, user_id=None, order=None,
        count=None, offset=None, fields=None, name_case=None):

    params_dict = core.params_dict_from_locals(locals())
    result = core.vdr('friends.get', params_dict)

    return result