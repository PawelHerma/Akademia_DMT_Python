ifLeap = False
m31 = [1,3,5,7,8,10,12]

def checkDate(data):
    if(data[2] == "-" and data[5] == "-" and len(data) == 10):
        print("dobre formatowanie")

        day = int(data[0] + data[1])
        month = int(data[3] + data[4])
        year = int(data[6] + data[7] + data[8] + data[9])

        if day < 1 or day > 31:
            print("zly dzien")
            exit()

        if month < 1 or month > 12:
            print("zly miesiac")
            exit()

        if year % 400 == 0 or ( year % 100 == 0 and year % 4 == 0 ):
            ifLeap = True
            if month == 2 and day > 30:
                print("Zla data")
                exit()
        
        if(month in m31 and day > 31):
            print("Zla data")
            exit()
        
        if month not in m31 and day > 30:
            print("Zla data")
            exit()

        print("Prawidlowa data")

    else:
        print("Nieprawidlowe formatowanie")
        exit()


data = input("Podaj date w formacie dd-mm-rrrr: ")
checkDate(data)
