import csv

def add_to_csv(info_list):
    with open('student_information.csv', 'a', newline='') as csv_file:
        writer = csv.writer(csv_file)
        
        if csv_file.tell() == 0:
            writer.writerow(["First Name", "Last Name", "Age", "Date of Birth(DOB)", "Phone Number", "Email ID"])
        
        writer.writerow(info_list)

print("Welcome to the ABC school administration system. \nUse this python program to enter the details of students.")
print("\n")
if __name__ == '__main__':
    
    condition = True
    
    student_sr_num = 1
    
    while(condition):
        student_info = input("Enter the student information for student no.{} in the given order (First_name Last_name Age DOB_in_dd/mm/yyyy Phone_number Email_ID): ".format(student_sr_num))
        
        print("\n")
        
        print("Your entered student info is: " + student_info)
        
        print("\n")
        
        student_info_list = student_info.split(' ')
        print("Split student information" + str(student_info_list))
        
        print("\n")
        
        print("\nInformation entered is: \nFirst_name:- {}\nLast_name:- {}\nAge:- {}\nDOB:- {}\nPhone_Number:- {}\nEmail_ID:- {}".format(student_info_list[0], student_info_list[1], student_info_list[2], student_info_list[3], student_info_list[4], student_info_list[5]))
        
        check_info = input("Do you confirm that given information is correct?(Yes/No): ")
        
        if check_info == "Yes":        
            add_to_csv(student_info_list)
        
            confirm = input("Do you want to add more student information?(Yes/No): ")
            if confirm == "Yes":
                condition = True
                student_sr_num = student_sr_num + 1
            elif confirm == "No":
                condition = False
        elif check_info == "No":
            print("\nPlease re-enter your information.")