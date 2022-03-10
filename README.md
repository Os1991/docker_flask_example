# docker_flask_example
Итоговый проект курса "Машинное обучение в бизнесе"

Стек:

ML: sklearn, pandas, numpy API: flask 
Данные собраны самостоятельный с сайта transfermarkt.com

Задача: предсказать по описанию игрока его стоимость


Используемые признаки:

age (int)
position (category)
citizenship (category)
club (category)
national_team (category)



Модель: catboost

Клонируем репозиторий и создаем образ
$ git clone https://github.com/Os1991/docker_flask_example/.git
$ cd docker_flask_example
$ docker build -t Os1991/docker_flask_example
Запускаем контейнер
Здесь Вам нужно создать каталог локально и сохранить туда предобученную модель (<your_local_path_to_pretrained_models> нужно заменить на полный путь к этому каталогу)

$ docker run -d -p 8180:8180 -p 8181:8181 -v <your_local_path_to_pretrained_models>:/app/app/models Os1991/docker_flask_example
Переходим на localhost:8181
