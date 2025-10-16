from selenium.webdriver.common.by import By

# === Базовый URL ===
BASE_URL = "https://stellarburgers.education-services.ru"

# === Поля на странице регистрации ===
NAME_INPUT         = (By.XPATH, "//label[text()='Имя']/following-sibling::input")       # Поле "Имя" на форме регистрации
EMAIL_INPUT        = (By.XPATH, "//label[text()='Email']/following-sibling::input")    # Поле "Email" на форме регистрации
PASSWORD_INPUT     = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")   # Поле "Пароль" на форме регистрации

# === Кнопки регистрации и логина ===
REGISTER_BUTTON    = (By.XPATH, "//button[text()='Зарегистрироваться']")              # Кнопка "Зарегистрироваться"
LOGIN_BUTTON       = (By.XPATH, "//button[text()='Войти']")                           # Кнопка "Войти" на форме регистрации/входа
REGISTER_FORM_LOGIN_LINK  = (By.XPATH, "//a[text()='Войти']")                         # Ссылка "Войти" внутри формы регистрации
RECOVERY_FORM_LOGIN_LINK  = (By.XPATH, "//a[text()='Войти']")                         # Ссылка "Войти" в форме восстановления пароля

# === Поля формы входа ===
LOGIN_EMAIL_INPUT     = (By.XPATH, "//label[text()='Email']/following-sibling::input")    # Поле "Email" в форме входа
LOGIN_PASSWORD_INPUT  = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")   # Поле "Пароль" в форме входа

# === Сообщения об ошибках ===
PASSWORD_ERROR_MSG    = (By.XPATH, "//p[contains(text(), 'Некорректный пароль')]")        # Сообщение "Некорректный пароль"

# === Навигация (меню, хедер) ===
MAIN_LOGIN_BTN        = (By.XPATH, "//button[text()='Войти в аккаунт']")                  # Кнопка "Войти в аккаунт" на главной
PROFILE_LINK          = (By.XPATH, "//a[@href='/account']")                               # Ссылка "Личный кабинет" в шапке сайта
CONSTRUCTOR_TAB       = (By.LINK_TEXT, "Конструктор")                                    # Вкладка "Конструктор" в шапке сайта
LOGO_LINK             = (By.XPATH, "//div[contains(@class,'AppHeader_header__logo')]/a[@href='/']")  # Логотип Stellar Burgers в шапке
LOGOUT_BUTTON         = (By.XPATH, "//button[normalize-space(text())='Выход']")           # Кнопка "Выход" в личном кабинете

# === Вкладки внутри конструктора ===
TAB_BUNS      = (By.XPATH, "//span[text()='Булки']")        # Вкладка "Булки"
TAB_SAUCES    = (By.XPATH, "//span[text()='Соусы']")        # Вкладка "Соусы"
TAB_FILLINGS  = (By.XPATH, "//span[text()='Начинки']")      # Вкладка "Начинки"

# === Заголовки разделов конструктора ===
HEADER_BUNS      = (By.XPATH, "//h2[text()='Булки']")       # Заголовок секции "Булки"
HEADER_SAUCES    = (By.XPATH, "//h2[text()='Соусы']")       # Заголовок секции "Соусы"
HEADER_FILLINGS  = (By.XPATH, "//h2[text()='Начинки']")     # Заголовок секции "Начинки"