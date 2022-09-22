# imports
from venv import create
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import string
import random
import lorem
from faker import Faker

#import functions_file
from generic_functions import *

#initialize generators
fake = Faker()

#Seeds
np.random.seed(0)
random.seed(0)
Faker.seed(0)


#PRODUCTS DATAFRAME

def shopify_product_df(num_of_rows):
    
    """ Generates a dataframe emulating Shopify product table
    """
    
    #product_id - Shopify product id 8 digits, ie. 6776271208513; use set/list to remove duplicates

    ids = gen_create_ids(num_of_rows, 8, id_type='numerical', unique=True)
    product_id = pd.Series(ids)
    
    #ids attribute
    shopify_product_df.all_ids = ids
    

    #body_html field: description of product

    body_html = [ lorem.sentence() for i in range(num_of_rows) ]
    body_html = pd.Series(body_html)
    
    
    #title(product name) & handle (short version of title)
    
    title = []
    handle = []
    
    for i in range(num_of_rows):
        txt = lorem.sentence().split()
        title_0 = txt[0] + " " + txt[1] + " " + txt[2]
        handle_0 = txt[0] + " " + txt[1]
        title.append(title_0)
        handle.append(handle_0)
    title = pd.Series(title)
    handle = pd.Series(handle)
    
    #titles attribute
    shopify_product_df.all_titles = title
    shopify_product_df.all_handles = handle

    #product_type
    
    product_type = [ lorem.sentence().split()[0] for i in range(num_of_rows) ]
    product_type = pd.Series(product_type)
    
    
    #vendor - Use faker company name
    
    vendor = [ fake.company() for i in range(num_of_rows) ]
    vendor = pd.Series(vendor)
    
    
    #datetimes: created_at, updated_at, published_at
    
    all_dates_df = gen_create_shopify_datetimes(num_of_rows)
    created_at = all_dates_df.loc[:,'created_at']
    updated_at = all_dates_df.loc[:,'updated_at']
    published_at = all_dates_df.loc[:,'published_at']
    
    shopify_product_df.created_at_dts = gen_create_shopify_datetimes.created_at
    shopify_product_df.updated_at_dts = gen_create_shopify_datetimes.updated_at
    shopify_product_df.published_at_dts = gen_create_shopify_datetimes.published_at


    #create product status; ie. active, draft, archived
    
    prod_status = []
    prod_status_values = 'active','archived','draft'
    status_weights = [0.50,0.25,0.25]
    
    for i in range(num_of_rows):
        prod_status.append(np.random.choice(prod_status_values,p=status_weights))
    
    status = pd.Series(prod_status)

    
    #dataframe
    
    df_product = pd.DataFrame({
        'id':product_id,
        'body_html':body_html,
        'title':title,
        'handle':handle,
        'product_type':product_type,
        'vendor':vendor,
        'created_at':created_at,
        'updated_at':updated_at,
        'published_at':published_at,
        'status':status
        }
    )
    
    #dataframe attributes
    shopify_product_df.df_product_columns = df_product
    

    return df_product
    

#PRODUCT_VARIANT DATAFRAME

