# Bank System

О чем проект?
--
Данный проект представляет из себя оконное банковское приложение, где вы, создав аккаунт в базе данных, можете совершать банковские операции, такие как:
1. снятие денег со счета
2. пополнение баланса
3. перевод денег на другой аккаунт
Также вы можете отслеживать историю своих операций.

Как запустить проект?
--
Необходимо склонировать репозиторий с помощью комманды "git clone git@github.com:yourEmotion/Bank-System.git", затем запустить из папки файл main.py, например, с помощью терминала: "python3 Bank-System/src/main.py"

Интерфейс
--
Для удобства пользования были созданы ночную и дневную темы, чтобы вам было максимально комфортно при работе с приложением. Вы всегда можете сменить режим в правом верхнем углу окна.
При запуске вам будет предложено создать новый аккаунт или воспользоваться уже существующим. При входе вам предстоит пройти аутентификацию, а именно ввести свой логин и пароль. При регистрации вам необходимо придумать логин, ввести дату рождения и придумать пароль. Помните: чем надежнее пароль, тем в большей безопасности находятся ваши средства!
Далее вы попадете на главное окно аккаунта, где вам будет предложено снять деньги, отправить их другому пользователю или пополнить баланс извне. Вы всегда можете проверить историю своих банковских операций, перейдя в специальное окно в меню.

Реализация
--
При создании приложения использовались библиотеки PyQt5 и SQLite3, а также некоторые встроенные, по типу collections и string. PyQt5 используется для интерфейса приложения: создание окон и взаимодействие между ними. SQLite3 используется для хранения пользователей и всех операций, проводимых ими.


Возможности для развития
--
На мой взгляд, данный проект может иметь даже широкое прикладное применение ввиду своего удобного интерфейса и довольно полезного функционала. Поэтому было бы хорошо поместить базу данных на сервер, чтобы пользоваться ей могли люди с разных адресов. И понятно, что было бы неплохо, если бы внос денег на счет проводился бы не из ниоткуда, и вдовесок к этому нужна повышенная безопасность доступа к данным.
