import pprint
from config import *
import requests


class TickerLister:
    def __init__(self):
        pass

    def get_ticket_by_id(self, ticket_id):
        try:
            if type(ticket_id) is not int:
                return {}, INVALID_TICKET_ID
            response = requests.get(f"{TICKET_BY_ID_URL}{ticket_id}", auth=(USER, TOKEN))
            return response.json(), response.status_code
        except requests.ConnectionError:
            print(f"unable to establish connection to {TICKET_BY_ID_URL}")
        except AttributeError as ae:
            print(f"invalid response received from url {TICKET_BY_ID_URL}")
            print(ae)

    def get_tickets_by_page_url(self, page_url):
        try:
            response = requests.get(page_url, auth=(USER, TOKEN))
            return response.json(), response.status_code
        except requests.ConnectionError:
            print(f"unable to establish connection to {page_url}")
        except AttributeError as ae:
            print(f"invalid response received from url {page_url}")
            print(ae)

    def display_ticket_by_page(self, next_page=TICKETS_BY_PAGINATION):
        try:
            response, status_code = self.get_tickets_by_page_url(next_page)
            if status_code == 200:
                if not response["tickets"]:
                    print("next page not found")
                    self.display_options()
                else:
                    print(
                        f"{'id'!s:6} {'subject'!s:45} {'priority'!s:8} {'created_at'!s:25} {'status'!s:10}"
                    )
                    for ticket in response["tickets"]:
                        print(
                            f"{ticket['id']!s:6} {ticket['subject'][:45]!s:45} {str(ticket['priority'])[:8]!s:8}"
                            f"{ticket['created_at'][:25]!s:25} {ticket['status'][:10]!s:10}"
                        )
                    if not response['meta']['has_more']:
                        self.display_options()
                    next_page = self.get_next_link(response)
                    if not next_page:
                        self.display_options()
                    else:
                        self.display_ticket_by_page(next_page)
            else:
                print(f"unable to query for page {status_code} {response}")
        except KeyError as ke:
            print("Key Error!!.unable to retrieve required fields from api")
            print(ke)
            exit()

    def get_next_link(self, response, count=0):
        try:
            self.display_pagination_options()
            option = input("your option:")
            if option in ['n', 'p', 'm', 'P', 'M', 'N']:
                option = option.lower()
                if option == "p":
                    return response["links"]["prev"]
                elif option == "n":
                    return response["links"]["next"]
                elif option == "m":
                    return None
                else:
                    if count == 3:
                        self.display_options()
                        return None
                    return self.get_next_link(response, count=count + 1)
            else:
                if count == 3:
                    self.display_options()
                    return None
                return self.get_next_link(response, count=count + 1)
        except KeyError as ke:
            print("Unable to get required fields from the API")
            print(ke)
            exit()

    def display_options(self):
        self.display_options_message()
        option = input("Enter your option")
        if option.isdigit() and int(option) in [1, 2, 3]:
            option = int(option)
            if option == 1:
                self.display_ticket_by_page()
            elif option == 2:
                self.display_ticket_by_id()
            else:
                exit()
        else:
            print("***************Invalid option****************************")
            self.display_options()

    def display_options_message(self):
        print("***********Zendesk Ticket Viewer****************")
        print("select options")
        print("Select 1 Display ALl Tickets")
        print("Select 2 to view a Ticket ")
        print("Select 3 to quit")

    def display_pagination_options(self):
        print(" Press N for Next Ticket")
        print(" Press P for Previous Ticket")
        print("Press M for Main menu")

    def display_ticket_by_id(self):
        option = input("Enter ID")
        if option.isnumeric():
            option = int(option)
            response, status = self.get_ticket_by_id(option)
            if status == 200:
                pprint.pprint(response)
            else:
                print(f"unable to display ticket with id {option}")
                print(response, status)
            self.display_options()
        else:
            print("invalid Input")
            self.display_options()


if __name__ == "__main__":
    t = TickerLister()
    t.display_options()
