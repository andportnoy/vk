from . import core

def get(access_token=None, owner_id=None, domain=None, offset=None, count=None,
        filter=None, extended=None, fields=None):

    params_dict = {}
    if access_token:
        params_dict['access_token'] = access_token
    if owner_id:
        params_dict['owner_id'] = owner_id
    if domain:
        params_dict['domain'] = domain
    if offset:
        params_dict['offset'] = offset
    if count:
        params_dict['count'] = count
    if filter:
        params_dict['filter'] = filter
    if extended:
        params_dict['extended'] = extended
    if fields:
        params_dict['fields'] =  fields

    result = core.vdr('wall.get', params_dict)

    return result


def getById(posts=None, extended=None, copy_history_depth=None, fields=None):

    """posts is a comma-joined string of post ids."""
    params_dict = {}

    if posts:
        params_dict['posts'] = posts
    if extended:
        params_dict['extended'] = extended
    if copy_history_depth:
        params_dict['copy_history_depth'] = copy_history_depth
    if fields:
        params_dict['fields'] = fields

    result = core.vdr('wall.getById', params_dict)

    return result