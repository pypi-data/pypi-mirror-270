import datetime
import re

import autocommand
import dateutil.parser
from splinter import Browser

from . import contact as contact_info
from .compat.py38 import removeprefix


DROPPED_CALL = '2'


def clean_phone(number):
    """
    >>> clean_phone("+1 202 555 1212")
    '2025551212'
    """
    return re.sub(r'[-. ]', '', removeprefix(number, '+1'))


@autocommand.autocommand(__name__)
def report_spam_call(
    number,
    comment='',
    close=False,
    browser='firefox',
    when: dateutil.parser.parse = datetime.datetime.now(),  # type: ignore
):
    """
    Report the common spam calls.
    """
    contact = contact_info.load()
    browser = Browser(browser)
    browser.visit('https://www.donotcall.gov/report.html')
    browser.find_by_value('Continue').click()
    browser.fill('PhoneTextBox', clean_phone(contact.phone))
    browser.fill('DateOfCallTextBox', when.strftime('%m/%d/%Y'))  # type: ignore
    browser.select('TimeOfCallDropDownList', when.strftime('%H'))  # type: ignore
    browser.select('ddlMinutes', when.strftime('%M'))  # type: ignore
    browser.choose('PrerecMsg', 'PrerecordMessageYESRadioButton')
    browser.choose('TextMsg', 'PhoneCallRadioButton')
    browser.select(
        'ddlSubjectMatter',
        DROPPED_CALL,
    )
    browser.find_by_value('Continue').click()
    browser.fill('CallerPhoneNumberTextBox', clean_phone(number))
    browser.choose('HaveBusiness', 'HaveBusinessNoRadioButton')
    browser.choose('StopCalling', 'StopCallingNoRadioButton')
    browser.fill('FirstNameTextBox', contact.first_name.replace('.', ''))
    browser.fill('LastNameTextBox', contact.last_name)
    browser.fill('StreetAddressTextBox', contact.street_address)
    browser.fill('CityTextBox', contact.city)
    browser.select('StateDropDownList', contact.state)
    browser.fill('ZipCodeTextBox', contact.zip)
    browser.fill('CommentTextBox', comment)
    browser.find_by_value('SUBMIT').click()
    if close:
        browser.windows.current.close()
