try:
    from app.core.config import settings
except (NameError, ImportError):
    raise AssertionError(
        'Не обнаружен инициализированный объект `settings`.'
        'Проверьте и поправьте: он должен быть доступен в модуле '
        '`app.core.config`',
    )


def test_google_cred():
    need_cred = [
        'app_title',
        'description',
        'database_url',
        'secret',
        'postgres_user',
        'postgres_password',
        'postgres_host',
        'postgres_port',
        'postgres_name',
    ]
    for cred in need_cred:
        assert hasattr(settings, cred), (
            f'В объекте `app.core.config.Settings` нет атрибута `{cred}`'
        )
