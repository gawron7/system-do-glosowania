# Online Voting System

## Wymagania

- Python 3.6+
- Virtualenv (opcjonalnie)

## Instalacja

1. Sklonuj repozytorium:
    ```
    git clone https://github.com/gawron7/system-do-glosowania.git
    ```
2. Przejdź do katalogu projektu:
    ```
    cd online-voting-system
    ```
3. Stwórz i aktywuj wirtualne środowisko (opcjonalnie):
    ```
    python -m venv venv
    source venv/bin/activate  # Na Windows: venv\Scripts\activate
    ```
4. Zainstaluj wymagane biblioteki:
    ```
    pip install -r requirements.txt
    ```
5. Utwórz bazę danych:
    ```
    flask shell
    >>> from app import db
    >>> db.create_all()
    >>> exit()
    ```
6. Uruchom aplikację:
    ```
    flask run
    ```

## Użycie

- Otwórz przeglądarkę i przejdź do `http://127.0.0.1:5000/`, aby zobaczyć działającą aplikację.
