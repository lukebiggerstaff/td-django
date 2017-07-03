Provisioning a new site
=======================

## Required packages:

* nginx
* Python 3.5
* virtualenv + pip
* Git

## Nginx Virtual Host config

* see nginx.template.conf
* replace SITENAME with, e.g., staging.my-domain.com

## Systemd service

* see gunicorn-systemd.template.service
* replace SITENAME with, e.g., staging.m-domain.com


## Folder structure:
Assume w have a user account at /home/username

/home/username
|__ sites
    |__ SITENAME
	 |--- database
	 |--- source
	 |--- static
	 |___ virtualenv
