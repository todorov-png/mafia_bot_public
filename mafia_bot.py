# -*- coding: utf8 -*-
import telebot
import random
import time
from telebot import types
TOKEN = '6347512142:AAHC9hofi1ZCKSv-m3TL54Xn1a2PsGx0W3Q' #bot token from
bot=telebot.TeleBot(TOKEN)
global UserMas
global Killmas
global chatId
global GROUP_ID
global suisad
GROUP_ID= 1835974339 # Ваш ID группы  мафии
mafia_don_list="Список мафии:\n"
mir_list="Список мирных жителей:\n"
mafWin=0
mirWin=0
donwork=0
MentKill=0
doctorwork=0
doctorworkBuf=0
suisad=0
kill=0
kill1=-1
chatId=0
startGameValue=0
bludwork="a" 
checkment="b"
UserMas=[]
Killmas=[]
Maf3_5=['дон','доктор','блудница']
Maf6_8=['дон','мафия','доктор','блудница','ментяра']
Maf9_10=['дон','мафия','мафия','доктор','блудница','ментяра','камикадзе']
Maf11_14=['дон','мафия','мафия','мафия','доктор','блудница','ментяра','лейтенант','камикадзе']
Maf15_18=['дон','мафия','мафия','мафия','мафия','доктор','блудница','ментяра','лейтенант','камикадзе']
Maf19_next=['дон','мафия','мафия','мафия','мафия','доктор','блудница','ментяра','лейтенант','лейтенант','камикадзе']

#Отправляем приветственное сообщение при команде старт
@bot.message_handler(commands=['start'])
def welcome(message):
   if startGameValue==0:
      #Отправляем стикер
      bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIQC15-Zuo8YhfYe0MnBlkdXqT63MM6AAJBAANSiZEj1dZXStNkcVYYBA')
      bot.send_message(message.chat.id, "Привет мафиозник, запусти меня и мы устроем месиво!")
      print("В чат вступил "+str(message.from_user.first_name))


@bot.message_handler(commands=['startgame'], func=lambda message: message.chat.id == GROUP_ID)
def StartGamess(message):
   global counter
   global UserMas
   global Killmas
   global mafia_don_list
   global mir_list
   global name
   global startGameValue
   global chatId
   global doctorworkBuf
   global suisad
   if startGameValue==0:
      doctorworkBuf=0
      suisad=0
      print(str(message.from_user.first_name)+" - запустил игру")
      chatId=0
      chatId=message.chat.id
      mafia_don_list="Список мафии:\n"
      mir_list="Список мирных жителей:\n"
      name='Список игроков:\n'
      counter=0
      UserMas.clear()
      Killmas.clear()
      #Отправляем стикер
      bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIQC15-Zuo8YhfYe0MnBlkdXqT63MM6AAJBAANSiZEj1dZXStNkcVYYBA')
      #Создаем кнопки под сообщением
      markup = types.InlineKeyboardMarkup(row_width=1)
      item1 = types.InlineKeyboardButton("Зарегистрироваться!", callback_data='registration')
      markup.add(item1)
      #Отправляе сообщение и прикрепляем клавиатуру
      bot.send_message(message.chat.id, "Ну что, кто готов играть?".format(message.from_user), reply_markup=markup)
   else:
      bot.send_message(message.chat.id, "Игра уже идет, не мешай!")


@bot.message_handler(commands=['testuser'])
def test_user(message):
   global startGameValue
   if startGameValue==0:
      print(str(message.from_user.first_name)+" - решил проверить себя")
      #Создаем кнопки под сообщением
      markupTestUser = types.InlineKeyboardMarkup(row_width=1)
      item1 = types.InlineKeyboardButton("Проверить себя", callback_data='TestUser')
      markupTestUser.add(item1)
      #Отправляе сообщение и прикрепляем клавиатуру
      bot.send_message(message.chat.id, "Нажмите на кнопку для проверки данных, если получите в 3 поле None, то задайте в профиле фамилию".format(message.from_user), reply_markup=markupTestUser)
   else:
      bot.send_message(message.chat.id, "Во время игры запрещено себя проверять")


@bot.message_handler(commands=['gameover'], func=lambda message: message.chat.id == GROUP_ID)
def Gemeover(message):
   print(str(message.from_user.first_name)+" - решил завершить игру")
   global startGameValue
   startGameValue=0
   bot.send_message(message.chat.id, "Игра завершена")


@bot.message_handler(commands=['help'])
def helps(message):
   print(str(message.from_user.first_name)+" - вызвал команду help")
   bot.send_message(message.chat.id, "Для того что бы играть, нужно нажать кнопку 'зарегистрироваться'\nПосле первого зарегистрировавшегося запускается таймер на 90 секунд!'\nДальше начинается раздача ролей.\nКаждому прийдет сообщение с его ролью.\nЕсли играют от 3 до 5 человек: мафия, доктор, блудница, остальные мир\nЕсли играют от 6 до 8 человек: две мафии, доктор, блудница, ментяра, остальные мир\nЕсли играют от 9 до 10 человек:три мафии, доктор, блудница, ментяра, камикадзе, остальные мир\nЕсли играют от 11 до 14 человек: четыре мафии, доктор, блудница, ментяра, лейтенант, камикадзе, остальные мир\nЕсли играют от 15 до 18 человек: пять мафии, доктор, блудница, ментяра, лейтенант, камикадзе, остальные мир\nПосле раздачи ролей начинается ночь и активные роли делают свои делишки, на это у них 1 минута.\nПосле ночи начинается день, и мирные жители собираются что бы кого то казнить, на поиск виновных у них 1 минута.\nЕсли мафию не смогли убить, то наступает ночь...\nИ так по кругу, пока кто то, не победит.\nРоли:\nДон - глава мафии, он решает кого убивать\nМафия - помощники дона, после смерти дона один из мафия становится доном\nМентяра - ищет или убивает злодеев\nЛейтенант - минимент, который становится ментярой после смерти начальника, \nДоктор - лечит подстреленных бойцов\nБлудница - устраивает массовые оргии с кучей свидетелей\nКамикадзе - хочет сдохнуть, но не хватает силы воли, побеждает, когда жители на дневном собрании повесят")


