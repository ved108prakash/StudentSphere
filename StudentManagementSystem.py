
db = {101:{'name':'sumit','city':'pune','passing_year': 2020,'percentage':89,'course': 'python','fee':40000},
      102:{'name':'ved','city':'delhi','passing_year': 2021,'percentage':89,'course': 'python','fee':42000},
      103:{'name':'satyam','city':'goa','passing_year': 2023,'percentage':75,'course': 'java','fee':41000}}
print('-'*100)
print(f'{' '*35}WelCome To The Kiran Academy')
print('-'*100)
while True:
    print("""
    1. Add Student Details
    2. Display Student Details
    3. Update Student Details
    4. Delete Student Details
    5. Search Student Details
    6. Filter Student Details  
    7. Add Extra Fee  
    """)
    ch = int(input('enter your choice: '))
    if ch == 1:
        reg = int(input('enter registration number: '))
        name = input('enter name: ')
        city = input('enter city: ')
        passing_year = int(input('enter passing_year: '))
        percentage = float(input('enter percentage: '))
        course = input('enter course name: ')
        fee = int(input('enter fee: '))
        db[reg]={'name':name,'city':city,'passing_year':passing_year,'percentage':percentage,
        'course':course,'fee':fee}
        print("Data Added Successfully.....")

    elif ch==2:
        print("-"*111)
        print('|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|'.format('Registration No','Name','City','Passing_year',
        'Percentage','Course','fee'))
        for reg in db:
            print("-"*111)
            print('|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|'.format(reg,db[reg]['name'],db[reg]['city'],db[reg]['passing_year'],
            db[reg]['percentage'],db[reg]['course'],db[reg]['fee']))
            print("-"*111)

    elif ch==3:
        reg=int(input("Enter Registration no.: "))
        print("""
        1. Name
        2. city
        3. passing_year
        4. percentage
        5. course
        6. Fee
            """)
        Choice=int(input("Enter your choice what you want to update: "))
        if Choice==1:
            Up_Name=input("Enter New name: ")
            db[reg]['name']=Up_Name
            print("Name Updated Successfuly....")
        elif Choice==2:
            Up_City=input("Enter New City: ")
            db[reg]['city']=Up_City
            print("City updated successfully....")
            
        elif Choice==3:
            Up_passing_y=input("Enter New passing_year: ")
            db[reg]['passing_year']=Up_passing_y
            print("passing_year Updated Successfuly....")
        elif Choice==4:
            Up_per=input("Enter New per: ")
            db[reg]['percentage']=Up_per
            print("percentage Updated Successfuly....")
        elif Choice==5:
            Up_course=input("Enter New course: ")
            db[reg]['course']=Up_course
            print("Course Updated Successfuly....")
        elif Choice==6:
            Up_fee=input("Enter New fee: ")
            db[reg]['fee']=Up_fee
            print("Fee Updated Successfuly....")
        else:
            print("Invalid Choice....")
        
    elif ch==4:
        reg=int(input("enter registration no: "))
        del db[reg]
        print("deleted successfully.....")
    elif ch==5:
        name=input("enter Student's Name: ")
        Details={}
        for key ,values in db.items():
                if name==values['name']:
                      Details[key]=values
                # else:
                #     print('{:^45}'.format("No Student Found........"))
        print("-"*111)
        print('|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|'.format('Registration No','Name','City','Passing_year',
                            'Percentage','Course','fee'))
        for reg in Details:
                                print("-"*111)
                                print('|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|'.format(reg,db[reg]['name'],db[reg]['city'],db[reg]['passing_year'],
                                db[reg]['percentage'],db[reg]['course'],db[reg]['fee']))
                                print("-"*111)
                                print("Database Filtered Successfully......")
    elif ch==6:
        print("""
        1. course
        2. passing_year
        3. percentage
        4. city
        5. fee
               """)
        fl=int(input("enter your filter: "))
        if fl==1:
            crs=input("enter course name: ")
            filter={}
            for i,j in db.items():
                    if crs==j['course']:
                        filter[i]=j
            else:
                    print('{:^65}'.format("No Student Found........"))
            print("-"*111)
            print('|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|'.format('Registration No','Name','City','Passing_year',
                            'Percentage','Course','fee'))
            for reg in filter:
                                print("-"*111)
                                print('|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|'.format(reg,db[reg]['name'],db[reg]['city'],db[reg]['passing_year'],
                                db[reg]['percentage'],db[reg]['course'],db[reg]['fee']))
                                print("-"*111)
                                print("Database Filtered Successfully......")
        elif fl==2:
            crs=int(input("enter passing_year name: "))
            filter={}
            for i,j in db.items():
                    if crs==j['passing_year']:
                        filter[i]=j
            else:
                            print('{:^65}'.format("No Student Found........"))
            print("-"*111)
            print('|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|'.format('Registration No','Name','City','Passing_year',
                            'Percentage','Course','fee'))
            for reg in filter:
                                print("-"*111)
                                print('|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|'.format(reg,db[reg]['name'],db[reg]['city'],db[reg]['passing_year'],
                                db[reg]['percentage'],db[reg]['course'],db[reg]['fee']))
                                print("-"*111)
                                print("Database Filtered Successfully......")
        elif fl==3:
            crs=int(input("enter percentage: "))
            filter={}
            for i,j in db.items():
                    if crs==j['percentage']:
                        filter[i]=j
            else:
                    print('{:^65}'.format("No Student Found........"))
            print("-"*111)
            print('|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|'.format('Registration No','Name','City','Passing_year',
                            'Percentage','Course','fee'))
            for reg in filter:
                                print("-"*111)
                                print('|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|'.format(reg,db[reg]['name'],db[reg]['city'],db[reg]['passing_year'],
                                db[reg]['percentage'],db[reg]['course'],db[reg]['fee']))
                                print("-"*111)
                                print("Database Filtered Successfully......")
        elif fl==4:
            crs=(input("enter city name: "))
            filter={}
            for i,j in db.items():
                    if crs==j['city']:
                        filter[i]=j
            else:
                    print('{:^65}'.format("No Student Found........"))
            print("-"*111)
            print('|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|'.format('Registration No','Name','City','Passing_year',
                            'Percentage','Course','fee'))
            for reg in filter:
                                print("-"*111)
                                print('|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|'.format(reg,db[reg]['name'],db[reg]['city'],db[reg]['passing_year'],
                                db[reg]['percentage'],db[reg]['course'],db[reg]['fee']))
                                print("-"*111)
                                print("Database Filtered Successfully......")
        elif fl==5:
            crs=int(input("enter fee: "))
            filter={}
            for i,j in db.items():
                    if crs==j['fee']:
                        filter[i]=j
            else:
                    print('{:^65}'.format("No Student Found........"))
            print("-"*111)
            print('|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|'.format('Registration No','Name','City','Passing_year',
                            'Percentage','Course','fee'))
            for reg in filter:
                                print("-"*111)
                                print('|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|'.format(reg,db[reg]['name'],db[reg]['city'],db[reg]['passing_year'],
                                db[reg]['percentage'],db[reg]['course'],db[reg]['fee']))
                                print("-"*111)
                                print("Database Filtered Successfully......")
    elif ch==7:
        fee_2=eval(input("enter Additional fee: "))
        print("-"*132)
        print('|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|'.format('Registration No','Name','City','Passing_year',
        'Percentage','Course','fee','Tatal_fee'))
        for reg in db:
            print("-"*132)
            print('|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|{:^15}|'.format(reg,db[reg]['name'],db[reg]['city'],db[reg]['passing_year'],
            db[reg]['percentage'],db[reg]['course'],db[reg]['fee'],((db[reg]['fee'])+fee_2)))
            print("-"*132)

    else:
        print("Invalid Choice: ")
    c=input("Do you want to continue --y/n: ")
    if c=='n':
        break
print("Thanks.....")
