import math

from . import core


def get(access_token=None, user_ids=None, fields=None, name_case=None):

    """user_ids has to be a list of ids"""
    user_ids = ','.join(str(uid) for uid in user_ids)
    fields = ','.join(fields)

    # the API method only accepts at most 1000 user ids,
    # so if there is more, we organize them in batches

    batch_size = 1000
    n_ids = len(user_ids)

    result = []
    if n_ids > batch_size:
        n_batches = int(math.ceil(n_ids/float(batch_size)))
        print(n_batches, 'batches.')
        for i in range(n_batches):
            batch = user_ids[i: (i+1) * batch_size]
            result += _get_batch(access_token=access_token, user_ids=batch,
                                 fields=fields, name_case=name_case)
            print('Batch', i+1, 'out of', n_batches, 'received.')
    else:
        return _get_batch(access_token=access_token, user_ids=user_ids,
                          fields=fields, name_case=name_case)

    return result


def _get_batch(access_token=None, user_ids=None, fields=None, name_case=None):
    params_dict = {}
    if access_token:
        params_dict['access_token'] = access_token
    if user_ids:
        params_dict['user_ids'] = user_ids
    if fields:
        params_dict['fields'] = fields
    if name_case:
        params_dict['name_case'] = name_case

    result = core.vdr('users.get', params_dict=params_dict)

    return result
