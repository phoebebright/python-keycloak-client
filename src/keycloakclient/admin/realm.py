from keycloakclient.admin import KeycloakAdminBase

__all__ = ('Realm', 'Realms',)


class Realms(KeycloakAdminBase):

    def by_name(self, name):
        return Realm(name=name, client=self._client)


class Realm(KeycloakAdminBase):
    _name = None

    def __init__(self, name, *args, **kwargs):
        self._name = name
        super(Realm, self).__init__(*args, **kwargs)

    @property
    def clients(self):
        from keycloakclient.admin.clients import Clients
        return Clients(realm_name=self._name, client=self._client)

    @property
    def users(self):
        from keycloakclient.admin.users import Users
        return Users(realm_name=self._name, client=self._client)

    @property
    def groups(self):
        from keycloakclient.admin.groups import Groups
        return Groups(realm_name=self._name, client=self._client)
