Seoul Mate Website
---

<img src="files/seoulmate_tile_dark.png" alt="Seoul Mate"/> 


Setting up your local environment
-----

This assumes that you have python3 installed. (we are using 3.4 but this should work for most python 3 versions)

1. Clone the project by entering `git clone git@github.com:SeoulMate/seoulmate_web.git` in the terminal
    - This will create a folder called `seoulmate_web` where you ran the command

2. Create a virtualenv by creating a new folder `mkdir virtualenvironments` and going into that folder `cd virtualenvironments`

3. Create the virtual environment (mostly copied from the django girls tutorial)
    > ## Virtual environment

    > Before we install Django we will get you to install an extremely useful tool to help keep your coding environment tidy on your computer. It's possible to skip this step, but it's highly recommended. Starting with the best possible setup will save you a lot of trouble in the future!

    > So, let's create a **virtual environment** (also called a *virtualenv*). Virtualenv will isolate your Python/Django setup on a per-project basis. This means that any changes you make to one website won't affect any others you're also developing. Neat, right?

    > All you need to do is find a directory in which you want to create the `virtualenv`; your home directory, for example. On Windows it might look like `C:\Users\Name\` (where `Name` is the name of your login).

        cd seoulmate_web

    > We will make a virtualenv called `smvenv`. The general command will be in the format:

        python3 -m venv smvenv

    > ### Windows

    > To create a new `virtualenv`, you need to open the console (we told you about that a few chapters ago - remember?) and run `C:\Python34\python -m venv smvenv`. It will look like this:

        C:\Users\Name\seoulmate_web> C:\Python34\python -m venv smvenv

    > where `C:\Python34\python` is the directory in which you previously installed Python and `smvenv` is the name of your `virtualenv`. You can use any other name, but stick to lowercase and use no spaces, accents or special characters. It is also good idea to keep the name short - you'll be referencing it a lot!

    > ### Linux and OS X

    > Creating a `virtualenv` on both Linux and OS X is as simple as running `python3 -m venv smvenv`.
    It will look like this:

        ~/seoulmate_web$ python3 -m venv smvenv

    > `smvenv` is the name of your `virtualenv`. You can use any other name, but stick to lowercase and use no spaces. It is also good idea to keep the name short as you'll be referencing it a lot!

    > > __NOTE:__ Initiating the virtual environment on Ubuntu 14.04 like this currently gives the following error:

    > >     Error: Command '['/home/eddie/Slask/tmp/venv/bin/python3', '-Im', 'ensurepip', '--upgrade', '--default-pip']' returned non-zero exit status 1

    > > To get around this, use the `virtualenv` command instead.

    > >     ~/djangogirls$ sudo apt-get install python-virtualenv
    > >    ~/djangogirls$ virtualenv --python=python3.4

4. Activate the virtualenv (also copied from the djangogirls tutorial - change `djangogirls` to `seoulmate_web`)
    > ## Working with virtualenv

    > The command above will create a directory called `smvenv` (or whatever name you chose) that contains our virtual environment (basically a bunch of directory and files).

    > #### Windows

    > Start your virtual environment by running:

        C:\Users\Name\seoulmate_web> smvenv\Scripts\activate

    > #### Linux and OS X

    > Start your virtual environment by running:

        ~/seoulmate_web$ source smvenv/bin/activate

    > Remember to replace `smvenv` with your chosen `virtualenv` name!

    > > __NOTE:__ sometimes `source` might not be available. In those cases try doing this instead:

    > >    ~/djangogirls$ . smvenv/bin/activate

    > You will know that you have `virtualenv` started when you see that the prompt in your console looks like:

        (smvenv) C:\Users\Name\seoulmate_web>

    > or:

        (smvenv) ~/seoulmate_web$

    > Notice the prefix `(smvenv)` appears!

    > When working within a virtual environment, `python` will automatically refer to the correct version so you can use `python` instead of `python3`.

    > OK, we have all important dependencies in place. We can finally install Django!

5. Run `pip install -r requirements.txt` to install the pip dependencies

6. Run `python manage.py makemigrations` and then `python manage.py migrate`

7. Run `python manage.py runserver`

8. Success! (hopefully)

* If you see anything wrong here, please make an issue or a pull request!


---
