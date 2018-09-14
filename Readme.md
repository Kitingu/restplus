[![Build Status](https://travis-ci.org/Kitingu/restplus.svg?branch=develop)](https://travis-ci.org/Kitingu/restplus)
[![Coverage Status](https://coveralls.io/repos/github/Kitingu/restplus/badge.svg?branch=develop)](https://coveralls.io/github/Kitingu/restplus?branch=develop)
[![Maintainability](https://api.codeclimate.com/v1/badges/decc4fdf78c5ca700f8c/maintainability)](https://codeclimate.com/github/Kitingu/restplus/maintainability)
![GitHub](https://img.shields.io/github/license/mashape/apistatus.svg)

 Ride-my App is a carpooling application that provides drivers with the ability to create ride oﬀers and passengers to join the available ride oﬀers.
***
![Home Image](https://raw.github.com/kitingu/restplus/main_pic.png)
## Getting Started
1. Clone the repository to your machine;
    *https://github.com/Kitingu/Restplus.git
2. Open the repo with an IDE of your choice as a project.
## Prerequisites
* Python 3
* Virtual environment.
* Flask
* flask rest-plus
* Postman
* Browser of your choice
## Setup
1 Open cmd. In the root directory folder;
* Run the command: virtualenv venv -p python3.6,  to create a virtual <br/>
 environment with the name venv. Folder with the name venv will <br>
 created.
 windows
* Activate the virtual environment by moving to the Script directory i.e. cd venv\Scripts, and running <br>
activate
linux and mac
Activate the virtual environment by running the command: source /venv/bin/activate
## Application Requirements
* The application requirements are clearly listed in the ***requirents.txt*** document.
   * To install them run the following cmd command:
     * pip install -r requirements.txt
## End-Points
|Requests     |   EndPoint                          | Functionality
|:-----------:|:-----------------------------------:|:--------------:
   GET        |  api/v1/rides                       | Get all Rides
   GET        |  api/vi/rides/{ride_id}             | Get a specific ride
   DELETE     |  api/v1/rides/{ride_id}             | Delete ride
   POST       |  api/v1//rides                      | Add a ride
   POST       |  api/v1/rides/{ride_id}/requests    | Request to join a ride
   PUT        |  api/v1/rides/{ride_id}             | Edit ride details
   POST       |  api/v1/users                       | Register users
   POST       |  api/v1/users                       | Get all users
   DELETE     |  api/v1/users/{username}            | Delete a user
* The above endpoints can be tested by Postman.

## Running Of Tests
* Running of tests can be done by using pytest and unittest.
    run


## Version Control
* GitHub

## Github link
* https://github.com/Kitingu/Restplus/tree/develop

## Heroku
https://ride-my-way1.herokuapp.com/

## Author
* Benedict Kiting'u

## License
* This project is licensed under the MIT License



