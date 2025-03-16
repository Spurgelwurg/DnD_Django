# DnD_Django
Django Project of a DnD Manager App

# Installation
1. (Optional) Erstelle ein virtuelles Python-Umgebung:
   ```python -m venv .venv```

2. (Optional) activate the virtual environment:
   ```.\.venv\Scripts\activate```

3. Installiere die benötigten Pakete:
   ```pip install -r requirements.txt```

4. Erstelle und migriere die Datenbank:
   ```python manage.py makemigrations ```  
   ```python manage.py migrate```

5. Für das Laden von Testaten für Klassen und Rassen um Charaktere zu erstellen:
    ```python manage.py populate_data```

6. Führe den Entwicklungsserver aus:
   ```python manage.py runserver```

7. Öffne deinen Browser und navigiere zu `http://127.0.0.1:8000/` zum Anmelden.

8. Einen neuen Account erstellen.

8. Nach der Anmeldung kannst du deine Charaktere erstellen, Kampagnen verwalten und den integrierten Würfelroller verwenden.

## Kurzanleitung zur Benutzung
Wenn man die Anwendung testen möchte:
- Einen neuen Account erstellen
- Einen Charakter erstellen und diesem Werte zuteilen.
- Eine Kampagne erstellen und Charaktere hinzufügen.
- Den Code für die Kampagne kopieren und an die Spieler senden.
- (Zu Simulationszwecken) Weitere Spieler anlegen und der Kampagne beitreten.

Weiter infos zu den Funktionen der Anwendung und wie DnD gespielt wird sind in der Dokumentation zu finden.

