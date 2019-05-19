import random

class MazeGrid:
	def __init__(self, rows = 10, cols = 10):
		self.rows = 10
		self.cols = 10

def in_grid(pos, grid):
	return pos[0] >= 0 and pos[1] >= 0 and pos[0] < grid.rows and pos[1] < grid.cols

def move_up(pos, grid):
	new_pos = (pos[0]-1, pos[1])
	if in_grid(new_pos, grid):
		return new_pos
	else:
		return pos

def move_right(pos, grid):
	new_pos = (pos[0], pos[1]+1)
	if in_grid(new_pos, grid):
		return new_pos
	else:
		return pos

def move_down(pos, grid):
	new_pos = (pos[0]+1, pos[1])
	if in_grid(new_pos, grid):
		return new_pos
	else:
		return pos

def move_left(pos, grid):
	new_pos = (pos[0], pos[1]-1)
	if in_grid(new_pos, grid):
		return new_pos
	else:
		return pos

def execute_steps(steps, start_pos, grid):
	pos = start_pos
	for step in steps:
		pos = step(pos, grid)
	return pos

def calc_score(steps, start, target, grid):
	pos = execute_steps(steps, start, grid)
	dist_factor = abs(pos[0]-target[0]) + abs(pos[1]-target[1])
	steps_factor = len(steps)
	return 1000*dist_factor + steps_factor
	
possible_steps = [move_up, move_right, move_left, move_down]
def perform_mutations(steps, mutations=3, constructiveness=.9):
	new_steps = steps.copy()
	for i in range(mutations):
		r = random.random()
		if (r<constructiveness):
			rand_index = random.randrange(len(new_steps)+1)
			rand_step = random.randrange(len(possible_steps))
			new_steps.insert(rand_index, possible_steps[rand_step])
		else:
			if len(new_steps) > 0:
				rand_index = random.randrange(len(new_steps))
				new_steps.pop(rand_index)
	return new_steps

def find_best_step_list(step_lists, start, target, grid):
	min_score = calc_score(step_lists[0], start, target, grid)
	best_list = step_lists[0]
	for cur_list in step_lists[1:]:
		cur_list_score = calc_score(cur_list, start, target, grid)
		if cur_list_score < min_score:
			min_score = cur_list_score
			best_list = cur_list
	return best_list

grid = MazeGrid()
start = (0,0)
target = (9,9)

current_steps = []
for i in range(10):
	cur_score = calc_score(current_steps, start, target, grid)
	
	new_step_lists = []
	for j in range(5):
		new_step_lists.append(perform_mutations(current_steps))
		
	new_steps = find_best_step_list(new_step_lists, start, target, grid)
	print(new_steps, end = ' : ')
	if calc_score(new_steps,start,target,grid)<calc_score(current_steps,start,target,grid):
		current_steps = new_steps
	print(current_steps)

