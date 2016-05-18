from . import core, users, friends

"""I want this class to automatically read or request a token and then
call functions from other modules passing the token as an argument.
I don't know how to achieve that yet.
"""

class TokenSession:

    def __init__(self, token=None, app_id=5080984):
        if token:
            self.token = token
        else:
            try:
                with open('token.txt') as t:
                    self.token = t.read()
            except IOError:
                print('Token file not found, getting token from vk.')
                self.token = core.get_token(app_id)


    def users_get(self, user_ids=None, fields=None, name_case=None):
        return users.get(token=self.token, user_ids=user_ids,
                         fields=fields, name_case=name_case)

    def friends_get(self, user_id=19002881, order=None, count=None,
                    offset=None, fields=None, name_case=None):

        return friends.get(token=self.token, user_id=user_id,
                           order=order, count=count, offset=offset,
                           fields=fields, name_case=name_case)
