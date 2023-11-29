
database1 = []
project = []
workers = 0
project_status = ["ongoing", "onhold", "completed"]

while True:
    # while loop is used to loop the main menu until the user choose exit (6)
    print("XYZ Company")
    print("Main Menu")
    print("1. Add a new project to existing project")
    print("2. Remove a completed project from existing project")
    print('3. Add new workers to available workers group')
    print('4. update details on ongoing projects')
    print('5. Project statistics')
    print("6. Exit    ")
    num = int(input("Enter your selection: "))
    if num == 1:
        print("XYZ Company")
        print("Add a new project")
        project_code = int(input("Enter Project Code (Enter 0 to project code to exit): "))
        if project_code == 0:
            exit(project_code)
        else:
            client_name = input("Enter Client name: ")
            start_date = input("Enter start date :")
            end_date = input("Enter expected end  date: ")
            no_of_workers = int(input("Input number of worker: "))
            status = str(input("Enter project status ('ongoing','on hold' or 'completed'):"))
            # use only the values give in the brackets
            if status == "ongoing":
                status = project_status[0]
            elif status == "onhold":
                status = project_status[1]
            elif status == "completed":
                status = project_status[3]
            else:
                print("Invalid value, try again")
            save_project = input("Do you want to save the project (yes/no):")
            if save_project == "yes" or "Yes" or "YES" or "y" or "Y":
                project = [project_code, client_name, start_date, end_date, no_of_workers, status]
                database1.append(project)

            elif save_project == "no" or "No" or "NO" or "n" or "N":
                exit(save_project)
            else:
                print("invalid input please try again")
    elif num == 2:
        print("XYZ Company")
        print("Remove Completed Project")
        project_code = int(input("Enter project code:"))
        remove_project = input("Do you want to remove the project (yes/no):")
        if remove_project == "y" or "yes" or "YES" or "Yes" or "Y":

    elif num == 4:
        print("XYZ Company")
        print("Update Project Details")
        project_code = int(input("Enter Project Code (Enter 0 to project code to exit): "))
        if project_code == 0:
            exit(project_code)
        else:

            client_name = input("Enter Client name: ")
            name.append(client_name)
            start_date = input("Enter start date :")
            s_date.append(start_date)
            end_date = input("Enter expected end  date: ")
            e_date.append(end_date)
            workers = int(input("Input number of worker: "))
            status = int(input("Enter project status ('ongoing'= 1, 'on hold'= 2 or 'completed'= 3):"))
            if status == 1:
                status = project_status[0]
            elif status == 2:
                status = project_status[1]
            elif status == 3:
                status = project_status[3]
            else:
                print("Invalid value, try again")
            update_project = input("Do you want to update the project (yes/no):")
            if update_project == "yes":
                database1.append(project_code)
                database1.append(name)
                database1.append(s_date)
                database1.append(e_date)
                database1.append(workers)
                database1.append(status)
            elif update_project == "no":
                exit(update_project)
            else:
                print("invalid input please try again")
    elif num == 3:
        print("XYZ Company")
        print("Add Workers")
        no_of_workers = int(input("Number of workers to add:"))
        add_workers = input("Do you want to add (yes/no):")
        if add_workers == "yes" or "Yes" or "YES" or "y" or "Y":
            workers = workers + no_of_workers
        elif add_workers == "no" or "No" or "NO" or "n" or "N":
            exit(no_of_workers)
        else:
            exit(no_of_workers)
    elif num == 5:
        print("XYZ Company")
        print("Project Statistics")
        ongoing_projects = database1.count("ongoing")
        onhold_projects = database1.count("onhold")
        completed_projects = database1.count("completed")
        print("Number of Ongoing projects:", ongoing_projects)
        print("Number of Onhold projects:", onhold_projects)
        print("Number of Completed: ", completed_projects)
    elif num == 6:
        exit()
