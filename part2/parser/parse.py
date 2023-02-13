from ast import arg
# from utils.commands as cmd
import sys, os
from this import d
from part2.db.manager import get_all_tasks, search
sys.path.append('C:\\Users\\xuan\\Documents\\GitHub\\cise337-hw1-wepeng07')
# print(sys.path)

from part2.utils.commands import add_task_cmd, change_priority_cmd, complete_task_cmd, remove_task_cmd, search_cmd, showhelp, list_all_tasks_cmd, list_all_tasks, sort_cmd, update_cmd

# parse the command line arguments and execute the appropriate commands.
def parseArgs(args):
   
    global task_id
    if (len(args) > 1 ):
        
        if (args[1] == "-h" or args[1] == "--help"):
            showhelp()
        elif (args[1] == "-l" or args[1] == "--list"):
            return list_all_tasks()
        elif (args[1] == "-a" or args[1] == "--add"):
            if (len(args) > 5):
                return 'Error: Found extraneous options'

            if (len(args) == 4):
                if (args[2] == "-p" or args[2] == "--priority"):
                    return 'Error: Incorrect priority option'

                if (args[3] == "-p" or args[2] == "--priority"):
                    return 'Error: Cannot add a task with empty priority'
                

            if (len(args) == 5 and (not str(args[4]).isdigit())):
                return 'Priority must be integer'
        
            return add_task_cmd(args[2], int(args[4]))
            
        elif (args[1] == "-r" or args[1] == "--remove"):
            if (len(args) == 3 and (not str(args[2]).isdigit())):
                return 'Task ID must be a number'
            if (len(args) == 2):
                return 'Task ID missing'
            if (len(args) == 5):
                
                return 'Error: Found extraneous options'
            return remove_task_cmd(args[2])
        
        elif (args[1] == "-c" or args[1] == "--complete"):
            if (len(args) == 3 and (not str(args[2]).isdigit())):
                return 'Task ID must be a number'
            if (len(args) == 2):
                return 'Task ID missing'
            if (len(args) == 5):
                return 'Error: Found extraneous options'

            return complete_task_cmd(args[2])

        elif (args[1] == "-cp" or args[1] == "--changepriority"):
            if (len(args) == 3 and (not str(args[2]).isdigit())):
                return 'Task ID must be a number'
            if (len(args) == 2):
                return 'Task ID or priority missing'
            if (len(args) == 5):
                return 'Error: Found extraneous options'

            return change_priority_cmd(args[2], args[3])

        elif (args[1] == "-u" or args[1] == "--update"):
            if (len(args) == 4 and (not str(args[2]).isdigit())):
                return 'Task ID must be a number'
            if (len(args) == 2):
                return 'Task ID or description missing'
            if (len(args) == 5):
                return 'Error: Found extraneous options'

            return update_cmd(args[2], args[3])

        elif (args[1] == "-s" or args[1] == "--search"):

            if (len(args) == 2):
                return 'Search Criteria Missing'

            if (len(args) > 9 or len(args) == 3 or len(args) == 5 or len(args) == 7):
                return "Search Criteria Wrong Input: Please use a correct search criteria"

            if (len(args) == 4):
                if (args[2] == "-i" or args[2] == "--id"):
                    return search_cmd(int(args[3]), None, None)
                
                elif (args[2] == "-dp" or args[2] == "--description"):
                    return search_cmd(None, args[3], None)

                elif (args[2] == "-p" or args[2] == "--priority"):
                    return search_cmd(None, None, int(args[3]))
                else:
                    return "Search Criteria Wrong Input1"

            if (len(args) == 6):
                id = None
                priority = None
                dp = None
              
                if ((args.count('-i') == 1) or (args.count('--id') == 1) or (args.count('-id') == 1)):
                    if (args.count('-i') == 1):
                        id = args[args.index('-i') + 1]
                    if (args.count('--id') == 1):
                        id = args[args.index('--id') + 1]
                    if (args.count('-id') == 1):
                        id = args[args.index('-id') + 1]
                    
                    if ((not str(id).isdigit()) ):
                        return 'search ID and priority must be integer.'
                    
                    if ((args.count('-p') ==1) or (args.count('--priority') ==1) or (args.count('-priority') ==1)):
                       
                        
                        if "-p" in args:
                            priority = args[args.index('-p') + 1]
                        if "--priority" in args:
                            priority = args[args.index('--priority') + 1]
                        if "-priority" in args:
                            priority = args[args.index('-priority') + 1]

                        if ( (not str(priority).isdigit()) ):
                            return 'search ID and priority must be integer.'

                        return search_cmd(id, None, priority)

                    elif (("-dp" in args) or ("--decription" in args) or ("--dp" in args)):
                        
                        if "-dp" in args:
                            dp = args[args.index('-dp') + 1]
                        if "--description" in args:
                            dp = args[args.index('--description') + 1]
                        if "--dp" in args:
                            dp = args[args.index('--dp') + 1]
                        return search_cmd(id, dp, None)

                    else:
                        return "Search Criteria Wrong Input2"

                else:
                    if "-p" in args:
                        priority = args[args.index('-p') + 1]
                    if "--priority" in args:
                        priority = args[args.index('--priority') + 1]
                    if "-priority" in args:
                        priority = args[args.index('-priority') + 1]
                    

                    if ( (not str(priority).isdigit()) ):
                        return 'search ID and priority must be integer.'

                    if "-dp" in args:
                        dp = args[args.index('-dp') + 1]
                    if "--description" in args:
                        dp = args[args.index('--description') + 1]
                    if "--dp" in args:
                        dp = args[args.index('--dp') + 1]

                    return search_cmd(None, dp, priority)
                
                
                

            if (len(args) == 8):
                id = None
                if "-i" in args:
                    id = args[args.index('-i') + 1]
                if "--id" in args:
                    id = args[args.index('--id') + 1]
                
                if ( (not str(id).isdigit()) ):
                    return 'search ID and priority must be integer.'

                priority = None
                if "-p" in args:
                    priority = args[args.index('-p') + 1]
                if "--priority" in args:
                    priority = args[args.index('--priority') + 1]
                if ( (not str(priority).isdigit()) ):
                    return 'search ID and priority must be integer.'

                dp = None
                if "-dp" in args:
                    dp = args[args.index('-dp') + 1]
                if "--description" in args:
                    dp = args[args.index('--description') + 1]

                return search_cmd(id, dp, priority)

            
            



        elif (args[1] == "-t" or args[1] == "--sort"):
            if(len(args) > 3):
                return 'Error: Found extraneous options'
            if(len(args) == 2):
                return sort_cmd()
            if(len(args) == 3):
                if(args[2] == '-d'):
                    return sort_cmd('-d')
                else:
                    return "sort_cmd: wrong input"
            
            

    else:
        return 'Missing Required argument. Type -h to seek help'
