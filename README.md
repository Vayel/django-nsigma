# django-nsigma-members

Une application Django pour gérer les inscriptions à Nsigma.

## Installation

**Attention :** le projet n'est pas configuré pour la production. Se référer à
[cette page](https://docs.djangoproject.com/en/1.10/howto/deployment/) et notamment
à la [checklist](https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/).

```
git clone https://github.com/Vayel/django-nsigma-members
cd django-nsigma-members
# Facultatif (mais conseillé) : travailler dans un environnement virtuel Python
# Ex : http://sametmax.com/mieux-que-python-virtualenvwrapper-pew/
pip install -r requirements.txt
./manage.py makemigrations members
./manage.py migrate
./manage.py createsuperuser
./manage.py runserver
```
