import datetime as dt
import random
import string
import hashlib

def create_ids(number_of_ids,len_of_id):
    # creates a list of random id's: length = number_of_ids, len_of_id is id character length
    # example of id generated: 7vraAnT8rdGJ (len_of_id == 12)
    options = string.ascii_letters + string.digits
    id_list = []
    for i in range(number_of_ids):
        id_list.append(''.join(random.choice(options) for x in range(len_of_id)))
    return id_list

def create_random_times(number_of_entries, start_date = '1/1/2021', max_amount_of_seconds=10000):
    # creates a list (len == number_of_entries) of random times, 
    # generated a random amount of seconds from 1/1/2021
    # with a possibility to have a modified start_date and a max time range
    times_list = []
    for i in range(0,number_of_entries):
        start = dt.datetime.strptime(start_date+' 12:00 AM', '%m/%d/%Y %I:%M %p')
        random_second = random.randrange(max_amount_of_seconds)
        time = start + dt.timedelta(seconds=random_second)
        times_list.append(time)
    return times_list

def create_md5_ids(number_of_ids):
    # creates a list of md5-encoded ids, len(list) == number_of_ids
    md5_id_list = []
    id_list = create_ids(number_of_ids, 20)
    for id in id_list:
        md5_id_list.append(hashlib.md5(id.encode('utf-8')).hexdigest())
    return md5_id_list
