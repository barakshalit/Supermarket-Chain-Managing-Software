from persistence import *

import sys

def main(args : list[str]):
    inputfilename : str = args[1]

    with open(inputfilename) as inputfile:
        for line in inputfile:
            splittedline : list[str] = line.strip().split(", ")
            # product is arivved
            if int(splittedline[1]) > 0:
                x= splittedline[0]
                prouductOrm = repo.products.find(id = x)
                quantitiy = prouductOrm[0].quantity
                newQuantitiy = quantitiy + int(splittedline[1])

                id = prouductOrm[0].id
                description = prouductOrm[0].description
                price = prouductOrm[0].price
                
                repo.products.delete(id =splittedline[0]) 
                repo.products.insert(Product(id,description,price,newQuantitiy)) 
                addToActivities(splittedline) 


            else:
                x= splittedline[0]
                prouductOrm = repo.products.find(id = x)
                quantitiy = prouductOrm[0].quantity
                newQuantitiy = quantitiy + int(splittedline[1])

                if newQuantitiy > 0: #check if its legal
                    id = prouductOrm[0].id
                    description = prouductOrm[0].description
                    price = prouductOrm[0].price
                
                    repo.products.delete(id =splittedline[0]) 
                    repo.products.insert(Product(id,description,price,newQuantitiy)) 
                    addToActivities(splittedline) #see if we need to inset to table at any case? or if its not done not to insert?

               

            

def addToActivities(splittedline):
    repo.activities.insert(Activitie(splittedline[0],splittedline[1],splittedline[2],splittedline[3]))


if __name__ == '__main__':
    main(sys.argv)