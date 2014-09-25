Tiny Multiplayer Bot
====================

Tiny Multiplayer Bot (TMB) is a service for Civilization V hotseat save sharing.
Groups of players can setup games and use this site to upload and download
saves to continue their games instead of actually needing to sit at the same
computer.


Requirements
------------

* pip install -r requirements.txt
* Log-in to Steam and go to http://steamcommunity.com/dev/apikey
 * Replace "YOUR KEY HERE" in tmb/views.py with the key you receive
 * This will be a config option soon!

Running a Server
----------------

* If this is your first run, you need to setup a database with

    python manage.py initdb

* Then run:

    python manage.py runserver

 * -h <host name> -p <port> are options for runserver
