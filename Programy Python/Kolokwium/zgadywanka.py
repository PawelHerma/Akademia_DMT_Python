# Program prosi użytkownika o podanie dowolnej liczby naturalnej. 
# Jeżeli użytkownik poda złą liczbę, to wyświetla się komunikat “Haha, nie zgadłeś” 
# oraz kolejny raz wyświetla się prośba o podanie dowolnej liczby naturalnej.
# Program kończy się w momencie gdy użytkownik poda liczbę: 2022, 
# wówczas wyświetla się komunikat “Zgadłeś moją liczbę, dziękuję za zabawę”.

def zgadnij():
    liczba = int(input("Podaj dowolną liczbę naturalną: "))
    if liczba == 2022:
        print("Zgadłeś moją liczbę, dziękuję za zabawę")
        exit()
    else:
        print("Haha, nie zgadłeś")
        zgadnij()

zgadnij()