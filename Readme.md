# Human Resource Management App

## (A Project for Human Resource Management of A Company)

Here is a project for human resource management of a company.  
Back-End of this project is written in microservice architecture and uses python FastAPI framework, sqlalchemy and sqlite for database,
and has token-base authentication using different python libraries.
Front-End of the project uses ReactJs and bootstrap5.
To use it and test it follow these instructions:
<br><br>


## Setup and start the back-end

### 1. Download project
Download the project into your device or simply clone the project into your virtual environment or any directory
you want by running the
command :

```commandline
git clone https://github.com/HB2102/human_resorce_managment
```

### 2. Install requirements

First you should install the requirements of the project, for that, go to the project directory and run the command :

```commandline
pip install -r Backend/requirements/requirements.txt
```

and wait for pip to install packages.

### 3. Run the project

For running the project, go to its directory of project and run the command :

```commandline
uvicorn Backend.main:app --reload
```

if you get the error that the port is in use you can change the port by running the command like :

```commandline
uvicorn main:app --reload --port 5000
```

and it'll change the port to 5000 but running it on port 8000 should be fine at the beginning.  
When the project is running you can go to the URL that it shows tou on your browser and see the first page.

### 4. See the APIs list

To see the list of APIs just add /docs at the end of the URL. It should look something like this :

```Url
http://127.0.0.1:8000/docs
```

you can see the list of all the APIs and you can test them if you want. project has different functionalities, you can
add employees, promote them to admin, manage their arrival and departure time, make teams with employees and manage them and ...

database already has one default admin with default values of :

- Username : admin
- Password : admin

<br><br><br>
Thanks for your time.