def shopify_product_variant_df(num_of_rows):
    
    """Generates a dataframe emulating Shopify product variant table
    """
    
    #product_id, title, created_at, updated_at from product table
    
    try:
        product_df = shopify_product_df.df_product_columns.loc[:,['id','title','created_at','updated_at']]
    
    except AttributeError:
        
        #product_ids
        ids = gen_create_ids(num_of_rows, 8, id_type='numerical', unique=True)
        product_id = pd.Series(ids)

        #title
        title_lst = []
        for i in range(num_of_rows):
            txt = lorem.sentence().split()
            title_lst.append(txt[0] + ' ' + txt[1])
        title = pd.Series(title_lst)
        
        #created_at and updated_at
        gen_create_shopify_datetimes(num_of_rows)
        created_at = pd.Series(gen_create_shopify_datetimes.created_at)
        updated_at = pd.Series(gen_create_shopify_datetimes.updated_at)
    

    #inventory_item_id
    
    inv_item_id = gen_create_ids(num_of_rows,9,id_type='numerical',unique=True)
    inventory_item_id = pd.Series(inv_item_id)
    
    #image_id
    
    img_ids = gen_create_ids(num_of_rows,9,id_type='numerical')
    image_id = pd.Series(img_ids)
        
    #barcode
    
    barcode = gen_create_ids(num_of_rows,14,id_type='numerical')
    barcode = pd.Series(barcode)
    
    #price - float
    
    min_price = 1
    max_price = 5000
    
    price_lst = [ round(random.uniform(min_price,max_price),2) for i in range(num_of_rows) ]  
    price = pd.Series(price_lst)
    
    #compare_at_price
        
    compare_at_price = [ round(i - (i * random.uniform(0,1)),2) for i in price ]
    compare_at_price = pd.Series(compare_at_price)
    
    #weight
    
    min_weight = 10
    max_weight = 5000
    
    weight_lst = [ round(random.uniform(min_weight,max_weight),2) for i in range(num_of_rows) ]
    weight = pd.Series(weight_lst)
    
    
    #weight_unit
    
    weight_values = ['g', 'kg', 'oz', 'lb']
    weight_weights = [0.40,0.10,0.40,0.10]
    
    weight_unit = [ np.random.choice(weight_values,p=weight_weights) for i in range(num_of_rows) ]
    
    #inventory_quantity
    
    min_qty = 0
    max_qty = 5000
    
    qty_lst = [ random.randrange(min_qty,max_qty) for i in range(num_of_rows) ]
    inventory_quantity = pd.Series(qty_lst)
    
    #sku
    
    sku = gen_create_ids(num_of_rows,8,id_type='alphanumerical')
    sku = pd.Series(sku)
    
    
    #product variant dataframe 
    try:
        #product_id, title, created_at, updated_at from product table
        df_product_variant = product_df.assign(
            inventory_item_id = inventory_item_id,
            image_id=image_id,
            barcode=barcode,
            compare_at_price=compare_at_price,
            inventory_quantity=inventory_quantity,
            price=price,
            sku=sku,
            weight=weight,
            weight_unit=weight_unit   
        )
        df_product_variant=df_product_variant.rename(columns={"id":"product_id"})
        
    except UnboundLocalError:
        df_product_variant = pd.DataFrame({
            "product_id":product_id,
            "inventory_item_id":inventory_item_id,
            "image_id":image_id,
            "barcode":barcode,
            "compare_at_price":compare_at_price,
            "created_at":created_at,
            "inventory_quantity":inventory_quantity,
            "price":price,
            "sku":sku,
            "title":title,
            "updated_at":updated_at,
            "weight":weight,
            "weight_unit":weight_unit
        })
        
    #dataframe attributes
    shopify_product_variant_df.df_product_variant_columns = df_product_variant
    

    return df_product_variant

    
#PRODUCT_IMAGE DATAFRAME

