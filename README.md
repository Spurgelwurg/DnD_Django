# DnD_Django
Django Project of a DnD Manager App

# Installation
1. Installiere die benötigten Pakete:
   ```pip install -r requirements.txt```

2. Für das Laden von Testaten für Klassen und Rassen um Charaktere zu erstellen:
    ```python manage.py populate_data```

3. Erstelle und migriere die Datenbank:
   ```python manage.py makemigrations ```  

   ```python manage.py migrate```

4. Führe den Entwicklungsserver aus:
   ```python manage.py runserver```

5. Öffne deinen Browser und navigiere zu `http://127.0.0.1:8000/` zum Anmelden.

6. Nach der Anmeldung kannst du deine Charaktere erstellen, Kampagnen verwalten und den integrierten Würfelroller verwenden.

## Kurzanleitung zur Benutzung
Wenn man die Anwendung testen möchte:
- Einen Charakter erstellen und diesem Werte zuteilen.
- Eine Kampagne erstellen und Charaktere hinzufügen.
- Den Code für die Kampagne kopieren und an die Spieler senden.
- (Zu Simulationszwecken) Weitere Spieler anlegen und der Kampagne beitreten.


