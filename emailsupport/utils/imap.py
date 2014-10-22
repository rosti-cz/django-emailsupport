from __future__ import unicode_literals
from imbox import Imbox

HOST = 'mail.rosti.cz'
USERNAME = 'support@rbas.cz'
PASSWORD = 'support'
USE_SSL = False


def get_unread_messages():
    imbox = Imbox(HOST,
                  username=USERNAME,
                  password=PASSWORD,
                  ssl=USE_SSL)

    # Unread messages
    unread_messages = imbox.messages(unread=True)
    return unread_messages


if __name__ == '__main__':
    import pprint
    pprint.pprint(list(get_unread_messages()))