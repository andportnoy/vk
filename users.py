from . import _core


def get(access_token=None, user_ids=None, fields=None, name_case=None):
    """user_ids and fields have to be lists."""

    # check type, joining is done later batch by batch
    if user_ids is not None:
        if not isinstance(user_ids, list):
            raise TypeError('user_ids must be a list.')

    # check type and join
    if fields is not None:
        if isinstance(fields, list):
            fields = ','.join(fields)
        else:
            raise TypeError('fields must be a list.')

    # check type
    if name_case is not None:
        if not isinstance(name_case, str):
            raise TypeError('name_case must be a string.')

    # create params dictionary from passed arguments,
    # but put user_ids in a separate dict
    params_dict = _core.params_dict_from_locals(locals())
    user_ids = {'user_ids': params_dict.pop('user_ids')}

    # the API method only accepts at most 1000 user ids,
    # but in reality it can't handle more than 900 long ids,
    # possibly because of commas overhead
    # for explanation of the choice of batch_size, see relevant notebook
    batch_size = 900
    result = _core.request_in_batches(_get_batch_of_users,
                                      user_ids,
                                      batch_size,
                                      params_dict)

    return result


def _get_batch_of_users(access_token=None, user_ids=None,
                        fields=None, name_case=None):

    user_ids = ','.join(str(uid) for uid in user_ids)

    params_dict = _core.params_dict_from_locals(locals())
    result = _core.vdr('users.get', params_dict=params_dict)

    return result
