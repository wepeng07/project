import sys, os
sys.path.insert(1, os.getcwd())

from part2.parser.parse import parseArgs
db_task_id = 0
args = sys.argv
print(parseArgs(args))
