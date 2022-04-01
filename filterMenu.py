import csv 
import os



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
    
    def Justsave(jobsListing):
        with open('progress_filter.csv', 'a') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["save",jobsListing[0], jobsListing[1], jobsListing[2], jobsListing[3]])


    print_menu()
    option = ''
    try:
        option = int(input('Enter your choice: '+ "\n"))
    except:
        Justsave(jobsListing)
        # print('Wrong input. Please enter a number ...')
    #Check what choice was entered and act accordingly
    if option == 1:    
        option1(jobsListing)
    elif option == 2:
        option2(jobsListing)
    elif option == 3:
        option3(jobsListing)
    elif option == 4:
        Justsave(jobsListing)
    #     exit()
    # else:
    #     print('Invalid option. Please enter a number between 1 and 4.')

