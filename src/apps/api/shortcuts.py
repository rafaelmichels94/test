from apps.api.permissions import UserRoleEnum
from apps.domain import models
from commons import jwt


def generate_user_token(instance, exp=None):
    """
    Generate the correct token for a user instance.

    WARNING: This method was created just to development and test purpose,
        never call this in a production environment.
    """
    role = None
    if isinstance(instance, models.User):
        if models.User.objects.check_role(instance, "agent"):
            role = UserRoleEnum.AGENT.value
        elif models.User.objects.check_role(instance, "supervisor"):
            role = UserRoleEnum.SUPERVISOR.value
        elif instance.is_superuser:
            role = UserRoleEnum.ADMIN.value

    if role is None:
        raise TypeError(
            "Instance must be 'domain.models.User' type and with a role."
        )

    return jwt.Jwt.generate(key=jwt.JWT_KEY, exp=exp, id=str(instance.pk), role=role)
