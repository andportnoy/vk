from tqdm import tqdm
import math
from . import _core


def get(access_token=None, owner_id=None, domain=None,
        filter=None, extended=None, fields=None):

    params_dict = _core.params_dict_from_locals(locals())
    total = get_count(access_token=access_token, owner_id=owner_id, domain=domain, filter=filter)

    batch_size = 100
    n_batches = math.ceil(total / batch_size)

    posts = []
    for i in tqdm(range(n_batches)):
        offset = batch_size * i
        posts += _get_batch_of_posts(**params_dict, offset=offset)['items']

    return posts


def _get_batch_of_posts(access_token=None, owner_id=None, domain=None, offset=None,
                        count=100, filter=None, extended=None, fields=None):

    if access_token is None and owner_id is None and domain is None:
        raise TypeError('either access_token, owner_id'
                        'or domain must be not None.')

    params_dict = _core.params_dict_from_locals(locals())
    result = _core.vdr('wall.get', params_dict=params_dict)

    return result


def get_count(access_token=None, owner_id=None, domain=None, filter=None):
    params_dict = _core.params_dict_from_locals(locals())
    return _get_batch_of_posts(**params_dict, count=1)['count']


def getById(posts=None, extended=None, copy_history_depth=None, fields=None):

    """posts is a comma-joined string of post ids."""
    params_dict = _core.params_dict_from_locals(locals())
    result = _core.vdr('wall.getById', params_dict)

    return result
