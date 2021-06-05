# Webchat Projekt Skryptowy

Serwis webowy w formie chatu internetowego do, którego można się zarejestrować i rozmawiać z innymi użytkownikami serwisu. Aplikacja operuje na pokojach do których można dołączyć lub tworzyć własne i rozmawiać w kilka osób. W serwisie będzie można zmienić swoje zdjęcie, nick, email oraz hasło. 

Technologie wykorzystane do projektu:
- Backend: Python, Django, Sqlite
- Frontend: HTML, CSS, Bootstrap, JavaScript

# I Raport 26.03.2021
Na obecną chwilę zaimplementowałem bazę danych i system użytkowników. W systemie użytkowników działa już logowanie, wylogowywanie, zmiana hasła, resetowanie hasła (jeśli się je zapomniało po przez email z linkiem do strony gdzie można nadać nowe hasło) oraz rejestracja w serwisie.

Logowanie:  
![](img_project/img1.png)

Rejestracja:  
![](img_project/img5.png)

Zmiana hasła:  
![](img_project/img6.png)

Wylogowywanie:  
![](img_project/img7.png)

Reset zapomnianego hasła:  
![](img_project/img2.png)  
![](img_project/img4.png)
![](img_project/img3.png)

# II Raport 09.04.2021
Na obecny moment rozszerzyłem system użytkowników o przypisywanie domyślnego zdjęcia po utworzeniu konta oraz możliwość zmiany zdjęcia na własne. Użytkownik posiada również teraz możliwość zmiany: nazwy użytkownika, maila oraz hasła.

Profil:  
![](img_project/img8.png)

# III Raport 23.04.2021
W obecnej aktualizacji zaimplementowałem wygląd przez CSS i Bootstrapa. W przyszłości wygląd strony może się jeszcze zmienić po zaimplementowaniu systemu chatowania.

Wygląd:  
![](img_project/img9.png)

# IV Raport 21.05.21
![](img_project/chat.gif)

# Do Zrobienia
- system chatowania (tworzenie i dołączanie do chatów, rozmowy)
- dodanie automatycznego dodawania nowych wiadomości bez odświeżania strony
