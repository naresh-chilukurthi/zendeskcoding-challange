import pprint
from config import *
import requests


class TickerLister:
    def __init__(self):
        pass

    def get_ticket_by_id(self, id):
        """
        fetches tickets by id
        :return:Json data,Error_message
        """
        try:
            if type(id) is not int:
                return {}, INVALID_TICKET_ID
            response = requests.get(f"{TICKET_BY_ID_URL}{id}", auth=(USER, TOKEN))
            return response.json(), response.status_code
        except requests.ConnectionError:
            print(f"unable to establish connection to {TICKET_BY_ID_URL}")

        except AttributeError as ae:
            print(f"invalid response received from url {TICKET_BY_ID_URL}")

    def get_ticket_by_page(self, page_id):
        """
        fetches tickets by id
        :return:Json data,Error_message
        """
        try:
            if type(page_id) is not int:
                return {}, INVALID_TICKET_ID
            response = requests.get(f"{TICKET_BY_ID_PAGE}{page_id}", auth=(USER, TOKEN))
            if response.status_code == 200:
                return response.json()
            else:
                return response.json(), response.status_code
        except requests.ConnectionError:
            print(f"unable to establish connection to {TICKET_BY_ID_PAGE}")
        except AttributeError as ae:
            print(f"invalid response received from url {TICKET_BY_ID_PAGE}")

    def get_tickets_by_page_url(self, page_url):
        try:
            response = requests.get(page_url, auth=(USER, TOKEN))
            return response.json(), response.status_code
        except requests.ConnectionError:
            print(f"unable to establish connection to {page_url}")
        except AttributeError as ae:
            print(f"invalid response received from url {page_url}")

    def get_tickets_count(self):
        try:
            response = requests.get(TICKET_COUNT_URL, auth=(USER, TOKEN))
            if response.status_code == 200:
                return response.json()["count"]["value"], response.status_code
            else:
                return response.json(), response.status_code
        except requests.ConnectionError:
            print(f"unable to establish connection to {TICKET_COUNT_URL}")
        except AttributeError as ae:
            print(f"invalid response received from url {TICKET_COUNT_URL}")
    def get_tickets_by_pagination(self):
        try:
            response = requests.get(TICKETS_BY_PAGINATION, auth=(USER, TOKEN))
            return response.json(), response.status_code
        except requests.ConnectionError:
            print(f"unable to establish connection to {TICKETS_BY_PAGINATION}")
        except AttributeError as ae:
            print(f"invalid response received from url {TICKETS_BY_PAGINATION}")

    def display_ticket_by_page(
        self, next_page=TICKETS_BY_PAGINATION, single_page=False
    ):
        try:
            response, status_code = self.get_tickets_by_page_url(next_page)
            if status_code == 200:
                if not response["tickets"]:
                    print("next page not found")
                    self.display_options()
                else:
                    print(
                        f"{'id'!s:3} {'subject'!s:40} {'priority'!s:3} {'created_at'!s:10} {'status'!s:8}"
                    )
                    for ticket in response["tickets"]:
                        print(
                            f"{ticket['id']!s:3} {ticket['subject']!s:40} {ticket['priority']!s:3} "
                            f"{ticket['created_at']!s:10} {ticket['status']!s:10}"
                        )
                    if single_page:
                        return
                    next_page = self.get_next_link(response)
                    if not next_page:
                        self.display_options()
                    else:
                        self.display_ticket_by_page(next_page)
            else:
                print(f"unable to query for page {response.status_code} {response}")
        except KeyError as ke:
            print("Key Error!!.unable to retrieve required fields from api")
            print(ke)
            exit()

    def get_next_link(self, response, count=0):
        try:
            self.display_pagination_options()
            option = input("your option:")
            if option.isascii() and ord(option) in [78, 80, 112, 110, 19, 77]:
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
                print("Invalid input")
                self.display_options()
        except KeyError as ke:
            print("Unable to get required fields from the API")
            print(ke)
            exit()

    def display_options(self):
        self.display_options_message()
        option = input()
        if option.isdigit() and int(option) in [1, 2, 3]:
            option = int(option)
            if option == 1:
                count, _ = self.get_tickets_count()
                if count > 25:
                    self.display_ticket_by_page()
                else:
                    self.display_ticket_by_page(single_page=True)
            elif option == 2:
                self.display_ticket_by_id()
            else:
                exit()
        else:
            print("Invalid option")
            self.display_options()

    def display_options_message(self):
        print("Zendesk Ticket Viewer")
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
                print(response, status)
            self.display_options()
        else:
            print("invalid Input")
            self.display_options()


if __name__ == "__main__":
    t = TickerLister()
    t.display_options()
