from unittest import TestCase
from TickerLister import TickerLister
from config import *

class TestTickerLister(TestCase):
    def test_get_ticket_by_id(self):
        _,ret = TickerLister().get_ticket_by_id("abv")
        self.assertTrue(ret == INVALID_TICKET_ID)


    def test_get_tickets_by_page_url(self):
        res,status_code = TickerLister().get_tickets_by_page_url(f"{TICKETS_BY_PAGINATION}1")
        self.assertEqual(type(res),dict,"received invalid response")
        res = TickerLister().get_tickets_by_page_url("httP://dnmcbdscbldclk.com")
        self.assertEqual(res, None, "Invalid url check failed")





