Vegan = input("Type 'yes' if anyone in your party is vegan, if not, type in 'no': ")
Gluten = input("Type 'yes' if anyone in your party is gluten free, if not, type in 'no': ")
Veg = input("Type 'yes' if anyone in your party is vegetarian, if not, type in 'no': ")

if Veg == "yes" or Veg == "no":
    if Vegan == "yes" or Vegan == "no":
        if Gluten == "yes" or Gluten == "no":
            
            if Veg == "yes":
                if Vegan == "yes":
                    if Gluten == "yes" or Gluten == "no":
                        print("Corner Cafe and The Chef's Kitchen")
                else:
                    if Gluten == "yes":
                        print("Main Street Pizza Company, Corner Cafe, and the Chef's Kitchen")
                    
                    else:
                        print("Main Street Pizza Company, Corner Cafe, Mama's Fine Italian, and the Chef's Kitchen")
                    
            else:
                if Vegan == "yes":
                    
                    if Gluten == "yes" or Gluten == "no":
                        print("Corner Cafe and the Chef's Kitchen")
                else:
                    if Gluten == "yes":
                        print("Main Street Pizza Company, Corner Cafe, and The Chef's Kitchen")
                        
                    else:
                        print("Main Street Pizza Company, Joe's Gourmet Burgers, Corner Cafe, Mama's Fine Italian, and The Chef's Kitchen")
