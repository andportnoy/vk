from . import core


def get(token=None, user_id=None, order=None,
        count=None, offset=None, fields=None, name_case=None):

    params_dict = {}
    if token:
        params_dict['access_token'] = token
    if user_id:
        params_dict['user_id'] = user_id
    if order:
        params_dict['order'] = order
    if count:
        params_dict['count'] = count
    if offset:
        params_dict['offset'] = offset
    if fields:
        params_dict['fields'] = fields
    if name_case:
        params_dict['name_case'] = name_case

    result = core.vdr('friends.get', params_dict)

    return result