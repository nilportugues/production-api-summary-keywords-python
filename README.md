FOR PYTHON 2.7

# 1. Installation and running
 
## 1.1. Development

Meet the requirements for this project: 

```bash
sudo apt-get install -y python python-pip python-virtualenv \
    cython libblas-dev liblapack-dev gfortran python-numpy python-scipy \
    python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose
```

Run the following script to get you started in no time:

```bash
chmod +x dev.sh
./dev.sh
```
This will start the Flask framework listening on `127.0.0.1:8080` .

## 1.2. Production

Use the docker container

### 1.2.1 - Infrastructure Setup
In order to make it run, we will need to configure nginx and uwsgi and generate the package for the flask application. 

```
nginx (port 80 or 443) 
    --> uwsgi (port 8080) 
        --> your flask application
```

### 1.2.2 - Creating the build

In order to create a build that we can use anywhere, we need to generate a tarball using `easy_install`'s proxy file `setup.py`. 

```sh
# Git clone the project
git clone <git repo>.git example
 
# Generate release tarball
cd example/
python setup.py sdist

# save somewhere the build at: 
./example/dist/flask_app_example-0.1.tar.gz
```

Move the resulting tarball to the project's root directory and modify the docker-compose path.

Finally use the docker container.
 
 
# 2. API 

- **API Responses**: Uses `hal+json` standards.
- **API Error Responses**: Uses `vnd+error` error response standard.
- **Documentation**: Uses Swagger (OpenAPI)

## 2.1 Documentation: 

 - **Swagger UI**: http://127.0.0.1:8080/api/
 - **Swagger.json**: http://127.0.0.1:8080/api/swagger.json
 
## 2.2 Methods

 - [GET] http://127.0.0.1:8080/api/text/languages
 - [POST] http://127.0.0.1:8080/api/text/detect
 - [POST] http://127.0.0.1:8080/api/text/translate
 
# 3. Framework:

API has been written in Python (2.7) and uses the Flask-RESTful framework.
 
