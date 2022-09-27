import pandas as pd
import string
import random
from datetime import datetime,timedelta

#IDS

def gen_create_ids(number_of_ids,len_of_id,id_type='alphanumerical', unique=False):
    
    """
        Function creates a list of randomized ids. 
        
        Parameters:
            number_of_ids = total number of ids generated
            len_of_id = id character length
            id_type = alphabetical, numerical or alphanumerical (default)
            unique = True or False
        
        Example of ids generated (len_of_id == 12): 
            alphabetical: abcdefghjklm
            numerical: 123456789012
            alphanumerical: 7vraAnT8rdGJ
        
        Returns:
        _type_: _description_
    """
    
    alphabetical = string.ascii_letters
    numerical = string.digits
    alphanumerical = string.ascii_letters + string.digits
    id_list = []
    
    #non-unique ids
    if not unique:    
        if id_type=='alphabetical':
            for i in range(number_of_ids):
                id_list.append(''.join(random.choice(alphabetical) for x in range(len_of_id)))
        elif id_type=='numerical':
            for i in range(number_of_ids):
                id_list.append(''.join(random.choice(numerical) for x in range(len_of_id)))
        elif id_type=='alphanumerical':
            for i in range(number_of_ids):
                id_list.append(''.join(random.choice(alphanumerical) for x in range(len_of_id)))
        
    #unique ids
    if unique:           
        if id_type=='alphabetical':
            while len(id_list) < number_of_ids: #while loop to ensure consistent # of records and uniqueness of ids
                id = ''.join(random.choice(alphabetical) for x in range(len_of_id))
                if id not in id_list:
                    id_list.append(id)
                else:
                    break
        if id_type=='numerical':
            while len(id_list) < number_of_ids: #while loop to ensure consistent # of records and uniqueness of ids
                id = ''.join(random.choice(numerical) for x in range(len_of_id))
                if id not in id_list:
                    id_list.append(id)
                else:
                    break
        if id_type=='alphanumerical':
            while len(id_list) < number_of_ids: #while loop to ensure consistent # of records and uniqueness of ids
                id = ''.join(random.choice(alphanumerical) for x in range(len_of_id))
                if id not in id_list:
                    id_list.append(id)
                else:
                    break
    
    return id_list


#DATETIMES: created_at, updated_at, published_at

def gen_create_shopify_datetimes(num_of_records):
    """
        Function creates 3 separate sequenced dates - created_at, updated_at, published_at (respectively). Each date has a randomized delta of 18k seconds (5 days).
        To call each date separately of each other, call the attributes passed in the function:
        - create_shopify_datetimes.created_at
        - create_shopify_datetimes.updated_at
        - create_shopify_datetimes.published_at
        
        Returns:
        _type_: _description_
    
    """
    
    min_date = datetime(2006,1,1,0,0,0) #date Shopify was founded
    max_date = datetime.now()

    secs_bn_dates = (max_date - min_date).seconds

    created_at_dts = []
    updated_at_dts = []
    published_at_dts = []


    for i in range(num_of_records):

        random_num_secs_0 = random.randrange(secs_bn_dates)
        random_num_secs_1 = random.randrange(432000) #5 days arbitrarily chosen
        random_num_secs_2 = random.randrange(432000) #5 days arbitrarily chosen

        #created_at field
        created_at_dt = min_date + timedelta(seconds=random_num_secs_0)

        #updated_at field
        updated_at_dt = created_at_dt + timedelta(seconds=random_num_secs_1)

        #published_at field
        published_at_dt = updated_at_dt + timedelta(seconds=random_num_secs_2)

        #append to respective dates lists
        created_at_dts.append(created_at_dt)
        updated_at_dts.append(updated_at_dt)
        published_at_dts.append(published_at_dt)
    
    
    created_at = pd.Series(created_at_dts)
    updated_at = pd.Series(updated_at_dts)
    published_at = pd.Series(published_at_dts)
    
    #datetime attributes
    gen_create_shopify_datetimes.created_at = created_at_dts
    gen_create_shopify_datetimes.updated_at = updated_at_dts
    gen_create_shopify_datetimes.published_at = published_at_dts
    
    dates_df = pd.DataFrame({
        'created_at':created_at,
        'updated_at':updated_at,
        'published_at':published_at
        }
    )
    
    return dates_df