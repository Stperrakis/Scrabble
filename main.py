import mylib24262401 as m


# --------------------------main -----------------------------


def menu():
    print('1. ΣΚΟΡ')
    print('2. ΔΥΣΚΟΛΙΑ')
    print('3. ΠΑΙΧΝΙΔΙ')
    print('q. ΕΞΟΔΟΣ')


print('******* SCRABLE *******')
print('-----------------------')
while True:
    menu()
    answer = input('Επέλεξε μια ενέργεια... \n')
    if answer in (['q', '1', '2', '3']):
        break
    else:
        print('Λάθος είσοδο! Παρακαλώ εισάγετε νέα.')

if answer == '1':
    try:
        with open('history.txt', 'r+', encoding="utf8") as his:
            for c, names in enumerate(his, 0):
                print(c, names)
    except FileNotFoundError:
        print('File not found...')
        print('ΑΝΤΕ ΓΕΙΑ')


elif answer == '2':
    hard = -1
    print('1. ΜΙΚΡΗ') # MinLetters Method (default)
    print('2. ΜΕΣΑΙΑ') #MaxLetters Method
    print('3. ΜΕΓΑΛΗ') #MaxLetters and MaxPoints Method
    while (int(hard) < 0 or int(hard) > 3):
        hard = input('\nΠληκτρολογείτε μια απο τις παραπανω επιλογες:')

    newgame = m.GamePlay(int(hard))

elif answer == '3':
    newgame = m.GamePlay(1) #default gameplay with method Min letters
else:
    print('ΑΝΤΕ ΓΕΙΑ!')
