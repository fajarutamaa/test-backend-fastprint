[![License](https://img.shields.io/badge/License-BSD_2--Clause-orange.svg)](https://github.com/fajarutamaa/test-backend-fastprint/blob/main/LICENSE)

## Introduction

This project implements a product recap flow using Django and the Django REST framework. Its primary objectives are product input, product editing, and product recapitulation. The project utilizes various Python packages to facilitate efficient development and functionality. For logging and monitoring, Sentry.io provides support for this project.

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

## Basic Usage

This project running on base url `http://127.0.0.1:8000` with api endpoints as follows:

| Methods | URLs                                | Actions                                   |
| ------- | ----------------------------------- | ----------------------------------------- |
| GET     | /admin/                             | login as admin (super user)               |
| GET     | /                                   | Get all product with status 'siap dijual' |
| GET     | /api/v1/products/                   | Get all products                          |
| POST    | /api/v1/products/post/              | Create a product                          |
| POST    | /api/v1/products/update/:id_produk/ | Update a product                          |
| DELETE  | /api/v1/products/:id_produk/        | Delete a product                          |

## License

This project is available for use under the BSD 2-Clause License.
