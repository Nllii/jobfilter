import csv 
import os

# def checking_progress():
if os.path.exists('progress_filter.csv'):
    with open("progress_filter.csv") as f:
        lines = f.readlines()
    lines
    print(lines[0])
    lines[0] = "status,hiring_company,get_time,get_url,site_name \n"
    lines # ["This is the line that's replaced.\n", 'This is the second line.\n']
    with open("progress_filter.csv", "w") as f:
        f.writelines(lines)
    for line in lines:
        line_count = len(lines)


# if exist progress_filter.csv
#     with open("progress_filter.csv") as f:
#         lines = f.readlines()
        # return line_count


# def continue_filter():
#     print("\n")
#     print("Do you want to continue from where you left off? (y/n)")
#     continue_filter = input()
#     if continue_filter == 'y':
#         return True
#     elif continue_filter == 'n':
#         return False
#     else:
#         print("Invalid input. Please enter 'y' or 'n'")
#         continue_filter()





def jobfilter_menu(jobsListing):

    menu_options = {
        1: 'Applied',
        2: 'Not Applied',
        3: 'Not Interested',
        4: 'Press Enter to continue...',
    }
    
    print("\n")
    print(jobsListing)

    def print_menu():
        for key in menu_options.keys():
            print (key, '--', menu_options[key] )

    def option1(jobsListing):
        with open('progress_filter.csv', 'a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Applied",jobsListing[0], jobsListing[1], jobsListing[2], jobsListing[3]])

            # writer.writerow(['hiring_company', 'get_time', 'get_url', 'site_name'])
    def option2(jobsListing):
        with open('progress_filter.csv', 'a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Not_Applied",jobsListing[0], jobsListing[1], jobsListing[2], jobsListing[3]])


    def option3(jobsListing):
        with open('progress_filter.csv', 'a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Not_Interested",jobsListing[0], jobsListing[1], jobsListing[2], jobsListing[3]])
    
    def option4(jobsListing):
        with open('progress_filter.csv', 'a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["save",jobsListing[0], jobsListing[1], jobsListing[2], jobsListing[3]])


    print_menu()
    option = ''
    try:
        option = int(input('Enter your choice: '))
    except:
        option4(jobsListing)
        # print('Wrong input. Please enter a number ...')
    #Check what choice was entered and act accordingly
    if option == 1:
        print("Applied")
        option1(jobsListing)
    elif option == 2:
        print("Not Applied")
        option2(jobsListing)
    elif option == 3:
        print("Not Interested")
        option3(jobsListing)
    elif option == 4:
        print("Just continue...")
        option4(jobsListing)
    #     exit()
    # else:
    #     print('Invalid option. Please enter a number between 1 and 4.')
# jobfilter_menu(jobsListing ="none")
