# FastApi - Stakewolle test work

Описание:
Необходимо разработать простой RESTful API сервис для реферальной системы.

Функциональные требования:
регистрация и аутентификация пользователя (JWT, Oauth 2.0);
аутентифицированный пользователь должен иметь возможность создать или удалить свой реферальный код. Одновременно может быть активен только 1 код. При создании кода обязательно должен быть задан его срок годности;
возможность получения реферального кода по email адресу реферера;
возможность регистрации по реферальному коду в качестве реферала;	
получение информации о рефералах по id реферера;
UI документация (Swagger/ReDoc).

Опциональные задачи:
использование clearbit.com/platform/enrichment для получения дополнительной информации о пользователе при регистрации;
использование emailhunter.co для проверки указанного email адреса;
кеширование реферальных кодов с использованием in-memory БД. 
Readme.md файл с описанием проекта и инструкциями по запуску и тестированию

Стек:
использование любого современного веб фреймворка;
использование СУБД и миграций (Sqlite, PostgreSQL, MySQL);
размещение проекта на GitHub;

Требования к проекту:
чистота и читаемость кода;
все I/O bound операции должны быть асинхронными;
проект должен быть хорошо структурирован.
проект должен быть простым в деплое, обеспечивать обработку нестандартных ситуаций, быть устойчивой к неправильным действиям пользователя и т.д.

# Sources
- [Design](https://pixso.net/app/editor/-MdRp36PScUQrriU4yWAew?showQuickFrame=true&icon_type=1&page-id=0%3A1)
- [Logic circuit](https://miro.com/app/board/uXjVNvKL4oA=/)

# Running

Подготовка рабочей среды

    $ python3 -m venv venv
    $ source venv/bin/activate
    $ pip3 install -r requirements.txt

Выполнение миграций
Нет необходимости настраивать Alembic. Все подготовлено для миграций.
Сразу инициализируем первую миграцию и выполняем её.

    $ alembic revision --autogenerate -m "first migration"
    $ alembic upgrade head

Запускаем приложение локально:

    $ cd aothapp
    $ uvicorn main:app --reload

# .env
    
    TOKEN_LIFE_TIME=900 # 900sec=15min

    # Redis variables
    REDIS_SERVER=localhost
    REDIS_PORT=6379
    REDIS_DB=0
    REDIS_PASSWORD= # password

    # PostgreSQL
    POSTGRES_DRV=postgresql+asyncpg
    POSTGRES_DRV_FOR_MIGRATIONS=postgresql
    POSTGRES_USER=  # username
    POSTGRES_PASSWORD=  # password
    POSTGRES_SERVER=localhost
    POSTGRES_DB=    # db name
    POSTGRES_PORT=5432
