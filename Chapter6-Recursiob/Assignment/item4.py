def string_to_int_list(s, result_list=None):
   if result_list is None:
      result_list = []

   # Base Case:
   if not s:
      return result_list

   # Recursive Case:
   else:
      result_list.append(int(s[0]))
      return string_to_int_list(s[1:], result_list)


def create_grid(rows_data, r, c, current_r=0, grid=None):
   if grid is None:
      grid = []

   # Base Case:
   if current_r == r:
      return grid

   # Recursive Case:
   else:
      row_str = rows_data[current_r]
      int_row = string_to_int_list(row_str)
      grid.append(int_row)
      return create_grid(rows_data, r, c, current_r + 1, grid)


def water_flow(grid, r, c, source_height):
   max_r = len(grid)
   max_c = len(grid[0])

   # --- Base Cases ---
   if not (0 <= r < max_r and 0 <= c < max_c):
      return
   if grid[r][c] == 0:
      return
   if grid[r][c] > source_height:
      return

   # --- Recursive Cases ---
   else:
      current_height = grid[r][c]
      grid[r][c] = 0

      water_flow(grid, r - 1, c, current_height)# up
      water_flow(grid, r + 1, c, current_height)# down
      water_flow(grid, r, c - 1, current_height)# left
      water_flow(grid, r, c + 1, current_height)# right


def print_grid(grid, row_index=0):
   # Base Case:
   if row_index == len(grid):
      return

   # Recursive Case:
   else:
      print("".join(map(str, grid[row_index])))
      return print_grid(grid, row_index + 1)


# --- Main Program ---
print(" *** Water Flow ***")
try:
   grid_str, high_str, water_str = input("Input rows,cols/data1,data2,.../start_row,start_col : ").split("/")

   r, c = map(int, grid_str.split(","))
   high_data = high_str.split(",")
   water_r, water_c = map(int, water_str.split(","))


   if not (len(high_data) == r and all(len(row) == c for row in high_data)):
      print("Error: Rows and columns must be between 1 and 9")
   elif not (0 <= water_r < r and 0 <= water_c < c):
      print("Error: Start coordinates are out of grid bounds")
   else:
      area_grid = create_grid(high_data, r, c)

      start_height = area_grid[water_r][water_c]

      area_grid[water_r][water_c] = 0

      water_flow(area_grid, water_r - 1, water_c, start_height) # up
      water_flow(area_grid, water_r + 1, water_c, start_height) # down
      water_flow(area_grid, water_r, water_c - 1, start_height) # left
      water_flow(area_grid, water_r, water_c + 1, start_height) # right

      print_grid(area_grid)

except (ValueError, IndexError):
   print("Error: Invalid input format.")