## Macro reports (CLI)

Скрипт читает один или несколько CSV с макроэкономическими данными и строит отчёты в консоль.
Сейчас реализован отчёт `average-gdp`: средний ВВП по странам по всем переданным файлам.

### Установка
```bash
pip install -r requirements.txt
```

### Запуск
```bash
python3 main.py --files economic1.csv economic2.csv --report average-gdp
```

### Тесты
```bash
pip install -e ".[dev]"
pytest --cov=reports
```

### Как добавить новый отчёт
1) Создать модуль в `reports/` с классом, у которого есть поля `name` и метод `build(rows)`.
2) Зарегистрировать его в `reports/__init__.py` в `_REGISTRY`.


### Screenshots
- `docs/run_average_gdp.png` — example report run
- `docs/tests_passed.png` — pytest run
