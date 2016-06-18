from . import _core

def get(access_token=None, user_id=None, order=None,
        count=None, offset=None, fields=None, name_case=None):

    if access_token is None and user_id is None:
        raise
    if fields is not None:
        raise NotImplementedError('Batching for requests with fields not None'
                                  'is not supported yet.')
    params_dict = _core.params_dict_from_locals(locals())
    result = _core.vdr('friends.get', params_dict)

    return result

def _get_batch_of_friends(access_token=None, user_id=None, order=None, count=None,
                          offset=None, fields=None, name_case=None):
    # TODO implement batching for friends.get with fields parameter
    raise NotImplementedError

