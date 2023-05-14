# zadanie - web-scrapping

Bazując na szablonie `zadanie_szablon.py` napisz kod, który wydobędzie ze strony 'https://www.python.org/downloads/' dane na temat aktywnych wersji Pythona. Jako rezultat powinniśmy dostać listę słowników. Każdy słownik powininen zawierać:
- wersję pythona
- datę końca wsparcia
- link to dokumentu PEP

## Poprawny wynik (na bazie pliku "downloads.html"):
```
[{'pep': 'https://www.python.org/dev/peps/pep-0664',
  'release_end': '2027-10',
  'version': '3.11'},
 {'pep': 'https://www.python.org/dev/peps/pep-0619',
  'release_end': '2026-10',
  'version': '3.10'},
 {'pep': 'https://www.python.org/dev/peps/pep-0596',
  'release_end': '2025-10',
  'version': '3.9'},
 {'pep': 'https://www.python.org/dev/peps/pep-0569',
  'release_end': '2024-10',
  'version': '3.8'},
 {'pep': 'https://www.python.org/dev/peps/pep-0537',
  'release_end': '2023-06-27',
  'version': '3.7'}]
```
