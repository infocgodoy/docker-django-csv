from django.core.management.base import BaseCommand
from django.utils import timezone
import csv 
from django.shortcuts import render, HttpResponse
import sqlite3

class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        con = sqlite3.connect('db.sqlite3')
        cur = con.cursor()
        
        cur.execute('SELECT model as sku,"" as store_view_code,"has_variants" as attribute_set_code,"configurable" as product_type,((CASE WHEN category_5_1 != 0 and category_5_2 != 0 and category_5_3 != 0 THEN "default/"||category_5_1||","||"default/"||category_5_1||"/"||category_5_2||","||"default/"||category_5_1||"/"||category_5_2||"/"||category_5_3||"," END)||(CASE WHEN category_6_1 != 0 and category_6_2 != 0 and category_6_3 != 0 THEN "default/"||category_6_1||","||"default/"||category_6_1||"/"||category_6_2||","||"default/"||category_6_1||"/"||category_6_2||"/"||category_6_3 WHEN category_7_1 != 0 and category_7_2 != 0 and category_7_3 != 0 THEN "default/"||category_7_1||","||"default/"||category_7_1||"/"||category_7_2||","||"default/"||category_7_1||"/"||category_7_2||"/"||category_7_3 WHEN category_8_1 != 0 and category_8_2 != 0 and category_8_3 != 0 THEN "default/"||category_8_1||","||"default/"||category_8_1||"/"||category_8_2||","||"default/"||category_8_1||"/"||category_8_2||"/"||category_8_3 END)) as categories,"base" as product_websites,name as name,long_description as description,short_description as short_description,"0.5" as weight,"1" as product_online,"Taxable Goods" as tax_class_name,"Catalog, Search" as visibility,price as price,"" as special_price,"" as special_price_from_date,"" as special_price_to_date,(REPLACE((name||"-"||max(sku))," ","-")) as url_key,"" as meta_title,"" as meta_keywords,"" as meta_description,"" as base_image,"" as base_image_label,"" as small_image,"" as small_image_label,"" as thumbnail_image,"" as thumbnail_image_label,"" as swatch_image,"" as swatch_image_label,"" as created_at,"" as updated_at,"" as new_from_date,"" as new_to_date,"" as display_product_options_in,"" as map_price,"" as msrp_price,"" as map_enabled,"" as gift_message_available,"" as custom_design,"" as custom_design_from,"" as custom_design_to,"" as custom_layout_update,"" as page_layout,"" as product_options_container,"Use config" as msrp_display_actual_price_type,"" as country_of_manufacture,("manufacturer="||(CASE WHEN brand IS NULL THEN "" ELSE brand END)||","||"application_advice="||(CASE WHEN application_advice IS NULL THEN "" ELSE application_advice END)||","||"attribute_format_container="||(CASE WHEN attribute_format_container IS NULL THEN "" ELSE attribute_format_container END)||","||"vegetal_active="||(CASE WHEN vegetal_active IS NULL THEN "" ELSE vegetal_active END)||","||"attribute_container="||(CASE WHEN attribute_container IS NULL THEN "" ELSE attribute_container END)||","||"inci="||(CASE WHEN inci IS NULL THEN "" ELSE inci END)||","||"attribute_esencia="||(CASE WHEN attribute_esencia IS NULL THEN "" ELSE attribute_esencia END)||","||"attribute_hair_type="||(CASE WHEN attribute_hair_type IS NULL THEN "" ELSE attribute_hair_type END)||","||"attribute_type_perfume="||(CASE WHEN attribute_type_perfume IS NULL THEN "" ELSE attribute_type_perfume END)||","||"attribute_texture="||(CASE WHEN attribute_texture IS NULL THEN "" ELSE attribute_texture END)||","||"attribute_type_skin="||(CASE WHEN attribute_type_skin IS NULL THEN "" ELSE attribute_type_skin END)||","||"attribute_zone="||(CASE WHEN attribute_zone IS NULL THEN "" ELSE attribute_zone END)||","||"color="||(CASE WHEN attribute_color IS NULL THEN "" ELSE attribute_color END)||","||"attribute_ip_solar="||(CASE WHEN attribute_ip_solar IS NULL THEN "" ELSE attribute_ip_solar END)||","||"attribute_action="||(CASE WHEN attribute_action IS NULL THEN "" ELSE attribute_action END)||","||"attribute_class="||(CASE WHEN attribute_class IS NULL THEN "" ELSE attribute_class END)||","||"attribute_type_product="||(CASE WHEN attribute_type_product IS NULL THEN "" ELSE attribute_type_product END)||","||"attribute_type_care="||(CASE WHEN attribute_type_care IS NULL THEN "" ELSE attribute_type_care END)||","||"attribute_need="||(CASE WHEN attribute_need IS NULL THEN "" ELSE attribute_need END)||","||"attribute_line="||(CASE WHEN attribute_line IS NULL THEN "" ELSE attribute_line END)||","||"summary="||(CASE WHEN summary IS NULL THEN "" ELSE summary END)||","||"beauty_advice="||(CASE WHEN attribute_beauty IS NULL THEN "" ELSE attribute_beauty END)) as additional_attributes,"99" as qty,"0.0000" as out_of_stock_qty,"1" as use_config_min_qty,"0" as is_qty_decimal,"0" as allow_backorders,"1" as use_config_backorders,"10.000" as min_cart_qty,"1" as use_config_min_sale_qty,"0.0000" as max_cart_qty,"1" as use_config_max_sale_qty,"1" as is_in_stock,"" as notify_on_stock_below,"1" as use_config_notify_stock_qty,"0" as manage_stock,"1" as use_config_manage_stock,"1" as use_config_qty_increments,"0.0000" as qty_increments,"1" as use_config_enable_qty_inc,"0" as enable_qty_increments,"0" as is_decimal_divided,"0" as website_id,"" as related_skus,"" as related_position,"" as crosssell_skus,"" as crosssell_position,"" as upsell_skus,"" as upsell_position,"" as additional_images,"" as additional_image_labels,"" as hide_from_product_page,"" as custom_options,"" as bundle_price_type,"" as bundle_sku_type,"" as bundle_price_view,"" as bundle_weight_type,"" as bundle_values,"" as bundle_shipment_type,(group_concat("sku="||sku||","||"color="||attribute_color,"|")) as configurable_variations,"" as configurable_variation_labels,"" as associated_skus FROM master_products_configurable group by model')
    
        with open('csv.csv', 'w', newline='') as csvfile:
            
            writer = csv.writer(csvfile,delimiter=';')            
            
            arr = []    

            for colinfo in cur.description:        
                arr.append(colinfo[0])        
            
            myData = [arr]
                
            # cabecera inicio
            writer.writerows(myData)
            # cabecera fin
            # cuerpo inicio
            for member in cur:
                #print(member)
                writer.writerow(member)    
            # cuerpo fin
        
        self.stdout.write("El archivo se creo en el directorio raiz y su nombre es Csv.csv")