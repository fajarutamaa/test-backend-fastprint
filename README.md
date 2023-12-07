[![License](https://img.shields.io/badge/License-BSD_2--Clause-orange.svg)](https://github.com/fajarutamaa/test-backend-fastprint/blob/main/LICENSE)

## test-backend-fastprint

## Installation Guide

Clone the project from GitHub repository:

      git clone https://github.com/fajarutamaa/test-backend-fastprint.git

Change Directory:

      cd test-backend-fastprint

## Project Setup

To set up and run this project, ensure that Python is installed on your computer. It is recommended to create a virtual environment to manage project dependencies separately. You can install `virtualenv` using the following command:

```
pip install virtualenv
```

Clone or download this repository and open it in your preferred code editor. In the terminal (mac/linux) or Windows terminal, execute the following command in the project's base directory:

```
virtualenv venv
```

This will create a new `venv` folder in your project directory. Activate the virtual environment with the following command on mac/linux:

```
source venv/Scripts/active
```

Next, install the project dependencies:

```
pip install -r requirements.txt
```

You can now run the project using the following command:

```
python manage.py runserver
```

**Note:** Create an `.env` file in your project root folder and add your variables. See `.env.example` for assistance.


## License

This project is available for use under the BSD 2-Clause License.


