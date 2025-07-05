import os 
import sys 
from datetime import datetime

# command line todo list. 
TODO_FILE = "todolist.txt"

def load_todo_list:
	if(not os.path.exists(TODO_FILE)):
	return []

	with open((TODO_FILE), 'r') as file:
		lines = file.readlines()
	todo_list=[]

	for line in lines:
		line =line.strip()
		
