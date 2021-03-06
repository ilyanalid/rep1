Принцип *Interface seggregation* декларирует, что клиенты не должны зависеть от методов, которые они **не используют**. То есть если какой-то метод интерфейса не используется клиентом, то изменения этого метода не должны приводить к необходимости внесения изменений в клиентский код.

Следование принципу ISP заключается в создании интерфейсов, которые достаточно специфичны и требуют только необходимый минимум реализаций методов. Избыточные интерфейсы, напротив, могут требовать от реализующего класса создание большого количества методов, причём даже таких, которые не имеют смысла в контексте класса.

- Пример из жизни:

*Расписание на весь университет*. Если не разделить его по группам, а запихнуть все в один файл, то студенты запутаются. Не нужная им информация о занятиях других групп им не нужны, но они будут на них ходить, исходя из расписания.
