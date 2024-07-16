try:
    from app.core.config import Settings # noqa
except (NameError, ImportError):
    raise AssertionError(
        'Не обнаружен объект настроек приложения `Settings`.'
        'Проверьте и поправьте: он должен быть доступен в модуле '
        '`app.core.config`.',
    )
