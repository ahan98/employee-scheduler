# Employee Scheduler
Scheduler that assigns employees to shifts subject to custom constraints

## Getting started

### Dependencies

Ensure that you're using python3 and have pip installed. If you have everything ready, skip this until **Django Setup** section

### Python Setup
Since there are many programs that depend on python2 and be default, Mac OSX uses python2, we will use pyenv to ensure that we use python3, python2 will stop being maintained in January 2020 :o.

#### Pyenv
Pyenv is a tool to manage several python environments such that you will still have access to python2 or python3 depending on what your choose. If you don't have homebrew run:

```/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"```

Then, to get pyenv, ensure that you have homebrew and install

```brew install pyenv```

Then, to get python 3.7.3, 

```pyenv install 3.7.3```

Set your global python environment to 3.7.3:

```pyenv global 3.7.3```

If you run:
```pyenv version```

You should be able to see 3.7.3 (set by /Users/your_name/.pyenv/version)

Then change the settings on your terminal by running:

```$ echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.zshrc```

restart your terminal and verify your default version of python is correct. 

```python --version``` should give you 3.7.3

### Django Setup

After you have setup python, your must install Django 2.2.7 using pip. 

```pip install Django==2.2.7```

Verify that you have installed django by running: 

```python -m django --version```

Finally, if you have cloned this repo, you will have a directory that holds Tunnel City Coffee's Scheduler (tcc_scheduler), change into that directory and run:

```python manage.py runserver```

to launch the server.

After running the server for the first time you may need to migrate the changes made.

```python manage.py migrate```

This should get you up and running with the application.