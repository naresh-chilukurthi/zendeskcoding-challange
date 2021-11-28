# Error codes
INVALID_TICKET_ID = "invalid ticket ID.ticket id must be an integer"

# Zendesk account url
ZENDESK_TICKETS_BASE_URL = "https://zendeskcodingchallenge7438.zendesk.com/"
# Auth token
USERNAME = 'youruseranem'
TOKEN = "yourtoken"
USER = f'{USERNAME}/token'

# PAGINATION SIZE
PAGE_SIZE = 25
# URLs
TICKET_BY_ID_URL = f"{ZENDESK_TICKETS_BASE_URL}api/v2/tickets/"
TICKETS_BY_PAGINATION = f"{ZENDESK_TICKETS_BASE_URL}api/v2/tickets?page[size]={PAGE_SIZE}"