def shopify_product_image_df(num_of_rows):
    
    """Generates a dataframe emulating Shopify product image table
    """
    
    #product_id, image_id (rename to id), created_at, updated_at from product table
    
    try:
        product_variant_df = shopify_product_variant_df.df_product_variant_columns.loc[:,['product_id','image_id','created_at','updated_at']]
        txt = shopify_product_variant_df.df_product_variant_columns.loc[:,['title']].tolist()
        src_lst = [ i.rsplit(' ', 1)[0].replace(' ','-').lower() for i in txt ]
    
    except AttributeError:
        
        #product_ids
        ids = gen_create_ids(num_of_rows, 8, id_type='numerical', unique=True)
        product_id = pd.Series(ids)
        
        #image_id
        img_ids = gen_create_ids(num_of_rows,9,id_type='numerical')
        image_id = pd.Series(img_ids)
        
        #created_at and updated_at
        gen_create_shopify_datetimes(num_of_rows)
        created_at = pd.Series(gen_create_shopify_datetimes.created_at)
        updated_at = pd.Series(gen_create_shopify_datetimes.updated_at)
        
        #src_list from 'title'
        src_lst = []
        for i in range(num_of_rows):
            txt = lorem.sentence().split()
            src_lst.append(txt[0].lower() + "-" + txt[1].lower())
    

    #height and width
    
    min_pixels = 100
    max_pixels = 3000
    
    height_lst = [ round(random.randrange(min_pixels,max_pixels),2) for i in range(num_of_rows) ]
    width_lst = [ round(random.randrange(min_pixels,max_pixels),2) for i in range(num_of_rows) ]
    height = pd.Series(height_lst)
    width = pd.Series(width_lst)
    
    #positon
    
    position_lst = [ round(random.randrange(1,100),2) for i in range(num_of_rows) ]
    position = pd.Series(position_lst)
    
    #is_default
    
    is_default_options = ["Y","N"]
    is_default = [np.random.choice(is_default_options) for i in range(num_of_rows)]
    
    #src - example format:"http://static.shopify.com/products/ipod-nano.png"
    
    const_img_src_str_1 = "http://static.shopify.com/products/"
    const_img_src_str_2 = [".jpg",".png"]

    src = [ const_img_src_str_1 + i + np.random.choice(const_img_src_str_2) for i in src_lst ]
        
    src = pd.Series(src)
    
    #product image dataframe

    try:
        #product_id, image_id, created_at, updated_at from product variant table
        df_product_image = product_variant_df.assign(
            height=height,
            is_default=is_default,
            position=position,
            src=src,
            width=width
        )
        df_product_image = df_product_image.rename(columns={"image_id":"id"})
        
    except UnboundLocalError:
        df_product_image = pd.DataFrame({
            "id":image_id,
            "product_id":product_id,
            "created_at":created_at,
            "height":height,
            "is_default":is_default,
            "position":position,
            "src":src,
            "updated_at":updated_at,
            "width":width
            
        })
        
    #dataframe attributes
    shopify_product_image_df.df_product_image_columns = df_product_image
    

    return df_product_image
    
    
#INVENTORY_ITEM DATAFRAME

def shopify_inventory_item_df(num_of_rows):
    
    """Generates a dataframe emulating Shopify inventory item table
    """
    
    #id (inventory_item_id, price, sku)
    
    try:
        product_variant_df = shopify_product_variant_df.df_product_variant_columns.loc[:,['inventory_item_id','sku']]
        price_lst = shopify_product_variant_df.df_product_variant_columns.loc[:,['price']].tolist()
        
    except AttributeError:
        
        #inventory_item_id
        inv_item_id = gen_create_ids(num_of_rows,9,id_type='numerical',unique=True)
        inventory_item_id = pd.Series(inv_item_id)
        
        #price
        min_price = 1
        max_price = 5000

        price_lst = [ round(random.uniform(min_price,max_price),2) for i in range(num_of_rows) ]  
        
        #sku
        sku = gen_create_ids(num_of_rows,8,id_type='alphanumerical')
        sku = pd.Series(sku)
    
    #cost
    
    cost = [ round(p * random.uniform(0.20,1),2) for p in price_lst ]
    
    #country_code_of_origin
        
    country_code_of_origin = [ 'CA' for i in range(num_of_rows) ]
    
    #created_at and updated_at
    
    all_dates_df = gen_create_shopify_datetimes(num_of_rows)
    created_at = all_dates_df.loc[:,'created_at']
    updated_at = all_dates_df.loc[:,'updated_at']
    
    #province_code_of_origin
    
    province_codes = ['ON','AB','NS','QC','BC','YT','NU','NT','MB','SK','NB','NL','PE']
    
    province_code_of_origin = [ np.random.choice(province_codes) for i in range(num_of_rows) ]
    
    #requires_shipping (TRUE/FALSE)
    
    requires_shipping = [bool(random.getrandbits(1)) for i in range(num_of_rows)]
    
    #tracked
    
    tracked = [bool(random.getrandbits(1)) for i in range(num_of_rows)]
    
    #inventory item dataframe

    try:
        #inventory_item_id, sku from product variant table
        
        df_inventory_item = product_variant_df.assign(
            cost=cost,
            country_code_of_origin=country_code_of_origin,
            created_at=created_at,
            province_code_of_origin=province_code_of_origin,
            requires_shipping=requires_shipping,
            tracked=tracked,
            updated_at=updated_at
        )
        df_inventory_item = df_inventory_item.rename(columns={"inventory_item_id":"id"})
        
    except UnboundLocalError:
        df_inventory_item = pd.DataFrame({
            "id":inventory_item_id,
            "sku":sku,
            "cost":cost,
            "country_code_of_origin":country_code_of_origin,
            "created_at":created_at,
            "province_code_of_origin":province_code_of_origin,
            "requires_shipping":requires_shipping,
            "tracked":tracked,
            "updated_at":updated_at
            
        })
    
    #dataframe attributes
    shopify_inventory_item_df.df_inventory_item_columns = df_inventory_item
    

    return df_inventory_item


