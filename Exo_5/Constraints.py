import json
import csv
import os.path

f = open('..\\data.json', )
data = json.load(f)



filename ='.\\NoProd_logfile.csv'
with open(filename, 'w') as csvfile:
    fieldnames = ['id', 'Product_name','status']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    file_exists = os.path.isfile(filename)

# ************************************************Debut Traitement***************************************************************
    for Bundles in data['Bundles']:

      if type(Bundles.get('Products')) is list:

        for Product in Bundles['Products']:
         # To print available Product i use the variable Isavailable (there is another varaible Isinstock)
          if (Product.get('IsAvailable')== True):
           ############ %1f to have one number after comma, and i used [0:29] to truncate
           print('You can buy '+Product.get('Name')[0:29],'at our store at ','%.1f' %(Product.get('Price')))
          if (Product.get('IsAvailable')== False):

               writer.writerow({'id': Product.get('Stockcode'), 'Product_name': Product.get('Name'),'status': 'Unvailable'})
          if (Product.get('IsAvailable') == None):


              writer.writerow({'id': Product.get('Stockcode'), 'Product_name': Product.get('Name'),'status':'Error'})

f.close()
