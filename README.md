# Sprint_6

Автотесты для учебного сервиса **«Яндекс.Самокат»** (Selenium + Pytest + Page Object Model + Allure).

## Структура проекта

```
Sprint_6/
├── tests/
│   ├── test_main_page.py     # тесты вопросов о важном (параметризация)
│   ├── test_order_flow.py    # позитивный флоу заказа (две точки входа, два набора данных)
│   └── test_logo.py          # проверка переходов по логотипам Самоката и Яндекса
├── page_objects/             # пакет Page Object
│   ├── __init__.py
│   ├── base_page.py          # базовый класс Page Object
│   ├── main_page.py          # страница главная
│   └── order_page.py         # страница заказа
├── conftest.py               # фикстура driver (Firefox)
├── requirements.txt
├── allure-report/            # сгенерированный Allure-отчёт
└── allure_results/           # сырые результаты (не коммитятся)
```

## Установка

```bash
pip install -r requirements.txt
```

Нужны браузер Mozilla Firefox и geckodriver, а также Java и Allure Commandline (для отчёта).

## Запуск тестов

```bash
python -m pytest tests/
```

## Allure-отчёт

```bash
# записать результаты
python -m pytest tests/ --alluredir=allure_results

# собрать отчёт
allure generate allure_results -o allure-report --clean

# открыть отчёт
allure open allure-report
```