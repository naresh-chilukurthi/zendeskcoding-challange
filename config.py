# Error codes
INVALID_TICKET_ID = "invalid ticket ID.ticket id must be an integer"

# Zendesk account url
ACCOUNT_URL = "https://zendeskcodingchallenge7438.zendesk.com/"

# PAGINATION SIZE
PAGE_SIZE = 25
# URLs
TICKET_BY_ID_URL = f"{ACCOUNT_URL}api/v2/tickets/"
TICKET_COUNT_URL = f"{ACCOUNT_URL}api/v2/tickets/count"
TICKET_BY_ID_PAGE = f"{ACCOUNT_URL}api/v2/tickets.json?page="
TICKETS_BY_PAGINATION = f"{ACCOUNT_URL}api/v2/tickets.json?page[size]={PAGE_SIZE}"
# Auth token
USERNAME = 'youruseranem'
TOKEN = "yourtoken"
USER = f'{USERNAME}/token'
