# Работа с базой данных
# Альбина Ерещенко, 47 когорта
Задание 1
Представь: тебе нужно проверить, отображается ли созданный заказ в базе данных.
Для этого: выведи список логинов курьеров с количеством их заказов в статусе «В доставке» (поле inDelivery = true).
# Итак, подключаемся к серверу:
Альбина@AlyaBook ~
$ cat ~/.ssh/id_ed25519.pub
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIKF80JpOAWr6nUilmqFa+JiV0gTCmyohDfdk6BN9+0KW Альбина@AlyaBook

# Подключаемся к бд c верным паролем!:
Альбина@AlyaBook ~
morty@server-c5deb0a2-cf49-4e97-aa0c-4797fceb7ad4:~$ psql -U morty -d scooter_rent
Password for user morty:
psql: FATAL:  password authentication failed for user "morty"
morty@server-c5deb0a2-cf49-4e97-aa0c-4797fceb7ad4:~$ psql -U morty -d scooter_rent
Password for user morty:
psql (11.18 (Debian 11.18-0+deb10u1))
Type "help" for help.
# Сам запрос(курьер авторизован, но заказ не взял):
scooter_rent=# SELECT "Couriers".login, COUNT("Orders".id) AS delivery_count
 FROM "Orders"
 JOIN "Couriers" ON "Orders"."courierId" = "Couriers".id
 WHERE "Orders"."inDelivery" = true
 GROUP BY "Couriers".login;
 login | delivery_count
-------+----------------
(0 rows)
# Авторизованный курьер принял заказ, повторяем запрос:
scooter_rent=# SELECT "Couriers".login, COUNT("Orders".id) AS delivery_count
 FROM "Orders"
 JOIN "Couriers" ON "Orders"."courierId" = "Couriers".id
 WHERE "Orders"."inDelivery" = true
 GROUP BY "Couriers".login;
 login | delivery_count
-------+----------------
 first |              2
(1 row)

Задание 2
Ты тестируешь статусы заказов. Нужно убедиться, что в базе данных они записываются корректно.
Для этого: выведи все трекеры заказов и их статусы. 
Статусы определяются по следующему правилу:
Если поле finished == true, то вывести статус 2.
Если поле canсelled == true, то вывести статус -1.
Если поле inDelivery == true, то вывести статус 1.
Для остальных случаев вывести 0.
Технические примечания:
Доступ к базе осуществляется с помощью команды psql -U morty -d scooter_rent. Пароль: smith.
У psql есть особенность: если таблица в базе данных с большой буквы, то её в запросе нужно брать в кавычки. Например, select * from "Orders".
# от БД мы все еще не отключены, второй запрос и результат выполнения:
scooter_rent=# SELECT "Orders".track,
scooter_rent-# CASE
scooter_rent-# WHEN "Orders".finished = true THEN 2
scooter_rent-# WHEN "Orders".cancelled = true THEN -1
scooter_rent-# WHEN "Orders"."inDelivery" = true THEN 1
scooter_rent-# ELSE 0
scooter_rent-# END AS status
scooter_rent-# FROM "Orders";
 track  | status
--------+--------
 783421 |      1
 783421 |      1
(2 rows)

scooter_rent=#
# Запрос выполнен но для тестирования статусов результата недостаточно, добавляем заказы и повторяем запрос:
scooter_rent=# SELECT "Orders".track,
CASE
WHEN "Orders".finished = true THEN 2
WHEN "Orders".cancelled = true THEN -1
WHEN "Orders"."inDelivery" = true THEN 1
ELSE 0
END AS status
FROM "Orders";
 track  | status
--------+--------
 783421 |      1
 783421 |      1
 528580 |      1
 528580 |      2
 430920 |      0
(5 rows)

scooter_rent=#