@bot.callback_query_handler(func=lambda call:True) #Функция ответа на нажатие кнопки, срабатывает разово при нажатии
def callback_inline(call):
   try:
      if call.message:
         if call.data == 'registration': #При нажатии кнопки записываем данные пользователя и увеличиваем счетчик
            global counter
            global name
            global mafia_don_list 
            global mir_list
            global checkment
            global mentid
            global bludwork
            global doctorwork
            global donwork
            global MentKill
            global mafWin
            global mirWin
            global kill
            global kill1
            global startGameValue
            global chatId
            global doctorworkBuf
            global Killmas
            global suisad
            warningUser=0
            if counter==0:#Если пользователь первый
               UserMasItem=[]
               suisad=0
               startGameValue=1 #Закрываем запуск игры
               if call.from_user.username==None:   #Если нет ника, то ставим имя
                  UserMasItem.append(str(call.from_user.first_name)+str(counter+1))
               else:
                  UserMasItem.append(call.from_user.username)    #Добавляем ник игрока
               UserMasItem.append(call.from_user.id)          #Добавляем id игрока
               if call.from_user.last_name==None:
                  UserMasItem.append(call.from_user.first_name)#Добавляем имя игрока, если фамилии нет
               else:
                  UserMasItem.append(call.from_user.last_name)#Добавляем фамилию игрока
               UserMasItem.append('мир')                      #Добавляем должность, по умолчанию мир
               UserMasItem.append('живой')                    #Добавляем статус, по умолчанию живой
               UserMasItem.append(0)                          #Добавляем голосов, по умолчанию 0
               UserMasItem.append(0)                          #Добавляем действие совершено, по умолчанию 0
               UserMas.append(UserMasItem)                    #Добавляем наш обьект пользователя в массив
               name+=str(UserMas[counter][2])+'\n'
               print(str(UserMas)+" - первый игрок присоединился")
               counter+=1
               #После первого зарегистрировавшегося выводим сообщение с участниками
               bot.send_message(call.message.chat.id, name+"\nДо конца регистрации осталось 90 секунд")
               #После первого нажатия пользователя запускаем цикл на 90 секунд, после которого регистрация заканчивается и начинается игра
               time.sleep(30)
               bot.send_message(call.message.chat.id, name+"\nДо конца регистрации осталось 60 секунд")
               time.sleep(30)
               bot.send_message(call.message.chat.id, name+"\nДо конца регистрации осталось 30 секунд")
               time.sleep(30)
               bot.send_message(call.message.chat.id, name+"\nРегистрация окончена, игра начинается)")
               #Удаляем кнопку регистрации
               bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
               if counter<3:
                  startGameValue=0
                  exitgame=1
                  markupOver = types.InlineKeyboardMarkup()
                  switch_button = types.InlineKeyboardButton(text='Начать новую игру', callback_data='res')
                  markupOver.add(switch_button)
                  print("Игра завершена, недостаточно игроков")
                  bot.send_message(chatId, "Недостаточно игроков, попробуйте позже!\nДля перезапуска игры, по братски, нажми кнопочку ниже!", reply_markup = markupOver)
               elif counter<6:
                  print("В игре меньше 6 человек, раздаем роли")
                  bot.send_message(call.message.chat.id, "В игре: одна мафия, одна блудница, один доктор, остальные мир")
                  for i in Maf3_5: #Перебираем массив с ролями и присваиваем каждую роль рандомному игроку
                     win=0 #Обнуляем переменную успеха
                     while win==0: #Пока не присвоим роль будем выполнять цикл
                        randomRol=random.randrange(counter) #Получаем рандомное число из диапазона игроков
                        if UserMas[randomRol][3]=='мир': #Если пользователь мир, то присваиваем ему роль
                           UserMas[randomRol][3]=i
                           win=1 #Выходим из цикла при удаче
               elif counter<9:
                  print("В игре меньше 9 человек, раздаем роли")
                  bot.send_message(call.message.chat.id, "В игре: две мафии, одна блудница, один доктор, один ментяра, остальные мир")
                  for i in Maf6_8: #Перебираем массив с ролями и присваиваем каждую роль рандомному игроку
                     win=0 #Обнуляем переменную успеха
                     while win==0: #Пока не присвоим роль будем выполнять цикл
                        randomRol=random.randrange(counter) #Получаем рандомное число из диапазона игроков
                        if UserMas[randomRol][3]=='мир': #Если пользователь мир, то присваиваем ему роль
                           UserMas[randomRol][3]=i
                           win=1 #Выходим из цикла при удаче
               elif counter<11:
                  print("В игре меньше 11 человек, раздаем роли")
                  bot.send_message(call.message.chat.id, "В игре: три мафии, одна блудница, один доктор, один ментяра, один лейтенант, остальные мир")
                  for i in Maf9_10: #Перебираем массив с ролями и присваиваем каждую роль рандомному игроку
                     win=0 #Обнуляем переменную успеха
                     while win==0: #Пока не присвоим роль будем выполнять цикл
                        randomRol=random.randrange(counter) #Получаем рандомное число из диапазона игроков
                        if UserMas[randomRol][3]=='мир': #Если пользователь мир, то присваиваем ему роль
                           UserMas[randomRol][3]=i
                           win=1 #Выходим из цикла при удаче
               elif counter<15:
                  print("В игре меньше 15 человек, раздаем роли")
                  bot.send_message(call.message.chat.id, "В игре: четыре мафии, одна блудница, один доктор, один ментяра, один лейтенант, остальные мир")
                  for i in Maf11_14: #Перебираем массив с ролями и присваиваем каждую роль рандомному игроку
                     win=0 #Обнуляем переменную успеха
                     while win==0: #Пока не присвоим роль будем выполнять цикл
                        randomRol=random.randrange(counter) #Получаем рандомное число из диапазона игроков
                        if UserMas[randomRol][3]=='мир': #Если пользователь мир, то присваиваем ему роль
                           UserMas[randomRol][3]=i
                           win=1 #Выходим из цикла при удаче
               elif counter<19:
                  print("В игре меньше 19 человек, раздаем роли")
                  bot.send_message(call.message.chat.id, "В игре: пять мафий, одна блудница, один доктор, один ментяра, один лейтенант, остальные мир")
                  for i in Maf15_18: #Перебираем массив с ролями и присваиваем каждую роль рандомному игроку
                     win=0 #Обнуляем переменную успеха
                     while win==0: #Пока не присвоим роль будем выполнять цикл
                        randomRol=random.randrange(counter) #Получаем рандомное число из диапазона игроков
                        if UserMas[randomRol][3]=='мир': #Если пользователь мир, то присваиваем ему роль
                           UserMas[randomRol][3]=i
                           win=1 #Выходим из цикла при удаче
               else:
                  print("В игре больше 19 человек, раздаем роли")
                  maf=counter//3-5 #Вычисляем сколько мафий нужно добавить
                  bot.send_message(call.message.chat.id, "В игре: "+str(maf+5)+" мафий, одна блудница, один доктор, один ментяра, два лейтенанта, остальные мир")
                  for number in range(maf):  #Добавляем мафию в список если недостаточно их
                     Maf19_next.append('мафия')
                  for i in Maf19_next: #Перебираем массив с ролями и присваиваем каждую роль рандомному игроку
                     win=0 #Обнуляем переменную успеха
                     while win==0: #Пока не присвоим роль будем выполнять цикл
                        randomRol=random.randrange(counter) #Получаем рандомное число из диапазона игроков
                        if UserMas[randomRol][3]=='мир': #Если пользователь мир, то присваиваем ему роль
                           UserMas[randomRol][3]=i
                           win=1 #Выходим из цикла при удаче
               #Если игроки набрались то запускаем игру
               if counter>2:
                  print("Начинаем игру")
                  bot.send_message(call.message.chat.id, "Игра начинается!")
                  #Обнуляем данные
                  MentKill=" "
                  checkment=" "
                  bludwork=" "
                  doctorwork=" "
                  donwork=" "
                  markupNight = types.InlineKeyboardMarkup()
                  switch_button = types.InlineKeyboardButton(text='Перейти к боту', url='https://t.me/MafiaMini_bot')
                  markupNight.add(switch_button)
                  bot.send_photo(call.message.chat.id, 'AgACAgIAAxkBAAIFN15-ajqMQhKUJA0BcgN8ENa72lmDAAIxrjEbbVr4S_0iyaU7dtjxTJTCDwAEAQADAgADbQADnhgGAAEYBA', "Наступает ночь\nНа улицы города выходят лишь самые отважные и бесстрашные. Утром попробуем сосчитать их головы...", reply_markup = markupNight)
                  print("Рассылаем сообщения с ролями игрокам")
                  #Рассылаем сообщения с ролями и прикрепляем действия
                  for j in range(counter):
                     if UserMas[j][3]=="мир":
                        mir_list+="Мир - "+str(UserMas[j][2])+"\n"
                        bot.send_message(UserMas[j][1], "Твоя роль: мирный житель!\nСтарайтесь вычислить мафию!")
                     
                     elif UserMas[j][3]=="камикадзе":
                        mir_list+="Камикадзе - "+str(UserMas[j][2])+"\n"
                        bot.send_message(UserMas[j][1], "Твоя роль: камикадзе!\nСтарайтесь совершить суисайд на дневном бунте!")
                     elif UserMas[j][3]=="мафия":
                        mafia_don_list+="Мафия - "+str(UserMas[j][2])+"\n"
                        #Перебираем массив и записываем туда всех мафий кроме того, кому отправляем сообщение
                        Maf_maf=" "
                        for rf in range(len(UserMas)):
                           if UserMas[rf][3]=="мафия" and rf!=j:
                              Maf_maf+="\nМафия - "+UserMas[rf][3]
                        for r in range(len(UserMas)):
                           if UserMas[r][3]=="дон":
                              bot.send_message(UserMas[j][1], "Твоя роль: мафия!\nМешай вычислить Дона и мафию!\nДон - "+str(UserMas[r][3])+str(Maf_maf))
                     elif UserMas[j][3]=="дон":
                        mafia_don_list+="Дон - "+str(UserMas[j][2])+"\n"
                        #Создаем кнопки под сообщением со списком игроков
                        markup = types.InlineKeyboardMarkup(row_width=1)
                        #Перебираем массив и если ты не дон, то выводим остальных в кнопках
                        for k in range(len(UserMas)):
                           if UserMas[k][3]!="дон":
                              if UserMas[k][3]!="мафия":
                                 markup.add(types.InlineKeyboardButton(UserMas[k][2], callback_data='дон'+UserMas[k][0]))
                              else:
                                 markup.add(types.InlineKeyboardButton(UserMas[k][2], callback_data='дон'+UserMas[k][0])+" - мафия")
                        #Отправляе сообщение и прикрепляем клавиатуру
                        bot.send_message(UserMas[j][1], "Твоя роль: Дон - глава мафии!\nКого будем убивать?", reply_markup=markup)
                        #Собираем список мафии
                        mafialist="Твои помощники мафиозники: "
                        MafCount=0
                        for k in range(len(UserMas)):
                           if UserMas[k][3]=="мафия":
                              mafialist+="\n"+UserMas[k][2]
                              MafCount=1
                        if MafCount==1:
                           bot.send_message(UserMas[j][1], str(mafialist))
                     elif UserMas[j][3]=="доктор":
                        mir_list+="Доктор - "+str(UserMas[j][2])+"\n"
                        #Создаем кнопки под сообщением со списком игроков
                        markupdoc = types.InlineKeyboardMarkup(row_width=1)
                        #Перебираем массив и выводим игроков в кнопках
                        for k in range(len(UserMas)):
                           markupdoc.add(types.InlineKeyboardButton(UserMas[k][2], callback_data='доктор'+UserMas[k][0]))
                        #Отправляе сообщение и прикрепляем клавиатуру
                        bot.send_message(UserMas[j][1], "Твоя роль: доктор!\nКого будем лечить?", reply_markup=markupdoc)
                     elif UserMas[j][3]=="ментяра":
                        mir_list+="Ментяра - "+str(UserMas[j][2])+"\n"
                        #Создаем кнопки под сообщением со списком игроков
                        markupment = types.InlineKeyboardMarkup(row_width=2)
                        #Перебираем действия
                        markupment.add(types.InlineKeyboardButton("Убивать!", callback_data='убить'))
                        markupment.add(types.InlineKeyboardButton("Проверять!", callback_data='проверить'))
                        #Отправляе сообщение и прикрепляем клавиатуру
                        bot.send_message(UserMas[j][1], "Твоя роль: ментяра!\nБудем проверять или убивать?", reply_markup=markupment)
                     elif UserMas[j][3]=="лейтенант":
                        mir_list+="Лейтенант - "+str(UserMas[j][2])+"\n"
                        #Перебираем массив и записываем туда всех лейтенантов кроме того, кому отправляем сообщение
                        Ment_ment=" "
                        for rf in range(len(UserMas)):
                           if UserMas[rf][3]=="лейтенант" and rf!=j:
                              Ment_ment+="\nЛейтенант - "+UserMas[rf][3]
                        for r in range(len(UserMas)):
                           if UserMas[r][3]=="ментяра":
                              bot.send_message(UserMas[j][1], "Твоя роль: лейтенант!\nПомогай вычислить Дона и мафию!\nМентяра - "+str(UserMas[r][3])+str(Ment_ment))
                     elif UserMas[j][3]=="блудница":
                        mir_list+="Блдница - "+str(UserMas[j][2])+"\n"
                        #Создаем кнопки под сообщением со списком игроков
                        markupblud = types.InlineKeyboardMarkup(row_width=1)
                        #Перебираем массив и выводим игроков в кнопках
                        for k in range(len(UserMas)):
                           if UserMas[k][3]!="блудница":
                              markupblud.add(types.InlineKeyboardButton(UserMas[k][2], callback_data='блудница'+UserMas[k][0]))
                        #Отправляе сообщение и прикрепляем клавиатуру
                        bot.send_message(UserMas[j][1], "Твоя роль: блудница!\nС кем будем спать?", reply_markup=markupblud)
                  time.sleep(45) #Ждем перед обработкой команды
                  bot.send_message(chatId, "До восхода солнца осталось 15 секунд...)")
                  time.sleep(15)
                  print("Наступает день, начинаем обрабатывать действия")
                  #Если шлюха и мент сходили к одному человеку то говорим что он не мафия
                  print("Шлюха сходила к "+str(bludwork))
                  print("Мент сходил к "+str(checkment))
                  if bludwork==checkment:
                     for k in range(len(UserMas)):
                        if UserMas[k][0]==checkment:
                           print("Шлюха скрыла роль")
                           bot.send_message(mentid, str(UserMas[k][2])+" - мирный житель")
                  else:#Если к разным то проверяем жителя
                     for kq in range(len(UserMas)):
                        if UserMas[kq][0]==checkment:
                           if UserMas[kq][3]=="дон":
                              print("Мент нашел дона")
                              bot.send_message(mentid, str(UserMas[kq][2])+" - дон")
                           elif UserMas[kq][3]=="мафия":
                              print("Мент нашел мафию")
                              bot.send_message(mentid, str(UserMas[kq][2])+" - мафия")
                           else:
                              print("Мент проверил мирного")
                              bot.send_message(mentid, str(UserMas[kq][2])+" - "+str(UserMas[kq][3]))
                  print("Определяе убитых")
                  print("Доктор лечил "+str(doctorwork))
                  #Перебираем массив и убиваем того, кого выбрал дон
                  for do in range(len(UserMas)):
                     if UserMas[do][0]==donwork:
                        UserMas[do][4]="убит"
                  #Перебираем массив и убиваем того, кого выбрал мент
                  for dom in range(len(UserMas)):
                     if UserMas[dom][0]==MentKill:
                        UserMas[dom][4]="убит"
                  #Оживляем убитого
                  for p in range(len(UserMas)):
                     if UserMas[p][0]==doctorwork:
                        UserMas[p][4]="живой"
                  print("Считаем убитых")
                  #Считаем убитых игроков
                  kill=0
                  kill1=-1
                  #Проходим по массиву и считаем убитых и запоминаем индекс убитого
                  for n in range(len(UserMas)):
                     if UserMas[n][4]=="убит":
                        kill+=1
                        kill1=n
                  if kill==0:
                     print("Этой ночью никого не убили")
                     bot.send_message(call.message.chat.id, "Странно, но этой ночью никто не умер...")
                  if kill==1: #Если убили одного, то удаляем его из массива
                     #Если убили дона, то отдаем его роль одному из мафии
                     if UserMas[kill1][3]=="дон":
                        mafia_don=0
                        for d in range(len(UserMas)):
                           if UserMas[d][3]=="мафия" and mafia_don==0:
                              UserMas[d][3]="дон"
                              print("Теперь дон "+str(UserMas[d][2]))
                              bot.send_message(UserMas[d][1], "Главу мафии убили, теперь ты дон! ")
                              mafia_don+=1
                     #Если убили ментяру, то отдаем его роль одному из лейтенантов
                     if UserMas[kill1][3]=="ментяра":
                        ment_le=0
                        for d in range(len(UserMas)):
                           if UserMas[d][3]=="лейтенант" and ment_le==0:
                              UserMas[d][3]="ментяра"
                              print("Теперь ментяра "+str(UserMas[d][2]))
                              bot.send_message(UserMas[d][1], "Главу полиции убили, теперь ты ментяра! ")
                              ment_le+=1
                     print("Этой ночью был зверски убит "+str(UserMas[kill1][3])+" - "+str(UserMas[kill1][2]))
                     bot.send_message(UserMas[kill1][1], "Этой ночью тебя убили")
                     bot.send_message(call.message.chat.id, "Этой ночью был зверски убит "+str(UserMas[kill1][3])+" - "+str(UserMas[kill1][2]))
                     Killmas.append(UserMas[kill1]) #Добавляем человека в массив убитых
                     bot.restrict_chat_member(GROUP_ID, UserMas[kill1][1], can_send_messages=False) #Блокируем чат для умершого
                     UserMas.pop(kill1)
                  if kill==2: #Если убили двух, то удаляем еще одного
                     for nf in range(len(UserMas)):
                        if UserMas[nf][4]=="убит":
                           kill1=nf
                     #Если убили дона, то отдаем его роль одному из мафии
                     if UserMas[kill1][3]=="дон":
                        mafia_don=0
                        for d in range(len(UserMas)):
                           if UserMas[d][3]=="мафия" and mafia_don==0:
                              UserMas[d][3]="дон"
                              print("Теперь дон "+str(UserMas[d][2]))
                              bot.send_message(UserMas[d][1], "Главу мафии убили, теперь ты дон! ")
                              mafia_don+=1
                     #Если убили ментяру, то отдаем его роль одному из лейтенантов
                     if UserMas[kill1][3]=="ментяра":
                        ment_le=0
                        for d in range(len(UserMas)):
                           if UserMas[d][3]=="лейтенант" and ment_le==0:
                              UserMas[d][3]="ментяра"
                              print("Теперь ментяра "+str(UserMas[d][2]))
                              bot.send_message(UserMas[d][1], "Главу полиции убили, теперь ты ментяра! ")
                              ment_le+=1
                     print("Так же ночью убили "+str(UserMas[kill1][3])+" - "+str(UserMas[kill1][2]))
                     bot.send_message(UserMas[kill1][1], "Этой ночью тебя убили")
                     bot.send_message(call.message.chat.id, "Так же, этой ночью умер "+str(UserMas[kill1][3])+" - "+str(UserMas[kill1][2]))
                     Killmas.append(UserMas[kill1]) #Добавляем человека в массив убитых
                     bot.restrict_chat_member(GROUP_ID, UserMas[kill1][1], can_send_messages=False) #Блокируем чат для умершого
                     UserMas.pop(kill1)
                  kill=0 #Обнуляем колличество убитых
                  print('Список живых игроков: '+str(UserMas))
                  #Перебираем массив игроков и определяем есть ли победитель, если победителя нет то запускаем круговой цикл
                  #Запускаем игру по кругу, пока в ней не закончатся участники
                  exitgame=0
                  while exitgame==0:
                     print('Проверяем есть ли живые игроки')
                     if range(len(UserMas))!=0: #Если игроки еще есть, то проверяем есть ли победитель
                        mafWin=0
                        mirWin=0
                        for vin in range(len(UserMas)):
                           #Если дон жив, то проверяем живы ли мирные
                           if UserMas[vin][3]=="дон":
                              mafWin=1
                           elif UserMas[vin][3]!="дон":
                              mirWin+=1
                        if mafWin==0: #Если мафию убили, то победили мирные
                           #Если камикадзе повесили то заносим его в список победителей
                           if suisad==1:
                              print('Мафия мертва, победили мирные и камикадзе, завершаем игру')
                              markupOver = types.InlineKeyboardMarkup()
                              switch_button = types.InlineKeyboardButton(text='Начать новую игру', callback_data='res')
                              markupOver.add(switch_button)
                              bot.send_photo(call.message.chat.id, 'AgACAgIAAxkBAAIFNV5-aNJaMyY9FpQxlJiFOP8z5t4AA4ytMRuss_FLy-QcXdea6YWPLO6RLgADAQADAgADeAADWCUAAhgE', "Игра окончена, победили мирные и камикадзе!\n"+mafia_don_list+mir_list, reply_markup = markupOver)
                              exitgame=1
                              startGameValue=0
                              for clearing in range(len(Killmas)):
                                 bot.restrict_chat_member(GROUP_ID, UserMas[clearing][1], can_send_messages=True) #Разблокируем чат после игры
                              break
                           else:
                              print('Мафия мертва, победили мирные, завершаем игру')
                              markupOver = types.InlineKeyboardMarkup()
                              switch_button = types.InlineKeyboardButton(text='Начать новую игру', callback_data='res')
                              markupOver.add(switch_button)
                              bot.send_photo(call.message.chat.id, 'AgACAgIAAxkBAAIFNV5-aNJaMyY9FpQxlJiFOP8z5t4AA4ytMRuss_FLy-QcXdea6YWPLO6RLgADAQADAgADeAADWCUAAhgE', "Игра окончена, победили мирные!\n"+mafia_don_list+mir_list, reply_markup = markupOver)
                              exitgame=1
                              startGameValue=0
                              for clearing in range(len(Killmas)):
                                 bot.restrict_chat_member(GROUP_ID, UserMas[clearing][1], can_send_messages=True) #Разблокируем чат после игры
                              break
                        elif mirWin<2: #Если мирных меньше двух, то победила мафия
                           #Если камикадзе повесили то заносим его в список победителей
                           if suisad==1:
                              print('Мирные мертвы, победила мафия и камикадзе, завершаем игру')
                              markupOver = types.InlineKeyboardMarkup()
                              switch_button = types.InlineKeyboardButton(text='Начать новую игру', callback_data='res')
                              markupOver.add(switch_button)
                              bot.send_photo(call.message.chat.id, 'AgACAgIAAxkBAAIFNV5-aNJaMyY9FpQxlJiFOP8z5t4AA4ytMRuss_FLy-QcXdea6YWPLO6RLgADAQADAgADeAADWCUAAhgE', "Игра окончена, победила мафия и камикадзе!\n"+mafia_don_list+mir_list, reply_markup = markupOver)
                              exitgame=1
                              startGameValue=0
                              for clearing in range(len(Killmas)):
                                 bot.restrict_chat_member(GROUP_ID, UserMas[clearing][1], can_send_messages=True) #Разблокируем чат после игры
                              break
                           else:
                              print('Мирные мертвы, победила мафия, завершаем игру')
                              markupOver = types.InlineKeyboardMarkup()
                              switch_button = types.InlineKeyboardButton(text='Начать новую игру', callback_data='res')
                              markupOver.add(switch_button)
                              bot.send_photo(call.message.chat.id, 'AgACAgIAAxkBAAIFNV5-aNJaMyY9FpQxlJiFOP8z5t4AA4ytMRuss_FLy-QcXdea6YWPLO6RLgADAQADAgADeAADWCUAAhgE', "Игра окончена, победила мафия!\n"+mafia_don_list+mir_list, reply_markup = markupOver)
                              exitgame=1
                              startGameValue=0
                              for clearing in range(len(Killmas)):
                                 bot.restrict_chat_member(GROUP_ID, UserMas[clearing][1], can_send_messages=True) #Разблокируем чат после игры
                              break
                        else: #Если нет победителя, то продолжаем игру
                           print('Победителя нет, продолжаем игру, наступает день')
                           #После ночи очищаем массив с действиями
                           for dw in range(len(UserMas)):
                              UserMas[dw][6]=0
                           #Выводим сообщение с итогами ночи и списком живых игроков и их ролей 
                           #Перебираем массив участников и записываем их в строку
                           Userstroka="Список живых участников:\n"
                           RolStroka="Кто то из них:\n"
                           for dt in range(len(UserMas)):
                              if UserMas[dt][4]=="живой":
                                 Userstroka+=str(UserMas[dt][2])+"\n"
                           for dtr in range(len(UserMas)):
                              if UserMas[dtr][3]=="дон":
                                 RolStroka+=str(UserMas[dtr][3])
                           for dtr in range(len(UserMas)):
                              if UserMas[dtr][3]=="мафия":
                                 RolStroka+=", "+str(UserMas[dtr][3])
                           for dtr in range(len(UserMas)):
                              if UserMas[dtr][3]=="доктор":
                                 RolStroka+=", "+str(UserMas[dtr][3])
                           for dtr in range(len(UserMas)):
                              if UserMas[dtr][3]=="блудница":
                                 RolStroka+=", "+str(UserMas[dtr][3])
                           for dtr in range(len(UserMas)):
                              if UserMas[dtr][3]=="ментяра":
                                 RolStroka+=", "+str(UserMas[dtr][3])
                           for dtr in range(len(UserMas)):
                              if UserMas[dtr][3]=="лейтенант":
                                 RolStroka+=", "+str(UserMas[dtr][3])
                           for dtr in range(len(UserMas)):
                              if UserMas[dtr][3]=="камикадзе":
                                 RolStroka+=", "+str(UserMas[dtr][3])
                           #Наступает день!
                           markupdayy = types.InlineKeyboardMarkup()
                           switch_button = types.InlineKeyboardButton(text='Перейти к боту', url='https://t.me/MafiaMini_bot')
                           markupdayy.add(switch_button)
                           bot.send_photo(call.message.chat.id, 'AgACAgIAAxkBAAIFOl5-a1UBGQlgn9NINbtQ7FHOZQr0AAIyrjEbbVr4S96ZXQxGesPEHp_CDwAEAQADAgADbQADlw8GAAEYBA', "Ночь закончилась, обсуждайте итоги ночи\n"+str(Userstroka)+str(RolStroka), reply_markup = markupdayy)
                           print('Предлагаем оставшимся участникам найти виновных и повесить их')
                           #Перебираем всех участников и отправляем им клавиатуру
                           for dayr in range(len(UserMas)):
                              #Создаем кнопки под сообщением со списком игроков
                              markupday = types.InlineKeyboardMarkup(row_width=1)
                              #Перебираем массив и выводим игроков в кнопках
                              for k in range(len(UserMas)):
                                 if UserMas[k][0]!=UserMas[dayr][2]: #Выводим всех кроме того, кому отправляем клавиатуру
                                    if UserMas[k][3]=="дон" or UserMas[k][3]=="мафия":
                                       markupday.add(types.InlineKeyboardButton(UserMas[k][2], callback_data='вешаем'+UserMas[k][0]+" - "+UserMas[k][3]))
                                    else:
                                       markupday.add(types.InlineKeyboardButton(UserMas[k][2], callback_data='вешаем'+UserMas[k][0]))
                                 #Отправляе сообщение и прикрепляем клавиатуру
                              bot.send_message(UserMas[dayr][1], "Кого вешать будем?", reply_markup=markupday)
                           time.sleep(45)
                           bot.send_message(chatId, "До наступления ночи осталось 15 секунд...)")
                           time.sleep(15)
                           print('Наступает ночь, обрабатываем результаты дня')
                           print("Список игроков: "+str(UserMas))
                           vechaem=0
                           bufmax=0
                           for vv in range(len(UserMas)):
                              if UserMas[vv][5]>bufmax:
                                 bufmax=UserMas[vv][5]
                           for vcv in range(len(UserMas)):
                              if UserMas[vcv][5]==bufmax:
                                 vechaem+=1
                           if vechaem==1:
                              for vccv in range(len(UserMas)):
                                 if UserMas[vccv][5]==bufmax:
                                    #Вешаем игрока
                                    bot.send_message(call.message.chat.id, "Жители собрались и отмудохали "+UserMas[vccv][3]+" - "+UserMas[vccv][2])
                                    idCill=vccv
                              #Если убили камикадзе, то записываем его в победители
                              if UserMas[idCill][3]=="камикадзе":
                                 suisad=1
                                 bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAIRAV6BIRrwu4Z94iK-G2PYi_rlBqnqAAJiAANSiZEjAAH9A-NAsomPGAQ')
                                 bot.send_message(UserMas[idCill][1], "Красачик, добился своего, ожидай следующую игру")
                              else:
                                 bot.send_message(UserMas[idCill][1], "Тебя отмудохали жители, ожидай следующую игру")
                              print("Жители собрались и отмудохали "+UserMas[idCill][3]+" - "+UserMas[idCill][2])
                              #Если убили дона, то отдаем его роль одному из мафии
                              if UserMas[idCill][3]=="дон":
                                 mafia_don=0
                                 for d in range(len(UserMas)):
                                    if UserMas[d][3]=="мафия" and mafia_don==0:
                                       UserMas[d][3]="дон"
                                       print("Теперь дон "+str(UserMas[d][2]))
                                       bot.send_message(UserMas[d][1], "Главу мафии повесили, теперь ты дон! ")
                                       mafia_don+=1
                              #Если убили ментяру, то отдаем его роль одному из лейтенантов
                              if UserMas[idCill][3]=="ментяра":
                                 ment_le=0
                                 for d in range(len(UserMas)):
                                    if UserMas[d][3]=="лейтенант" and ment_le==0:
                                       UserMas[d][3]="ментяра"
                                       print("Теперь ментяра "+str(UserMas[d][2]))
                                       bot.send_message(UserMas[d][1], "Главу полиции убили, теперь ты ментяра! ")
                                       ment_le+=1
                              Killmas.append(UserMas[idCill]) #Добавляем человека в массив убитых
                              bot.restrict_chat_member(GROUP_ID, UserMas[idCill][1], can_send_messages=False) #Блокируем чат для умершого
                              UserMas.pop(idCill)
                              if range(len(UserMas))!=0: #Если игроки еще есть, то проверяем есть ли победитель
                                 mafWin=0
                                 mirWin=0
                                 for vin in range(len(UserMas)):
                                    #Если дон жив, то проверяем живы ли мирные
                                    if UserMas[vin][3]=="дон":
                                       mafWin=1
                                    elif UserMas[vin][3]!="дон":
                                       mirWin+=1
                                 if mafWin==0: #Если мафию убили, то победили мирные
                                    #Если камикадзе повесили то заносим его в список победителей
                                    if suisad==1:
                                       print('Мафия мертва, победили мирные и камикадзе, завершаем игру')
                                       markupOver = types.InlineKeyboardMarkup()
                                       switch_button = types.InlineKeyboardButton(text='Начать новую игру', callback_data='res')
                                       markupOver.add(switch_button)
                                       bot.send_photo(call.message.chat.id, 'AgACAgIAAxkBAAIFNV5-aNJaMyY9FpQxlJiFOP8z5t4AA4ytMRuss_FLy-QcXdea6YWPLO6RLgADAQADAgADeAADWCUAAhgE', "Игра окончена, победили мирные и камикадзе!\n"+mafia_don_list+mir_list, reply_markup = markupOver)
                                       exitgame=1
                                       startGameValue=0
                                       for clearing in range(len(Killmas)):
                                          bot.restrict_chat_member(GROUP_ID, UserMas[clearing][1], can_send_messages=True) #Разблокируем чат после игры
                                       break
                                    else:
                                       print('Мафия мертва, победили мирные, завершаем игру')
                                       markupOver = types.InlineKeyboardMarkup()
                                       switch_button = types.InlineKeyboardButton(text='Начать новую игру', callback_data='res')
                                       markupOver.add(switch_button)
                                       bot.send_photo(call.message.chat.id, 'AgACAgIAAxkBAAIFNV5-aNJaMyY9FpQxlJiFOP8z5t4AA4ytMRuss_FLy-QcXdea6YWPLO6RLgADAQADAgADeAADWCUAAhgE', "Игра окончена, победили мирные!\n"+mafia_don_list+mir_list, reply_markup = markupOver)
                                       exitgame=1
                                       startGameValue=0
                                       for clearing in range(len(Killmas)):
                                          bot.restrict_chat_member(GROUP_ID, UserMas[clearing][1], can_send_messages=True) #Разблокируем чат после игры
                                       break
                                 elif mirWin<2: #Если мирных больше нет, то победила мафия
                                    #Если камикадзе повесили то заносим его в список победителей
                                    if suisad==1:
                                       print('Мирные мертвы, победила мафия и камикадзе, завершаем игру')
                                       markupOver = types.InlineKeyboardMarkup()
                                       switch_button = types.InlineKeyboardButton(text='Начать новую игру', callback_data='res')
                                       markupOver.add(switch_button)
                                       bot.send_photo(call.message.chat.id, 'AgACAgIAAxkBAAIFNV5-aNJaMyY9FpQxlJiFOP8z5t4AA4ytMRuss_FLy-QcXdea6YWPLO6RLgADAQADAgADeAADWCUAAhgE', "Игра окончена, победила мафия и камикадзе!\n"+mafia_don_list+mir_list, reply_markup = markupOver)
                                       exitgame=1
                                       startGameValue=0
                                       for clearing in range(len(Killmas)):
                                          bot.restrict_chat_member(GROUP_ID, UserMas[clearing][1], can_send_messages=True) #Разблокируем чат после игры
                                       break
                                    else:
                                       print('Мирные мертвы, победила мафия, завершаем игру')
                                       markupOver = types.InlineKeyboardMarkup()
                                       switch_button = types.InlineKeyboardButton(text='Начать новую игру', callback_data='res')
                                       markupOver.add(switch_button)
                                       bot.send_photo(call.message.chat.id, 'AgACAgIAAxkBAAIFNV5-aNJaMyY9FpQxlJiFOP8z5t4AA4ytMRuss_FLy-QcXdea6YWPLO6RLgADAQADAgADeAADWCUAAhgE', "Игра окончена, победила мафия!\n"+mafia_don_list+mir_list, reply_markup = markupOver)
                                       exitgame=1
                                       startGameValue=0
                                       for clearing in range(len(Killmas)):
                                          bot.restrict_chat_member(GROUP_ID, UserMas[clearing][1], can_send_messages=True) #Разблокируем чат после игры
                                       break
                                 else: #Если нет победителя, то продолжаем игру
                                    print('Победителя нет, продолжаем игру')
                                    #Выводим сообщение с итогами ночи и списком живых игроков и их ролей 
                                    #Перебираем массив участников и записываем их в строку
                                    Userstroka="Список живых участников:\n"
                                    RolStroka="Кто то из них:\n"
                                    for dt in range(len(UserMas)):
                                       if UserMas[dt][4]=="живой":
                                          Userstroka+=str(UserMas[dt][2])+"\n"
                                    for dtr1 in range(len(UserMas)):
                                       if UserMas[dtr1][3]=="дон":
                                          RolStroka+=str(UserMas[dtr1][3])
                                    for dtr2 in range(len(UserMas)):
                                       if UserMas[dtr2][3]=="мафия":
                                          RolStroka+=", "+str(UserMas[dtr2][3])
                                    for dtr3 in range(len(UserMas)):
                                       if UserMas[dtr3][3]=="доктор":
                                          RolStroka+=", "+str(UserMas[dtr3][3])
                                    for dtr4 in range(len(UserMas)):
                                       if UserMas[dtr4][3]=="блудница":
                                          RolStroka+=", "+str(UserMas[dtr4][3])
                                    for dtr5 in range(len(UserMas)):
                                       if UserMas[dtr5][3]=="ментяра":
                                          RolStroka+=", "+str(UserMas[dtr5][3])
                                    for dtr6 in range(len(UserMas)):
                                       if UserMas[dtr6][3]=="лейтенант":
                                          RolStroka+=", "+str(UserMas[dtr6][3])
                                    for dtr7 in range(len(UserMas)):
                                       if UserMas[dtr7][3]=="камикадзе":
                                          RolStroka+=", "+str(UserMas[dtr7][3])
                           else: #Никого не повесили
                              print('Жители не смогли решить кого повесить и разошлись')
                              print("Список жителей: "+str(UserMas))
                              bot.send_message(call.message.chat.id, "Жители не смогли решить кого вешать и разошлись")
                           #Очищаем результаты голосования и действий
                           for vclear in range(len(UserMas)):
                              UserMas[vclear][5]=0
                              UserMas[vclear][6]=0
                           #День заканчивается, наступает ночь!
                           print("Очистили результаты голосования "+str(UserMas))
                           print('Наступает ночь')
                           #Обнуляем данные
                           MentKill=" "
                           checkment=" "
                           bludwork=" "
                           doctorwork=" "
                           donwork=" "
                           markupNight = types.InlineKeyboardMarkup()
                           switch_button = types.InlineKeyboardButton(text='Перейти к боту', url='https://t.me/MafiaMini_bot')
                           markupNight.add(switch_button)
                           bot.send_photo(call.message.chat.id, 'AgACAgIAAxkBAAIFN15-ajqMQhKUJA0BcgN8ENa72lmDAAIxrjEbbVr4S_0iyaU7dtjxTJTCDwAEAQADAgADbQADnhgGAAEYBA', "Наступает ночь\nНа улицы города выходят лишь самые отважные и бесстрашные. Утром попробуем сосчитать их головы...", reply_markup = markupNight)
                           print('Рассылаем сообщения с ролями активным игрокам')
                           #Рассылаем сообщения с ролями и прикрепляем действия
                           for j in range(len(UserMas)):
                              if UserMas[j][3]=="дон":
                                 #Создаем кнопки под сообщением со списком игроков
                                 markup = types.InlineKeyboardMarkup(row_width=1)
                                 #Перебираем массив и если ты не дон, то выводим остальных в кнопках
                                 for k in range(len(UserMas)):
                                    if UserMas[k][3]!="дон":
                                       if UserMas[k][3]!="мафия":
                                          markup.add(types.InlineKeyboardButton(UserMas[k][2], callback_data='дон'+UserMas[k][0]))
                                       else:
                                          markup.add(types.InlineKeyboardButton(UserMas[k][2], callback_data='дон'+UserMas[k][0])+" - мафия")
                                 #Отправляе сообщение и прикрепляем клавиатуру
                                 bot.send_message(UserMas[j][1], "Дон, кого будем убивать?", reply_markup=markup)
                                 #Собираем список мафии
                                 mafialist="Твои помощники мафиозники: "
                                 MafCount=0
                                 for k in range(len(UserMas)):
                                    if UserMas[k][3]=="мафия":
                                       mafialist+="\n"+UserMas[k][2]
                                       MafCount=1
                                 if MafCount==1:
                                    bot.send_message(UserMas[j][1], str(mafialist))
                              elif UserMas[j][3]=="доктор":
                                 #Создаем кнопки под сообщением со списком игроков
                                 markupdoc = types.InlineKeyboardMarkup(row_width=1)
                                 #Перебираем массив и выводим игроков в кнопках
                                 for k in range(len(UserMas)):
                                    if UserMas[k][0]!=doctorworkBuf:
                                       markupdoc.add(types.InlineKeyboardButton(UserMas[k][2], callback_data='доктор'+UserMas[k][0]))
                                 #Отправляе сообщение и прикрепляем клавиатуру
                                 bot.send_message(UserMas[j][1], "Доктор, кого будем лечить?", reply_markup=markupdoc)
                                 doctorworkBuf=0
                              elif UserMas[j][3]=="ментяра":
                                 #Создаем кнопки под сообщением со списком игроков
                                 markupment = types.InlineKeyboardMarkup(row_width=2)
                                 #Перебираем действия
                                 markupment.add(types.InlineKeyboardButton("Убивать!", callback_data='убить'))
                                 markupment.add(types.InlineKeyboardButton("Проверять!", callback_data='проверить'))
                                 #Отправляе сообщение и прикрепляем клавиатуру
                                 bot.send_message(UserMas[j][1], "Ментяра, будем проверять или убивать?", reply_markup=markupment)
                              elif UserMas[j][3]=="блудница":
                                 #Создаем кнопки под сообщением со списком игроков
                                 markupblud = types.InlineKeyboardMarkup(row_width=1)
                                 #Перебираем массив и выводим игроков в кнопках
                                 for k in range(len(UserMas)):
                                    if UserMas[k][3]!="блудница":
                                       markupblud.add(types.InlineKeyboardButton(UserMas[k][2], callback_data='блудница'+UserMas[k][0]))
                                 #Отправляе сообщение и прикрепляем клавиатуру
                                 bot.send_message(UserMas[j][1], "Кого сегодня будем радовать?", reply_markup=markupblud)
                           time.sleep(45) #Ждем перед обработкой команды
                           bot.send_message(chatId, "До восхода солнца осталось 15 секунд...)")
                           time.sleep(15)
                           print("Наступает день, начинаем обрабатывать действия")
                           #Если шлюха и мент сходили к одному человеку то говорим что он не мафия
                           #После ночи очищаем массив с действиями
                           for dw in range(len(UserMas)):
                              UserMas[dw][6]=0
                           print("Шлюха сходила к "+str(bludwork))
                           print("Мент сходил к "+str(checkment))
                           if bludwork==checkment:
                              for k in range(len(UserMas)):
                                 if UserMas[k][0]==checkment:
                                    print("Шлюха скрыла роль")
                                    bot.send_message(mentid, str(UserMas[k][2])+" - мирный житель")
                           else:#Если к разным то проверяем жителя
                              for kq in range(len(UserMas)):
                                 if UserMas[kq][0]==checkment:
                                    if UserMas[kq][3]=="дон":
                                       print("Мент нашел дона")
                                       bot.send_message(mentid, str(UserMas[kq][2])+" - дон")
                                    elif UserMas[kq][3]=="мафия":
                                       print("Мент нашел мафию")
                                       bot.send_message(mentid, str(UserMas[kq][2])+" - мафия")
                                    else:
                                       print("Мент проверил мирного")
                                       bot.send_message(mentid, str(UserMas[kq][2])+" - "+str(UserMas[kq][3]))
                           print("Определяе убитых")
                           print("Доктор лечил "+str(doctorwork))
                           #Перебираем массив и убиваем того, кого выбрал дон
                           for do in range(len(UserMas)):
                              if UserMas[do][0]==donwork:
                                 UserMas[do][4]="убит"
                           #Перебираем массив и убиваем того, кого выбрал мент
                           for dom in range(len(UserMas)):
                              if UserMas[dom][0]==MentKill:
                                 UserMas[dom][4]="убит"
                           #Оживляем убитого
                           for p in range(len(UserMas)):
                              if UserMas[p][0]==doctorwork:
                                 UserMas[p][4]="живой"
                           print("Считаем убитых")
                           #Считаем убитых игроков
                           kill=0
                           kill1=-1
                           #Проходим по массиву и считаем убитых и запоминаем индекс убитого
                           for n in range(len(UserMas)):
                              if UserMas[n][4]=="убит":
                                 kill+=1
                                 kill1=n
                           if kill==0:
                              print("Этой ночью никого не убили")
                              bot.send_message(call.message.chat.id, "Странно, но этой ночью никто не умер...")
                           if kill==1: #Если убили одного, то удаляем его из массива
                              #Если убили дона, то отдаем его роль одному из мафии
                              if UserMas[kill1][3]=="дон":
                                 mafia_don=0
                                 for d in range(len(UserMas)):
                                    if UserMas[d][3]=="мафия" and mafia_don==0:
                                       UserMas[d][3]="дон"
                                       print("Теперь дон "+str(UserMas[d][2]))
                                       mafia_don+=1
                              #Если убили ментяру, то отдаем его роль одному из лейтенантов
                              if UserMas[kill1][3]=="ментяра":
                                 ment_le=0
                                 for d in range(len(UserMas)):
                                    if UserMas[d][3]=="лейтенант" and ment_le==0:
                                       UserMas[d][3]="ментяра"
                                       print("Теперь ментяра "+str(UserMas[d][2]))
                                       bot.send_message(UserMas[d][1], "Главу полиции убили, теперь ты ментяра! ")
                                       ment_le+=1
                              print("Этой ночью был зверски убит "+str(UserMas[kill1][3])+" - "+str(UserMas[kill1][2]))
                              bot.send_message(UserMas[kill1][1], "Этой ночью тебя убили")
                              bot.send_message(call.message.chat.id, "Этой ночью был зверски убит "+str(UserMas[kill1][3])+" - "+str(UserMas[kill1][2]))
                              Killmas.append(UserMas[kill1]) #Добавляем человека в массив убитых
                              bot.restrict_chat_member(GROUP_ID, UserMas[kill1][1], can_send_messages=False) #Блокируем чат для умершого
                              UserMas.pop(kill1)
                           if kill==2: #Если убили двух, то удаляем еще одного
                              for nf in range(len(UserMas)):
                                 if UserMas[nf][4]=="убит":
                                    kill1=nf
                              #Если убили дона, то отдаем его роль одному из мафии
                              if UserMas[kill1][3]=="дон":
                                 mafia_don=0
                                 for d in range(len(UserMas)):
                                    if UserMas[d][3]=="мафия" and mafia_don==0:
                                       UserMas[d][3]="дон"
                                       print("Теперь дон "+str(UserMas[d][2]))
                                       bot.send_message(UserMas[d][1], "Главу мафии убили, теперь ты дон! ")
                                       mafia_don+=1
                              #Если убили ментяру, то отдаем его роль одному из лейтенантов
                              if UserMas[kill1][3]=="ментяра":
                                 ment_le=0
                                 for d in range(len(UserMas)):
                                    if UserMas[d][3]=="лейтенант" and ment_le==0:
                                       UserMas[d][3]="ментяра"
                                       print("Теперь ментяра "+str(UserMas[d][2]))
                                       bot.send_message(UserMas[d][1], "Главу полиции убили, теперь ты ментяра! ")
                                       ment_le+=1
                              print("Так же ночью убили "+str(UserMas[kill1][3])+" - "+str(UserMas[kill1][2]))
                              bot.send_message(UserMas[kill1][1], "Этой ночью тебя убили")
                              bot.send_message(call.message.chat.id, "Так же, этой ночью умер "+str(UserMas[kill1][3])+" - "+str(UserMas[kill1][2]))
                              Killmas.append(UserMas[kill1]) #Добавляем человека в массив убитых
                              bot.restrict_chat_member(GROUP_ID, UserMas[kill1][1], can_send_messages=False) #Блокируем чат для умершого
                              UserMas.pop(kill1)
                           kill=0 #Обнуляем колличество убитых
                           print('Список живых игроков: '+str(UserMas))
                     else: #Если все умерли то говорим, что победителя нет и выходим из цикла
                        print('Игра завершена, все умерли, победителя нет')
                        exitgame=1
                        startGameValue=0
                        for clearing in range(len(Killmas)):
                           bot.restrict_chat_member(GROUP_ID, UserMas[clearing][1], can_send_messages=True) #Разблокируем чат после игры
                        markupOver = types.InlineKeyboardMarkup()
                        switch_button = types.InlineKeyboardButton(text='Начать новую игру', callback_data='res')
                        markupOver.add(switch_button)
                        bot.send_photo(call.message.chat.id, 'AgACAgIAAxkBAAIFNV5-aNJaMyY9FpQxlJiFOP8z5t4AA4ytMRuss_FLy-QcXdea6YWPLO6RLgADAQADAgADeAADWCUAAhgE', "Игра окончена, победителя нет!\n"+mafia_don_list+mir_list, reply_markup = markupOver)
            elif counter>0:#Если уже есть пользователь проверяем его уникальность
               i=0
               s=0
               bufCounter=counter #Буферная переменная счетчика
               while i<counter:
                  if UserMas[i][0]!=call.from_user.username: #Если юзер из массива уникальный, то записываем его
                     s+=1 #Считаем уникальность пользователя, она должна быть равна колличеству участников
                     if s==counter:
                        UserMasItem=[]
                        if call.from_user.username==None:   #Если нет ника, то ставим имя
                           UserMasItem.append(str(call.from_user.first_name)+str(counter+1))
                        else:
                           UserMasItem.append(call.from_user.username)    #Добавляем ник игрока
                        UserMasItem.append(call.from_user.id)       #Добавляем id игрока
                        if call.from_user.last_name==None:
                           UserMasItem.append(call.from_user.first_name)#Добавляем имя игрока, если фамилии нет
                        else:
                           UserMasItem.append(call.from_user.last_name)#Добавляем фамилию игрока
                        UserMasItem.append('мир')                   #Добавляем должность, по умолчанию мир
                        UserMasItem.append('живой')                 #Добавляем статус, по умолчанию живой
                        UserMasItem.append(0)                       #Добавляем голосов, по умолчанию 0
                        UserMasItem.append(0)                       #Добавляем действие совершено, по умолчанию 0
                        UserMas.append(UserMasItem)                 #Добавляем наш обьект пользователя в массив
                        name+=str(UserMas[counter][2])+'\n'
                        print('Присоединился к игре: '+str(UserMas[counter][0]))
                        print('Список игроков: '+str(UserMas))
                        counter+=1
                        #Меняем сообщение с колличеством участников
                        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id+1, text=name)
                  if bufCounter==counter: #Если счетчик не изменился, значит пользователь старый
                     if warningUser==0:
                        bot.send_message(call.from_user.id, call.from_user.username+", ты уже зарегистрирован, хватит клацать!")
                        warningUser+=1
                  i+=1
         if call.data[:3] == "дон": #Дон сделал выбор
            #Проверяем делал ли дон уже выстрел
            for dia in range(len(UserMas)):
               if UserMas[dia][3]=="дон" and UserMas[dia][6]==0:
                  UserMas[dia][6]=1
                  print('дон выстрелил в : '+str(call.data[3:]))
                  bot.send_message(chatId, "Дон сделал свой выбор")
                  #Перебираем массив, если пользователь еще жив то даем сделать выбор
                  for ms in range(len(UserMas)):
                     if UserMas[ms][0]==call.data[3:]:
                        for m in range(len(UserMas)):
                           if UserMas[m][0]==call.data[3:]:
                              donwork=UserMas[m][0]
            #Удаляем кнопку 
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
         if call.data[:6] == 'доктор': #Доктор сделал выбор
            #Проверяем лечил ли же доктор
            for dia in range(len(UserMas)):
               if UserMas[dia][3]=="доктор" and UserMas[dia][6]==0:
                  UserMas[dia][6]=1
                  print('доктор вылечил: '+str(call.data[6:]))
                  #Если такой игрок есть то лечим его
                  for md in range(len(UserMas)):
                     if UserMas[md][0]==call.data[6:]:
                        doctorwork=call.data[6:]
                        doctorworkBuf=doctorwork #Записываем кого выбрал медик
                        bot.send_message(chatId, "Доктор вышел на дежурство!")
            #Удаляем кнопку 
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
         if call.data[:8] == 'блудница': #блудница сделал выбор
            #Проверяем гуляла шлюха или нет
            for dia in range(len(UserMas)):
               if UserMas[dia][3]=="блудница" and UserMas[dia][6]==0:
                  UserMas[dia][6]=1
                  print('блудница выбрала: '+str(call.data[8:]))
                  #Если такой игрок есть то спим с ним
                  for mb in range(len(UserMas)):
                     if UserMas[mb][0]==call.data[8:]:
                        bludwork=call.data[8:]
                        bot.send_message(chatId, "Блудница пошла шалить")
            #Удаляем кнопку 
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
         if call.data == 'убить': #мент сделал выбор
            #Проверяем выходил мент или нет
            for dia in range(len(UserMas)):
               if UserMas[dia][3]=="ментяра":
                  if UserMas[dia][6]==0:
                     UserMas[dia][6]=1
                     print('Мент выбрал убить')
                     bot.send_message(chatId, "Ментяра зарядил свой кольт и готов выстрелить")
                     #Удаляем кнопку 
                     bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
                     #Создаем кнопки под сообщением со списком игроков
                     markupmentkill = types.InlineKeyboardMarkup(row_width=1)
                     #Перебираем массив и выводим игроков в кнопках
                     for kk in range(len(UserMas)):
                        if UserMas[kk][3]!="ментяра":
                           if UserMas[kk][3]=="лейтенант":
                              markupmentkill.add(types.InlineKeyboardButton(UserMas[kk][2], callback_data='ментярау'+UserMas[kk][0])+" - "+str(UserMas[kk][3]))
                           else:
                              markupmentkill.add(types.InlineKeyboardButton(UserMas[kk][2], callback_data='ментярау'+UserMas[kk][0]))
                        else:
                           M_id=kk
                     #Отправляе сообщение менту и прикрепляем клавиатуру
                     bot.send_message(UserMas[M_id][1], "Кого будем убивать?", reply_markup=markupmentkill)
                  else: #действие уже было выбрано, поэтому просто удаляем кнопку
                     #Удаляем кнопку 
                     bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
         if call.data == 'проверить': #мент сделал выбор
            #Проверяем выходил мент или нет
            for dia in range(len(UserMas)):
               if UserMas[dia][3]=="ментяра":
                  if UserMas[dia][6]==0:
                     UserMas[dia][6]=1
                     print('Мент выбрал проверку')
                     bot.send_message(chatId, "Ментяра пошел проверять документы")
                     #Удаляем кнопку 
                     bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
                     #Создаем кнопки под сообщением со списком игроков
                     markupmentcheck = types.InlineKeyboardMarkup(row_width=1)
                     #Перебираем массив и выводим игроков в кнопках
                     for kp in range(len(UserMas)):
                        if UserMas[kp][3]!="ментяра":
                           if UserMas[kk][3]=="лейтенант":
                              markupmentkill.add(types.InlineKeyboardButton(UserMas[kk][2], callback_data='ментярау'+UserMas[kk][0])+" - "+str(UserMas[kk][3]))
                           else:
                              markupmentkill.add(types.InlineKeyboardButton(UserMas[kk][2], callback_data='ментярау'+UserMas[kk][0]))
                        else:
                           M_id=kp
                     #Отправляе сообщение и прикрепляем клавиатуру
                     bot.send_message(UserMas[M_id][1], "Кого будем проверять?", reply_markup=markupmentcheck)
                  else: #действие уже было выбрано, поэтому просто удаляем кнопку
                     #Удаляем кнопку 
                     bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
         if call.data[:8] == 'ментярап': #ментяра сделал выбор
            #Проверяем что сделал мент
            for dia in range(len(UserMas)):
               if UserMas[dia][3]=="ментяра":
                  if UserMas[dia][6]==1:
                     UserMas[dia][6]=2
                     mentid=UserMas[dia][1]
                     print('Мент решил проверить: '+str(call.data[8:]))
                     bot.send_message(chatId, "Ментяра закончил досмотр")
                     #Если такой игрок есть то проверяем его
                     for mb in range(len(UserMas)):
                        if UserMas[mb][0]==call.data[8:]:
                           checkment=call.data[8:]
                     #Удаляем кнопку 
                     bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
                  else: #действие уже было выбрано, поэтому просто удаляем кнопку
                     #Удаляем кнопку 
                     bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
         if call.data[:8] == 'ментярау': #ментяра сделал выбор
            #Проверяем что сделал мент
            for dia in range(len(UserMas)):
               if UserMas[dia][3]=="ментяра":
                  if UserMas[dia][6]==1:
                     UserMas[dia][6]=2
                     mentid=UserMas[dia][1]
                     print('Мент решил убить: '+str(call.data[8:]))
                     bot.send_message(chatId, "Ментяра открыл огонь")
                     #Перебираем массив и убиваем игрока
                     for kme in range(len(UserMas)):
                        if UserMas[kme][0]==call.data[8:]:
                           MentKill=UserMas[kme][0]
                     #Удаляем кнопку 
                     bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
                  else: #действие уже было выбрано, поэтому просто удаляем кнопку
                     #Удаляем кнопку 
                     bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
         if call.data[:6] == 'вешаем': #Житель сделал выбор
            NameCill=" "
            if call.from_user.last_name==None:
               NameCill=call.from_user.first_name#Добавляем имя игрока, если фамилии нет
            else:
               NameCill=call.from_user.last_name#Добавляем фамилию игрока
            #Проверяем вешал ли уже кого то житель
            for dia in range(len(UserMas)):
               if UserMas[dia][2]==NameCill:
                  if UserMas[dia][6]==0:
                     print('+ 1 голос против: '+str(call.data[6:]))
                     #Если такой игрок есть то вешаем его
                     for mdv in range(len(UserMas)):
                        if UserMas[mdv][0]==call.data[6:]:
                           UserMas[mdv][5]+=1
                           UserMas[dia][6]=1
                           bot.send_message(chatId, str(NameCill)+" решил повесить "+str(UserMas[mdv][2]))
                     #Удаляем кнопку 
                     bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
                  else: #действие уже было выбрано, поэтому просто удаляем кнопку
                     #Удаляем кнопку 
                     bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
         if call.data == 'TestUser': #Житель решил проверить себя
            bot.send_message(call.message.chat.id, "Ваш ник: "+str(call.from_user.username)+"\nВаш id: "+str(call.from_user.id)+"\nВаша фамилия: "+str(call.from_user.last_name))
            if call.from_user.last_name==None:
               bot.send_message(call.message.chat.id, "Заполните ваш профиль фамилией")
            #Удаляем кнопку 
            bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
         if call.data == 'res': #Начать новую игру
            print('Перезапускаем игру')
            chatId=0
            chatId=call.message.chat.id
            mafia_don_list="Список мафии:\n"
            mir_list="Список мирных жителей:\n"
            name='Список игроков:\n'
            counter=0
            UserMas.clear()
            Killmas.clear()
            #Отправляем стикер
            bot.send_sticker(chatId, 'CAACAgIAAxkBAAIQC15-Zuo8YhfYe0MnBlkdXqT63MM6AAJBAANSiZEj1dZXStNkcVYYBA')
            #Создаем кнопки под сообщением
            markup3 = types.InlineKeyboardMarkup(row_width=1)
            item1 = types.InlineKeyboardButton("Зарегистрироваться!", callback_data='registration')
            markup3.add(item1)
            #Отправляе сообщение и прикрепляем клавиатуру
            bot.send_message(chatId, "Ну что, кто готов играть?".format(call.message.from_user), reply_markup=markup3)
   except Exception as e:
      print(repr(e))
#RUN
bot.polling(none_stop=True)
