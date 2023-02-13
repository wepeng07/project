from cgitb import reset
import os
import csv
from re import M
from webbrowser import get

tasks_file = os.path.join(os.getcwd(), 'part2','db', 'tasks.csv')

# creates tasks file is none exists
def create():
    if (is_tasks_file_exists()== False):      
        header = ['ID,DESCRIPTION,PRIORITY,STATUS\n']
        # writepath = 'C:\\Users\\xuan\\Documents\\cise337-hw1-wepeng07\\part2\\db\\tasks.csv'
 
        # mode = 'a' if os.path.exists(writepath) else 'w'
        # with open(writepath, mode) as f:
 
        # with open(csv.writer('C:\\Users\\xuan\\Documents\\cise337-hw1-wepeng07\\part2\\db\\tasks.csv', 'a+') as f:
        # with open('.\\part2\\db\\tasks.csv', 'w', encoding='UTF8') as f:
        # print(tasks_file)
        # with open(tasks_file, 'w', encoding='UTF8') as f:
        with open(tasks_file, 'w') as f:
            f.write('ID,DESCRIPTION,PRIORITY,STATUS\n')
        return True
    else:
        return False

# check if tasks file exists
def is_tasks_file_exists():
    return os.path.exists(tasks_file)
    


# adds a task to the task file and returns the task id.
def add_task(desc, priority):
    tasks = get_all_tasks()
    id = len(tasks) + 1
    with open(tasks_file, 'a') as f:   
        f.write(str(id) + "," + desc + "," + str(priority) + "," + "Incomplete\n") 
    print(get_all_tasks)
    return id
    
# returns list of tasks in the task file.
def get_all_tasks():
    create()
    with open(tasks_file, 'r') as f:
        content_list = f.readlines()[1: ]
    return content_list

# remove a task from the task file.
def remove_task(id):
    tasks = get_all_tasks()
    print(tasks)
    tasks_len = len(tasks)
    
    if (id > tasks_len or id <= 0):
        return False
    else:
        for i in range(id - 1, tasks_len - 1):
            task_str_list = tasks[i+1].split(',')
            new_task_id = int(task_str_list[0]) - 1
            tasks[i] = str(new_task_id) + "," + task_str_list[1] + "," + task_str_list[2] + "," + task_str_list[3]
        
        tasks.pop()
        print(tasks)

        with open(tasks_file, 'w') as f:
            f.write('ID,DESCRIPTION,PRIORITY,STATUS\n')
            f.writelines(tasks)  
        
        return True

# complete a task in the task file.
def complete_task(id):
    tasks = get_all_tasks()
    if (id > len(tasks) or id <= 0):
        return False
    else:
        task_str_list = tasks[id-1].split(',')
        tasks[id-1] = task_str_list[0] + "," + task_str_list[1] + "," + task_str_list[2] + "," + "Complete\n"

        with open(tasks_file, 'w') as f:
            f.write('ID,DESCRIPTION,PRIORITY,STATUS\n')
            f.writelines(tasks) 

        return True


# change the priority of a task in the task file.
def change_priority(id, priority):
    tasks = get_all_tasks()
    if (id > len(tasks) or id <= 0 or priority < 0):
        return False
    else:
        task_str_list = tasks[id-1].split(',')
        tasks[id-1] = task_str_list[0] + "," + task_str_list[1] + "," + str(priority) + "," + task_str_list[3]

        with open(tasks_file, 'w') as f:
            f.write('ID,DESCRIPTION,PRIORITY,STATUS\n')
            f.writelines(tasks) 

        return True

# update the task description of a task in the task file.
def update_desc(id, desc):
    tasks = get_all_tasks()
    if (id > len(tasks) or id <= 0 or not desc):
        return False
    else:
        task_str_list = tasks[id-1].split(',')
        tasks[id-1] = task_str_list[0] + "," + desc + "," + task_str_list[2] + "," + task_str_list[3]

        with open(tasks_file, 'w') as f:
            f.write('ID,DESCRIPTION,PRIORITY,STATUS\n')
            f.writelines(tasks) 

        return True

# search for a task in the task file.
def search(id, desc, priority):
    tasks = get_all_tasks()
   
    

    if ((not id) and (not desc) and (not priority)):
        # 000
        # print("000")
        return ''

    elif ((not id) and (not desc) and priority): 
        # 001
        res =""
        # print("001")
        if (priority < 0):
            return ''
        for t in tasks:
            if (int(t.split(',')[2]) == priority):
                res += t

        return res

    elif ((not id) and (desc) and (not priority)):
        # 010
        # print("010")
        res = ""
        for t in tasks:
            str_sp = t.split(',')
            if (str_sp[1].lower() == desc.lower()):
                res += t
        return res

    elif ((not id) and (desc) and (priority)):
        # 011
        # print("011")
        
        if (priority < 0):
            return ''
        res = ""
        for t in tasks:
            str_sp = t.split(',')
            if ((str_sp[1].lower() == desc.lower()) and (int(str_sp[2]) == priority)):
                res += t
                
        return res

    elif ((id) and (not desc) and (not priority)):
        # 100
        # print("100")
        if (id > len(tasks) or id <= 0):
            return ''
       
        return tasks[id-1]
        

    elif ((id) and (not desc) and (priority)):
        # 101
        # print("101")
        if (id > len(tasks) or id <= 0 or priority < 0):
            return ''

        for t in tasks:
            str_sp = t.split(',')
            if ( (int(str_sp[0]) == id) and (int(str_sp[2]) == priority)):
                
                return t
        return ''

    elif ((id) and (desc) and (not priority)):
        # # 110
        # print("110")
        if (id > len(tasks) or id <= 0):
            return ''

        for t in tasks:
            str_sp = t.split(',')
            if ( (int(str_sp[0]) == id) and (str_sp[1].lower() == desc.lower())):
                
                return t
        return ''

    elif ((id) and (desc) and (priority)):
        # 111
        # print("111")
        if (id > len(tasks) or id <= 0 or priority < 0):
            return ''

        for t in tasks:
            str_sp = t.split(',')
            # print (str_sp)
            if ( (int(str_sp[0]) == id) and (str_sp[1].lower() == desc.lower()) and (int(str_sp[2]) == priority)):
                return t
        
   
        return ''


    else:
        return ''


# sort the tasks in the task file. Default order is 1.
def sort(order = 1):
    
    tasks = get_all_tasks()
    if (order == 2):
        tasks.sort(key=lambda x: (x.split(',')[2]), reverse=True)
    else:
        tasks.sort(key=lambda x: (x.split(',')[2]), reverse=False)
    # print(tasks)
    res = ""
    for t in tasks:
        res += t
    return res
        

