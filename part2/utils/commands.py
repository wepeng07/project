from asyncio import tasks
import re
from part2.db.manager import add_task, change_priority, complete_task, get_all_tasks, remove_task, search, sort, update_desc


def showhelp():
    print('usage: python main.py <options>')
    print('===== options =====')
    print('-h or --help to print this menu.')
    print('-l or --list to list all tasks.')
    print('-a or --add <DESCRIPTION> to add a new task')
    print('-p or --priority <NUMBER> to assign a priority to a new task. Must use with -a or -s.')
    print('-r or --remove <ID> remove a task.')
    print('-c or --complete <ID> mark a task as complete.')
    print('-cp or --changepriority <ID> <NUMBER> change an existing task\'s priority.')
    print('-u or --update <ID> <DESCRIPTION> update an existing task\'s description.')
    print('-s or --search <OPTIONS> search a task by options.')
    print('-t or --sort show sorted list of tasks by increasing order of priority.')
    print('-d or --desc decreasing order of priority. Must use with -t.')
    print('-i or --id <ID> task ID. Must use with -s for search task with ID.')
    print('-dp or --description <TEXT> task description. Must use with -s for search task with description.')

# command to list all tasks
def list_all_tasks_cmd():
    tasks = get_all_tasks()
    if (len(tasks) == 0):
        return 'TODO List empty. Add some tasks.'
    else:
        new_tasks=""
        for str in tasks:
            
            #print(str)
            str_list = str.split(',')
            new_str = "ID: " + str_list[0] + " DESC: " + str_list[1] + " PRIORITY: " + str_list[2] + " STATUS: " + str_list[3]
            # print(re.sub("\d*,\D*,\d*,\D*", "ID: \d*: DESC: \D* PRIORITY: \d* STATUS: \D*", str))

            new_tasks +=  new_str
        
            # re.sub(",", ": ", str)
        #print(new_tasks.size())
        # print(new_tasks)
        # print(new_tasks.split('\n'))
        return new_tasks

def list_all_tasks():
    tasks = get_all_tasks()
    if (len(tasks) == 0):
        return 'TODO List empty. Add some tasks.'
    else:
        new_tasks=""
        for str in tasks:
            new_tasks +=  str
        
        # re.sub(",", ": ", str)
        #print(new_tasks.size())
        # print(new_tasks)
        # print(new_tasks.split('\n'))
        return new_tasks


# command to add a task
def add_task_cmd(task, priority):
    if (not task or priority < 0):
        return 'Failed to add task'
    id = add_task(task, priority)
    return 'Task added and assigned ID ' + str(id)

# command to delete a task
def remove_task_cmd(id):
    if (not remove_task(id)):
        return 'Failed to remove task ID ' + str(id)
    else:
        return 'Removed task ID '+ str(id)

# command to complete a task
def complete_task_cmd(id):
    if (not complete_task(id)):
        return 'Task ' + str(id) + ' could not be completed'
    else:
        return 'Task ' + str(id) + ' completed'

# command to edit task priority
def change_priority_cmd(id, priority):
    if (not change_priority(id, priority)):
        return 'Priority of task ' + str(id) + ' could not be changed'
    else:
        return 'Changed priority of task ' + str(id) + ' to ' + str(priority) 


# command to edit task description
def update_cmd(id, desc):
    if (not update_desc(id, desc)):
        return 'Failed to update task ' + str(id)
    else:
        return 'Task ' + str(id) + ' updated'

# command to search a task by id, description, or priority
def search_cmd(id = None, desc = None, priority = None):
    res = search(id, desc, priority)
    # print("res= ", res)
    if (not res):
        return 'Task not found'
    else:
        return res

# command to sort the tasks in specified order
def sort_cmd(order=None):
    if ( order == '-d'):
        return sort(2)
    else:
        return sort()
