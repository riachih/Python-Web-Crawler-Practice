import time
from channel_link_list import link_list

while True:
    print(link_list.find().count())
    time.sleep(5)