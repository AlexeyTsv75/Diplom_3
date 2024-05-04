**Проект Sprint_5**
В данном проекте созданы автотесты для сервиса Stellar Burgers. Это космический фастфуд: можно собрать и заказать бургер из необычных ингредиентов.

**Тесты проверяют:**
- Регистрация (_test_registration.py_)
Проверяется:
Успешная регистрация
Ошибку для некорректного пароля.
- Вход (_test_login.py_)
Проверяется:
вход по кнопке «Войти в аккаунт» на главной,
вход через кнопку «Личный кабинет»,
вход через кнопку в форме регистрации,
вход через кнопку в форме восстановления пароля.
- Переход в личный кабинет (_test_enter_profile.py_)
Проверяется переход по клику на «Личный кабинет».
- Переход из личного кабинета в конструктор (_test_move_from_profile.py_)
Проверяется переход по клику на «Конструктор» и на логотип Stellar Burgers.
- Выход из аккаунта (_test_exit_profile.py_)
Проверяется выход по кнопке «Выйти» в личном кабинете.
- Раздел «Конструктор» (_test_constructor_change_tabs.py_)
Проверяется, что работают переходы к разделам:
«Булки»,
«Соусы»,
«Начинки».

**Структура проекта:**
- configuration.py - файл с сылками на тестируемые страницы сайта
- conftest.py - используемые фикстуры
- data.py - тестовые данные
- locators.py - используемые в проекте локаторы
- tests - папка с тестами, распределенными в соответствии с тестируемой функциональностью

**Необходимо установить**
- фреймворк pytest
- драйвер для браузера WebDriver
- фреймворк Selenium

**Запуск тестов**

- запуск всех тестов:
  pytest -v tests/
- запуск выбранного теста
  pytest -v tests/"имя_выбранного_теста"
 