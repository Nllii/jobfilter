
# def checking_progress():

def check_if_job_exists(job):
    with open('jobfilter.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for jobs_found in csv_reader:
            if jobs_found[2] == job:
                print("Job already exists in csv file")
                return jobs_found[2]
            else:
                print("Job does not exist in csv file")
                return jobs_found[2]

            # print(jobs_found[2])

            # print(line[5])
            # if line[2] == job:
            #     return True
            # else:
            #     return False



# if os.path.exists('progress_filter.csv'):
#     with open("progress_filter.csv") as f:
#         lines = f.readlines()
#     lines
#     print(lines[0])
#     lines[0] = "status,hiring_company,get_time,get_url,site_name \n"
#     lines # ["This is the line that's replaced.\n", 'This is the second line.\n']
#     with open("progress_filter.csv", "w") as f:
#         f.writelines(lines)
#     for line in lines:
#         # print(len(line))
#         get_url = line.split(',')[4]
#         print(check_if_job_exists(job = get_url))
            # print(get_url + " is not in the csv file")
            
            # jobfilter_menu(get_url)
            # print(get_url)

        # line_count = len(lines)
        # print(line_count)
        # break
    # print(lines[2])

# check if job already exists in csv file



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


