from . import core


def get(user_ids=None, fields=None, name_case=None):
    """user_ids and fields have to be lists."""

    if not isinstance(user_ids, list):
        raise TypeError('user_ids must be a list.')

    if fields is not None:
        fields = ','.join(fields)

    params = core.params_dict_from_locals(locals())
    user_ids = {'user_ids': params.pop('user_ids')}
    
    # the API method only accepts at most 1000 user ids,
    # but in reality it can't handle more than 900 long ids,
    # possibly because of commas overhead
    # for explanation of the choice of batch_size, see relevant notebook
    batch_size = 900
    result = core.execute_in_batches(_get_batch_of_users,
                                     user_ids,
                                     batch_size,
                                     params)

    return result


def _get_batch_of_users(user_ids=None, fields=None, name_case=None):

    user_ids = ','.join(str(uid) for uid in user_ids)

    params_dict = core.params_dict_from_locals(locals())
    result = core.vdr('users.get', params_dict=params_dict)

    return result
