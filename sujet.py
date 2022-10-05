import random
import os
name = input("как зовут вашего героя? ")
if not name: name = "Ленивый герой"
way_1   = True
way_2   = True
way_3   = True
key = ""
game = True
scene = "0"
while game:
 os.system("cls")
 if (way_1 or way_2 or way_3) and key == "":
 	os.system("cls")
 	key = ""
 	print(f"подходите {name} к трем дорожкам, а на перекрестке лежит камень... " )
 	if way_1:
 		print("1-убитым будеш")
 	if way_2:
 		print("2-женатым будеш")
 	if way_3:
 		print("3-богатым будеш")
 	user_choise = input("напиши свой выбор и нажмт ENTER ")
 	key += user_choise

 if way_1 and key == "1":
 	print("дорога 1.на пути 5 разбойников-сдавайся {name} ")
 	print("1-биться")
 	print("2-сдаться")
 	user_choise = input("напиши свой выбор и нажмт ENTER ")
 	if user_choise == "1" or user_choise == "2":
 	  key += user_choise

 if way_1 and key == "11":
 	os.system("cls")
   print("начало битвы")
   if play == 1:
      xvo = True
      while xvo:
       xpyou = 100
       xpfiende = 70
       xpboss = 150
       udar = input("к вам подбежал разбойник, 1-ударить слабо 2-попытаться ударить сильно")
       if udar == 1:
         xpfiende -= 10

       if udar == 2:
         urad = random.randint(1, 2)
         if urad == 2:
            xpfiende - 45
      
       xpyou -= random.randint(10, 20)
       print(xpyou)
       print(xpfiende)

       if xpfiende <= 0:
         udar = input("к вам подбежал главарь разбойников, 1-ударить слабо 2-попытаться ударить сильно")
       if udar == 1:
         xpfiende -= 10

       if udar == 2:
         urad = random.randint(1, 2)
         if urad == 2:
            xpboss -= 45
      
       xpyou -= random.randint(10, 20)
       print(xpyou)
       print(xpboss)
      if xpyou <= 0:
         game = False
      if xpfiende <= 0 and xpboss <= 0:
         input("вы победили разбойников ENTER ")
         pass

   if play == 2:
      input("вас убили... ENTER")
      game = False
 	key = ""
 	way_1 = False
 	input("pause")

 if way_1 and key == "12":
 	print("вас ограбили и убили...")
 	game = False
 	input("pause")

 if way_2 and key == "2":
   print("дорога 2. на дороге красивая девушка и просит вас помощи.")
 	print("1-отказаться")
 	print("2-помочь")
 	user_choise = input("напиши свой выбор и нажмт ENTER ")
 	if user_choise == "1" or user_choise == "2":
 	  key += user_choise

 if way_2 and key == "21":
    print("девушка напала на вас но вы успели пронзить ее своим мечем")
    key = ""
    way_2 = False
    input("pause")

 if way_2 and key == "22":
    print("как только она оказалась за вашей спиной, она вaс убила...")
    game = False
    input("pause")
	
 if way_3 and key == "3":
 	print("дорога 3. на дороге лежит сундук с золотом.")
 	print("1-раздать бедным")
 	print("2-забрать себе")
 	user_choise = input("напиши свой выбор и нажмт ENTER ")
 	if user_choise == "1" or user_choise == "2":
 	  key += user_choise

 if way_3 and key == "31":
    print("вас будут помнить")
    key = ""
    way_3 = False
    input("pause")

 if way_3 and key == "32":
    print("сундук оказался таким тяжелым что проходя по рыхлой земле вы застряли и не смогли выбраться...")
    game = False
    input("pause")

 if way_1 == way_2 == way_3 == False:
 	game = False	

input("конец")


























