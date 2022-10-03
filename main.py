def doorArea(file):
    import ifcopenshell
    file = ifcopenshell.open(file)
    size = []
    products = file.by_type('IfcDoor')
    doors = []
    
    for product in products:
        if product.is_a('IfcDoor'):
            doors.append(product)
            
    for i in doors:
        size.append(i[4])
#    doorSizes.append(doorSize(file))

    import re
    
    sizeSplit = []
    for i in range(len(doorSize)):
        sizeSplit.append(doorSize[i].split("x"))
    
        
    sizeInt = []
    for i in range(len(sizeSplit)):
        number1 = re.sub(r'[^0-9]', '', str(sizeSplit[i][0]))
        number2 = re.sub(r'[^0-9]', '', str(sizeSplit[i][1]))
#        number = str(number)
        sizeInt.append(number1)
        sizeInt.append(number2)
        
    
    area = []
    for i in range(0, len(sizeInt), 2):
        if i+1 < len(sizeInt):
            area.append((int(sizeInt[i])*int(sizeInt[i+1]))/1000000)
        else:
            break
    print(sizeInt)
    print(len(sizeInt))
    return area