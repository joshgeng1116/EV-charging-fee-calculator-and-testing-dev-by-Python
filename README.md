# FIT2107_S2_2021 Team NullPointerException
Jeremy Chrimes, Jinyun Geng & Lantao Yang

## Setting up and running the project via the terminal

### Enabling virtualenv
To use virtualenv, you will need to have pip, the Python package installer, already installed on your machine (by default, it should also be installed when you install Python).

1. Windows
    ```
    python3 -m venv env
    .\env\Scripts\activate
    ```

2. Linux/macOS
    ```
    python3 -m venv env
    source env/bin/activate
    ```

    If you are unable to get virtualenv to run, you might need to run the following command first:
    ```
    sudo apt install python3-venv
    ```

### Installing Required Dependencies/Packages
You will need to install project dependencies for the provided code to work. This only needs to be done once.

```
pip install -r requirements.txt
```
### Start application
To start the application you can simply just run main.py inside the virtual environment
```
python main.py
```

### Exiting Virtualenv
Once you are finished working on the project, you can exit virtualenv by running the following command:

```
deactivate
```