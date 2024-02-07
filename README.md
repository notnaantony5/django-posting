1. Создать новый django проект
2. Установить зависимости
   1. djangorestframework
   2. djangorestframework-simplejwt
   3. envparse
   4. Создать requirements.txt
3. Отредактировать настройки
   1. Создание пути к `.env`
   2. Вынести Debug и SECRET_KEY
   3. Добавление приложений в INSTALLED_APPS
   4. Настройка Simple JWT (REST_FRAMEWORK)
   5. Прописать пути для токенов
4. Создать мини-приложение profiles
   1. В нем создать новую модель User от AbstractUser
   2. Создать модель анкета (поля на ваше усмотрение) со связью один ко многим к пользователю (ForeignKey)
   3. Написать сериализатор для регистрации пользователя 
   4. Написать сериализаторы для создания и удаления анкет
   5. Определить views для всех сериализаторов (анкеты может создавать только авторизованный пользователь, пользователь к анкете привязывается автоматически)
   6. Добавить и подключить мини приложения и urls
5. Создать .gitignore, заполнить, оформить README.md, создать репозиторий на гитхаб с этим проектом
6. (Дополнительно) Сделать так, чтобы анкету мог удалять только ее создатель (permission_classes)