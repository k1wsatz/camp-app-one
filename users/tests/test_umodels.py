def test_create_user(user, django_user_model):
    """
    Test creating user
    """
    users = django_user_model.objects.all()
    assert len(users) == 2


def test_change_password(user):
    """
    Test changing password
    """
    user.set_password('secret')
    assert user.check_password('secret') is True

