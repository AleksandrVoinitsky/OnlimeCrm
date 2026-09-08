# Развёртывание на Amvera

## Назначение

Этот runbook определяет безопасный порядок тестового развёртывания Onlime CRM на
Amvera. Текущий профиль состоит из одного Django-контейнера и SQLite в persistent
storage. Он не предназначен для конкурентных операций CRM; условия перехода на
PostgreSQL, Redis и Celery зафиксированы в архитектурной документации.

## Контракт поставки

В корне репозитория должны находиться:

```text
Dockerfile                 # воспроизводимый образ приложения
amvera.yml                 # порт и точка монтирования persistent storage
.env.example               # только имена и безопасные примеры переменных
```

Amvera не поддерживает `docker-compose.yml` для production-развёртывания. Файл
`compose.yml` сохраняется только как контракт локального запуска и CI.

Реальные секреты не добавляются в Git. Они задаются в панели Amvera.

## Persistent storage

`amvera.yml` подключает постоянное хранилище по пути `/data`. Для production
обязательны следующие значения:

```text
DATABASE_PATH=/data/db.sqlite3
MEDIA_ROOT=/data/media
STATIC_ROOT=/app/staticfiles
```

До обновления приложения создавайте резервную копию SQLite-файла и проверяйте её
восстановление. Один SQLite-файл допускает только один экземпляр `web`.

## Переменные окружения production

Задайте в панели Amvera:

```text
DJANGO_ENV=production
DEBUG=False
SECRET_KEY=<случайное значение длиной не менее 50 символов>
ALLOWED_HOSTS=<домен приложения>
CSRF_TRUSTED_ORIGINS=https://<домен приложения>
DATABASE_PATH=/data/db.sqlite3
MEDIA_ROOT=/data/media
STATIC_ROOT=/app/staticfiles
SECURE_SSL_REDIRECT=True
SESSION_COOKIE_SECURE=True
CSRF_COOKIE_SECURE=True
SECURE_HSTS_SECONDS=31536000
```

Не включайте HSTS до подтверждения, что домен и все используемые поддомены всегда
доступны по HTTPS.

## Первая выкладка

1. Подключить ветку `main` GitHub-репозитория к приложению Amvera.
2. Убедиться, что в корне репозитория находятся `Dockerfile` и `amvera.yml`.
3. Задать production-переменные в панели Amvera.
4. Дождаться успешной сборки образа. Статика собирается в Docker build командой
   `python manage.py collectstatic --noinput`.
5. Через консоль Amvera выполнить `python manage.py migrate`.
6. Через консоль Amvera выполнить `python manage.py createsuperuser`; пароль не
   передавать через Git или переменные среды приложения.
7. Проверить `/health/`, главную страницу и вход в `/admin/`.
8. Настроить резервное копирование `/data/db.sqlite3`.

## Обновление

1. Проверить CI и совместимость миграций с текущей версией.
2. Создать резервную копию `/data/db.sqlite3`.
3. Отправить проверенный коммит в подключённую ветку.
4. После успешной сборки применить миграции через консоль Amvera как отдельный
   контролируемый этап.
5. Проверить `/health/`, журналы и критический пользовательский сценарий.

Не откатывайте миграции автоматически: откат приложения допустим только к версии,
совместимой с уже применённой схемой данных.
