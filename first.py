username = input('Enter your username: ')
userAge = int(input('Enter your age: ')) # Example: 25

firstChildAge = int(input(username+", zəhmət olmasa ilk övladınızın yaşını qeyd edin: ")) # Example: 6
secondChildAge = int(input(username+", zəhmət olmasa ikinci övladınızın yaşını qeyd edin: ")) # Example: 5

difference = int((userAge + firstChildAge + secondChildAge) / 3)

print(username+' adlı istifadəçinin övladlarının yaş ortalaması ilə '+username+' adlı istifadəçinin yaş ortalaması '+str(difference)+'-dir')