# Candy Shop

## Installation

Installed virtualenv required

Linux:
```angular2
virtualenv -p python3 .venv
source .venv/bin/activate
pip install requirements.txt
```

Windows:
```angular2
virtualenv env
```
To activate virtualenv on Windows, activate script is in the Scripts folder :
```
full\path\to\env\Scripts\activate.bat
pip install -r requirements.txt
```


## Run

For the first time don't forget:
```
python manage.py makemigrations
python manage.py migrate
```

```angular2
python manage.py runserver
```

## Attention
To be able to make purchases,
the user must be registered
EXACTLY through the form on the site