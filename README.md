## ✨ Avito Analytics Academy | Python 🐍 | Final Project

---

В финальном проекте разработано CLI-приложение для заказа питсы 🍕. CLI-интерфейс используется с помощью использования click.

---

## Запуск
1. Склонируйте ветку с проектом в локальное расположение:

```git clone --branch final-task_working_branch https://github.com/freezeisperfect/pizza_project.git```

2. Перейдите в директорию `pizza_project`:

```cd pizza_project```

3. Запустите из директории `pizza_project` скрипт `main.py`. Возможные варианты использования:

* ```python main.py menu``` - вывести меню пиццерии

* ```python main.py order <pizza_name> [--delivery] [--size]``` - заказ пиццы.
   - Флаг `--delivery` выставляет доставку курьером, его отсутствие означает то, что клиент заберет пиццу с помощью самовывоза.
   - С помощью флага `--size` можно задать размер желаемой пиццы, если он доступен в пиццерии (например, `python main.py order pepproni --size XL` - заказ XL пиццы Pepperoni).
   - Доступные пиццы (можно увидеть с помощью `menu`): Margherita, Pepperoni, Hawaiian
   - Доступные размеры пицц: L, XL
---

## Тесты
Тесты написаны средствами `unittest`. Тесты запускаются с помощью `pytest` (т. к. `pytest` поддерживает запуск тест-кейсов, написанных для `unitcase`). Для запуска тестов из директории `pizza_project` запустите:

* ```python -m pytest -v```

Опционально можно сформировать отчет о покрытии тестами (отчет будет доступен в `htmlcov/index.html`):

* ```python -m pytest --cov . --cov-report html```