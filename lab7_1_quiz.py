# System Inteligentnego Domu

# Inteligentne Oświetlenie (SmartLight)
# Klasa SmartLight reprezentuje inteligentne żarówki, których jasność można regulować. Jasność jest ograniczona zakresem od 0 do 100. Użyj dekoratorów @property i @setter do kontroli poziomu jasności.

# System Audio (AudioSystem i SmartSpeaker)
# AudioSystem: Klasa bazowa z atrybutami brand i max_volume.
# SmartSpeaker: Klasa pochodna od AudioSystem (ma dziedziczyć z AudioSystem) , dodająca atrybut voice_command_enabled. Zdefiniuj metody get_details w obu klasach, aby zwracały informacje o systemie audio i inteligentnym głośniku (w formie słownika)(tak jak w testach).

# Robot Sprzątający (CleaningRobot)
# Klasa CleaningRobot z atrybutami model i battery_life. Zaimplementuj metodę magiczną setattr, aby zarządzać atrybutami klasy, upewniając się, że battery_life jest liczbą całkowitą. Dodatkowo, zaimplementuj metodę magiczną str, aby zwracała czytelną reprezentację robota sprzątającego.

# Twoje rozwiązanie:
# Tutaj tworzone są klasy SmartLight, AudioSystem, SmartSpeaker i CleaningRobot.
# Wszystkie te klasy powinny być zaimplementowane zgodnie z opisem w zadaniu.
