# mafia_bot_public
Это телеграмм бот популярной игры мафия. Для работы бота нужно заменить два поля: id чата в котором будете играть и токен бота.
В боте реализованы все базовые функции:
1)Регистрация участников
2)Автоматическое рандомное распределение ролей
3)Автоматическая смена дня и ночи по таймеру с параллельным приемом данных от участников
4)Автоматическое завершение игры при недостаточном колличестве игроков
5)Защита от запуска бота в нецелевых чатах
6)Защита от окончания игры из личного чата с ботом
7)Защита от множественного запуска игры
8)Вывод текущих живых игроков и ролей
9)Вывод сообщения о завершении игры при победе одной из команд
Планируется реализовать во второй версии:
1)Связать бота с БД
2)Создать отдельный чат для мафий
3)Создать рейтинг игроков
4)Сделать бота многопоточным для игры из множества чатов одновременно
