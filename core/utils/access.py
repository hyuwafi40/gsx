from django.contrib.auth.models import User


def get_user_role(user):
    if not user.is_authenticated:
        return None
    if user.is_superuser:
        return "developer"
    if user.is_staff:
        return "administrator"
    if user.is_active:
        return "reguler"
    return "nonactive"


def apply_role_to_user(user, role):
    if role == "developer":
        user.is_superuser = True
        user.is_staff = True
        user.is_active = True
    elif role == "administrator":
        user.is_superuser = False
        user.is_staff = True
        user.is_active = True
    elif role == "reguler":
        user.is_superuser = False
        user.is_staff = False
        user.is_active = True
    elif role == "nonactive":
        user.is_superuser = False
        user.is_staff = False
        user.is_active = False
