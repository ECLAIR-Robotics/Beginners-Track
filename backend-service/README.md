# Backend Design

## Overview

We are using Python and Flask for the backend. The backend is responsible for handling the requests from the frontend and communicating with the database. We will design a RESTful API on the backend. You can check out [this link](https://aws.amazon.com/what-is/restful-api/) for what a RESTful API is. Don't worry if it doesn't make too much sense right now! We will start small with making a simple API and then build on top of it. 

* File Structure
    - **Embedded**: Code for controlling the GPIO Pins in a Raspberry Pi
    - **Core**: These are the core files for the backend. This is where the API will be defined and the database will be accessed.
        1. **Views**: This is where you create different API endpoints that your frontend will call to get data from the backend.
        2.  \__**init__.py**: This is where you initialize the Flask app and the database. Basically whenever you import a folder in python
        it will look for a file called \__init__.py and run the code in there.

    - base: This is the file we run and it runs everything else. It is the entry point for the backend. Whenever you a .py file there is a variable called \__name__ that is set to the name of the file. When you run a file, the \__name__ variable is set to \__main__. So we check if the \__name__ variable is set to \__main__ and if it is, we run the app. This is so that when we import the base folder in another file, the app doesn't run.

* REST API
    - RESTful API is a way to communicate with the backend. It is a set of rules that define how the frontend and backend will communicate. The frontend will send a request to the backend and the backend will send a response back. The request will have a method (GET, POST, PUT, DELETE) and a URL. The URL will be the endpoint that the frontend wants to access. The backend will then send a response back to the frontend. The response will have a status code and a body. The status code will tell the frontend if the request was successful or not. The body will contain the data that the frontend requested.

    - TLDR: It is like defining functions in the backend that the frontend can call to get data from the backend. REST is the rules **we** define for how the frontend and backend will communicate. We base it on a widely accepted convention that is used by most companies.

** Note: We will be using Postman to test our API. Postman is a tool that allows us to send requests to our API and see the response. You can download it [here](https://www.postman.com/downloads/). **

## Setup

### Windows (no WSL)

1. After you have installed python 
2. Create a virtual environment in the folder
    - `python -m venv venv`
3. Activate the virtual environment
    - `cd venv/Scripts`
    - `activate`
    - `cd ../..`. 
4. Install the dependencies
    - `pip install -r requirements.txt`
5. Run the backend
    - `python -m base`


### WSL or MacOS or Linux
_if some of these commands don't work for you and you are on MacOS try changing pip to pip3 and python to python3_

1. Create a virtual environment in the folder
    - `conda create -n beginners-track`
2. Activate the virtual environment
    - `conda activate beginners-track`
    - `conda install pip`
3. Install the dependencies
    - `pip install -r requirements.txt`
4. Run the backend
    - `make run` (for Linux and WSL)
    - `make mac` (for MacOS)

