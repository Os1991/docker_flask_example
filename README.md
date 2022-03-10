# docker_flask_example
Итоговый проект курса "Машинное обучение в бизнесе"

Стек:

ML: sklearn, pandas, numpy API: flask 
Данные собраны самостоятельный с сайта transfermarkt.com <br>
Задача: предсказать по описанию игрока его стоимость

Используемые признаки:<br>
age (int)<br>
position (category)<br>
citizenship (category)<br>
club (category)<br>
national_team (category)<br>

Модель: catboost<br>

Клонируем репозиторий и создаем образ<br>
$ git clone https://github.com/Os1991/docker_flask_example/.git <br>
$ cd docker_flask_example <br>
$ docker build -t Os1991/docker_flask_example <br>

Запускаем контейнер<br>
Здесь Вам нужно создать каталог локально и сохранить туда предобученную модель (<your_local_path_to_pretrained_models> нужно заменить на полный путь к этому каталогу)<br>

$ docker run -d -p 8180:8180 -p 8181:8181 -v <your_local_path_to_pretrained_models>:/app/app/models Os1991/docker_flask_example <br>

Переходим на localhost:8181
