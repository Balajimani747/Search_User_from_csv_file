import csv

print("Data Presant in CSV file")
with open("names.csv","r") as show_data:
    read=csv.reader(show_data)
    for row in read:
        print(row)
    print("----------------------------------------------------------------------------")
while True:
    with open("names.csv","r") as user_data:
        read=csv.reader(user_data)
        print("Search The User:")
        user_name=input("Enter the User First_Name: ")
        count=0
        for row in read:
            if user_name in row:
                print(row)
                count=count+1  
        if count>0:
            pass
        else:
            print("User Data Not Present")
    print("----------------------------------------------------------------------------")
        
    