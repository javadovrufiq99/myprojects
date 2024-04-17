username = input('Enter your username: ')
age = int(input('Enter your age: '))

child1 = int(input(username+" adlı istifadəçinin 1-ci övladının yaşını qeyd edin: ")) # 6 yaş
child2 = int(input(username+" adlı istifadəçinin 2-ci övladının yaşını qeyd edin: ")) # 5 yaş

difference = int((age + child1 + child2) / 3)

print(username+' adlı istifadəçinin övladlarının yaş ortalaması ilə '+username+' adlı istifadəçinin yaş ortalaması '+str(difference)+'-dir')