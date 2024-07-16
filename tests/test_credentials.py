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
        'database_url_lite',
        'secret',
        'POSTGRESS_DB_NAME',
        'POSTGRESS_HOST',
        'POSTGRESS_PORT',
        'POSTGRES_USER',
        'POSTRGRES_PASSWORD',
        'REDIS_HOST',
        'REDIS_PORT',
    ]
    for cred in need_cred:
        assert hasattr(settings, cred), (
            f'В объекте `app.core.config.Settings` нет атрибута `{cred}`'
        )
