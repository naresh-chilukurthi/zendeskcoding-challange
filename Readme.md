**Zendesk Ticket Viewer**

This is a simple cli tool to query tickets listed in Zendesk 
This tool lists all tickets available and also display content of a specific ticket

Minimum Version of python required to run this tool is Python 3.6


All the configuration data is present in config.py
Ideally auth related data should be stored in secrets and accessed from there

Here for the case of simplicity AUTH data is given in config.py.
USERNAME,TOKEN,ZENDESK_TICKETS_BASE_URL should be changed before executing

All input options are self-explanatory while running

_Instructions to run this program_

Make sure the packages listed ins requirements.txt is installed

`python3 TicketLister.py`



