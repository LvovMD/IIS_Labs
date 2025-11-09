# Описание проекта
Проект посвящен решению задачи классификации мобильных устройств по стоимости
на основании датасета https://www.kaggle.com/datasets/iabhishekofficial/mobile-price-classification/data

# Запуск
Для запуска проекта необходимо выполнить команды:
```
git clone https://github.com/LvovMD/IIS_Labs.git
cd lab_project
python -m venv .lab_venv
source ./.lab_venv/bin/activate
pip install -r requirements.txt

```
# Исследование данных

Находится в `./eda/eda.ipynb`. Основные результаты:

В ходе исследования были проведены действия:
* Удалены записи с нулевым или отрицательным размером экрана
* Основные столбцы датасета проверены на валидность - данные не противоречивы
* Для столбцов 'battery_power', 'mobile_wt', 'px_height', 'px_width', 'ram', 'fc', 'int_memory', 'n_cores', 'pc', 'sc_h', 'sc_w', 'talk_time' изменен тип данных на int16
* Для столбцов 'clock_speed', 'm_dep' изменен тип данных на float16
* Для столбцов 'blue', 'dual_sim', 'four_g', 'three_g', 'touch_screen', 'wifi', 'price_range' установлен категориальный тип данных
* Был сформирован новый признак - `high_speed_ethernet` - доступ устройства к высокоскоростным стандартам Интернет-соединения.
* Был сформирован новый признак - `screen_size` - совокупный размер экрана устройства (в см).

В ходе анализа были выявлены следующие закономерности: 
* Размер батареи информативен для определения категории стоимости (см график `./eda/graph2.png`)
* Большинство особых функций связи мало информативны для классификации (см графики `./eda/graph3-5.png`)
* Числовые признаки мало зависимы друг от друга, что не позволяет снизить их размерность (кроме размеров экрана и модуля камеры).(см график `./eda/graph1.png`)

Обработанная выборка сохранена в файл `./data/clean_data.pkl`

# Настройка и обучение модели
На настройки модели используется MLFlow

Для запуска выполнить скрипт (находится в папке ./mlflow)
```
sh start_mlflow.sh

```
Исследования находятся в файле `./research/research.ipynb`

Лучшая модель получена в с помогщью CatboostClassifier, RFE и Optuna Search
`run_id = 08cfd1ee98cf442d91df8687db1aaea8` 
Она показывает следующие результаты
precision: 0.9210790773157267,
recall: 0.9216198957578268,
f1_score: 0.9212442875986313,
roc_auc: 0.9954045175474214
В ней выбраны следующие столбцы:
'ram', 'ram', 'ram*sc_h', 'px_width*ram', 'px_height*ram', 'sqrt(n_cores)*ram', 'battery_power*ram', 'ram*log(int_memory)', 'battery_power*px_width', 'battery_power*px_height', 'ram*log(talk_time)', 'sqrt(clock_speed)*ram'
С помощью Optuna Search выделены следующие гиперпараметры (за 20 прогонов):
'depth': 5, 'n_estimators': 150, 'learning_rate': 0.08491529648591742