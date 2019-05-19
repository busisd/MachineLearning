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

def calc_score(steps, pos, target):
	dist_factor = abs(pos[0]-target[0]) + abs(pos[1]-target[1])
	steps_factor = len(steps)
	return 1000*dist_factor + steps_factor

grid = MazeGrid()
target = (9,9)
start = (0,0)
current_steps = [move_right, move_down, move_right]
end = execute_steps(current_steps, start, grid)
print(end)
print(calc_score(current_steps, end, target))



