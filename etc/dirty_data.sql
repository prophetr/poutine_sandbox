/*------------------------------------------------------------------------------

DIRTY DATA

The purpose of this file is to inject incorrect data into tables in the 
ecommerce_backend schema to demo how DBT test feature works.

Tables effected: products, order_items & inventory_items

!! Note: For reference only !!

------------------------------------------------------------------------------*/

use warehouse "COMPUTE_WH";
use database "DBT_POUTINESHOP_RAW";
use schema "RAW_DATA";

--------------------------------------------------------------------------------
-- products
--------------------------------------------------------------------------------
select * from "DBT_POUTINESHOP_RAW"."RAW_DATA"."PRODUCTS" 
where id in (11033, 425, 1009, 8903, 29000, 100, 18166, 683, 14717, 27398);

---- break not null test
update "DBT_POUTINESHOP_RAW"."RAW_DATA"."PRODUCTS"
    set sku = null
    where id in (425, 1009, 8903, 29000, 100);

---- break unique test
update "DBT_POUTINESHOP_RAW"."RAW_DATA"."PRODUCTS"
    set sku = '73278A4A86960EEB576A8FD4C9EC6997'
    where id = 18166;

---- break unique test
update "DBT_POUTINESHOP_RAW"."RAW_DATA"."PRODUCTS"
    set sku = '5AD742CD15633B26FDCE1B80F7B39F7C'
    where id = 683;

---- break unique test
update "DBT_POUTINESHOP_RAW"."RAW_DATA"."PRODUCTS"
    set sku = 'F6F20ADA728B7A41EA4C0EB996C817B6'
    where id = 14717;
    
---- break unique test
update "DBT_POUTINESHOP_RAW"."RAW_DATA"."PRODUCTS"
    set sku = '6E1BEE0C59EF09E191D26ADE686DACF8'
    where id = 27398;
    
-- break relationships test
update "DBT_POUTINESHOP_RAW"."RAW_DATA"."PRODUCTS"
    set distribution_center_id = 9001
    where id  = 11033;

--------------------------------------------------------------------------------
-- order_items
--------------------------------------------------------------------------------
select * from "DBT_POUTINESHOP_RAW"."RAW_DATA"."ORDER_ITEMS" 
where id in (298433, 56567, 68410, 84202, 289395);

---- break accepted_values with null
update "DBT_POUTINESHOP_RAW"."RAW_DATA"."ORDER_ITEMS"
    set status = NULL
    where id in (298433, 56567, 68410, 84202);

---- break not null test
update "DBT_POUTINESHOP_RAW"."RAW_DATA"."ORDER_ITEMS"
    set order_id = NULL
    where id = 289395;
    
--------------------------------------------------------------------------------
-- inventory_items
--------------------------------------------------------------------------------
select * from "DBT_POUTINESHOP_RAW"."RAW_DATA"."INVENTORY_ITEMS" 
where id in (288038, 218960, 325238, 45766, 99912);

---- break not null test
update "DBT_POUTINESHOP_RAW"."RAW_DATA"."INVENTORY_ITEMS"
    set product_id = NULL
    where id in (288038, 218960, 325238, 45766, 99912);
