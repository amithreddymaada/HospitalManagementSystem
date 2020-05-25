# Hospital Management System in Django

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
1. python3 
2. pip3
3. virtualenvwrapper

Install `python3`
```bash
sudo apt-get install -y python3 
```

Install `pip3`
```bash
sudo apt-get install -y python3-pip
```

Install `virtualenvwrapper`
```bash
sudo pip3 install vitualenvwrapper
```

On your `.zshrc` or `.bashrc`
```bash
export WORKON_HOME=$HOME/.virtualenvs
export PROJECT_HOME=$HOME/projects
source /usr/local/bin/virtualenvwrapper.sh
```

```bash
source ~/.bashrc
#or
source ~/.zshrc
```

### Installing

Create a virtualenv

```bash
export PROJECT_NAME='hospital_management_system'
mkvirtualenv $PROJECT_NAME
workon $PROJECT_NAME
```

Clone the Repo

```bash
git clone https://github.com/amithreddymaada/HospitalManagementSystem.git $PROJECT_NAME
cd $PROJECT_NAME
```

Install the requirements

```bash
pip install -r requirements.txt
```


Install mysql
```bash
sudo apt-get install python3-dev libmysqlclient-dev
```






## Running the Application

```bash
python manage.py collectstatic --noinput
python manage.py makemigrations
python manage.py migrate
python manage.py runserver 0.0.0.0:8080
```