#INVENTORY_LEVEL DATAFRAME

def shopify_inventory_level_df(num_of_rows):
    
    """Generates a dataframe emulating Shopify inventory level table
    """
    
    #inventory_item_id
    
    try:
        inventory_item_df = shopify_inventory_item_df.df_inventory_item_columns.loc[:,['id']]
        available = shopify_product_variant_df.df_product_variant_columns.loc[:,['inventory_quantity']].squeeze().tolist()
        
    except AttributeError:
        
        #inventory_item_id
        inv_item_id = gen_create_ids(num_of_rows,9,id_type='numerical',unique=True)
        inventory_item_id = pd.Series(inv_item_id)
        
        #available
        min_qty = 0
        max_qty = 5000

        qty_lst = [ random.randrange(min_qty,max_qty) for i in range(num_of_rows) ]
        available = pd.Series(qty_lst)
        
    #location_id
    location_id = gen_create_ids(num_of_rows,8,id_type='numerical', unique=True)
    
    #updated_at
    all_dates_df = gen_create_shopify_datetimes(num_of_rows)
    updated_at = all_dates_df.loc[:,'updated_at']
    
    #inventory level dataframe

    try:
        #inventory_item_id, inventory_quantity
        
        df_inventory_level = inventory_item_df.assign(
            available=available,
            location_id=location_id,
            updated_at=updated_at
        )
        df_inventory_level = df_inventory_level.rename(columns={"inventory_quantity":"available","id":"inventory_item_id"})
        
    except UnboundLocalError:
        df_inventory_level = pd.DataFrame({
            "inventory_item_id":inventory_item_id,
            "available":available,
            "location_id":location_id,
            "updated_at":updated_at
            
        })
    
    #dataframe attributes
    shopify_inventory_level_df.df_inventory_level_columns = df_inventory_level
    

    return df_inventory_level


#CALL ALL DATAFRAMES

def all_shopify_dataframes(num_of_rows):
    
    """Generates all of the above dataframes
    """
    
    product_df = shopify_product_df(num_of_rows)
    product_variant_df = shopify_product_variant_df(num_of_rows)
    product_image_df = shopify_product_image_df(num_of_rows)
    inventory_item_df = shopify_inventory_item_df(num_of_rows)
    inventory_level_df = shopify_inventory_level_df(num_of_rows)
    
    return product_df, product_variant_df, product_image_df, inventory_item_df, inventory_level_df

#RUN TO GET ALL DATAFRAMES

#num_of_rows = number of desired rows
#product_df, product_variant_df, product_image_df, inventory_item_df, inventory_level_df = all_shopify_dataframes(num_of_rows)