from enum import Enum

from rest_framework.permissions import BasePermission


from enum import Enum

from rest_framework.permissions import BasePermission


class UserRoleEnum(Enum):
    AGENT = 0
    SUPERVISOR = 1
    ADMIN = 2

    @classmethod
    def is_agent(cls, user):
        return user.role == cls.AGENT.value

    @classmethod
    def is_supervisor(cls, user):
        return user.role == cls.SUPERVISOR.value

    @classmethod
    def is_admin(cls, user):
        return user.role == cls.ADMIN.value


class BaseRolePermission(BasePermission):
    http_allowed_verbs = ["HEAD", "OPTIONS"]

    def is_allowed_verb(self, request):
        """
        Check whether the http verb is allowed.
        """
        return request.method in self.http_allowed_verbs

    def is_authenticated(self, request):  # noqa
        """
        Check whether the panel_user is authenticated.
        """
        return request.user and request.user.is_authenticated

    def has_role_permission(self, request):
        """
        Check whether panel_user has the role permission.
        """
        raise NotImplementedError()

    def has_permission(self, request, view):
        """
        Check whether the panel_user is allowed to perform
        actions in the given request.
        """
        if self.is_allowed_verb(request):
            return True

        return self.is_authenticated(request) and self.has_role_permission(request)


class IsAgent(BaseRolePermission):
    """
    The request is authenticated as a agent, or cors http verbs.
    """

    def has_role_permission(self, request):
        return UserRoleEnum.is_agent(request.user)


class IsSupervisor(BaseRolePermission):
    """
    The request is authenticated as a supervisor, or cors http verbs.
    """

    def has_role_permission(self, request):
        return UserRoleEnum.is_supervisor(request.user)


class IsAdmin(BaseRolePermission):
    """
    The request is authenticated as a admin, or cors http verbs.
    """

    def has_role_permission(self, request):
        return UserRoleEnum.is_admin(request.user)


class IsAgentOrSupervisor(BaseRolePermission):
    """
    The request is authenticated as a agent or supervisor, or cors http verbs.
    """

    def has_role_permission(self, request):
        return UserRoleEnum.is_agent(request.user) or UserRoleEnum.is_supervisor(request.user)
