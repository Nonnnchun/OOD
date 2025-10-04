def solve_class_schedule(lessons, k):
   def can_schedule(capacity):
      periods_needed = 1
      current_time = 0
      for lesson_time in lessons:
         if lesson_time > capacity:
               return False
         if current_time + lesson_time <= capacity:
               current_time += lesson_time
         else:
               periods_needed += 1
               current_time = lesson_time
      return periods_needed <= k

   if not lessons:
      return 0, 0, []

   low = max(lessons)
   high = sum(lessons)
   optimal_max_period = high

   while low <= high:
      mid = (low + high) // 2
      if can_schedule(mid):
         optimal_max_period = mid
         high = mid - 1
      else:
         low = mid + 1

   groups = []
   current_group = []
   current_sum = 0
   for lesson_time in lessons:
      if current_group and (current_sum + lesson_time > optimal_max_period):
         groups.append(current_group)
         current_group = [lesson_time]
         current_sum = lesson_time
      else:
         current_group.append(lesson_time)
         current_sum += lesson_time
   if current_group:
      groups.append(current_group)

   while len(groups) < k:
      longest_group_idx = -1
      max_len = 1
      for i, group in enumerate(groups):
         if len(group) > max_len:
               max_len = len(group)
               longest_group_idx = i

      if longest_group_idx == -1:
         break

      group_to_split = groups.pop(longest_group_idx)

      new_group_after_split = [group_to_split.pop()] 

      groups.insert(longest_group_idx, group_to_split)
      groups.insert(longest_group_idx + 1, new_group_after_split)

   group_sums = [sum(g) for g in groups]
   max_p = max(group_sums) if group_sums else 0
   min_p = min(group_sums) if group_sums else 0
   diff = max_p - min_p
   
   return max_p, diff, groups


print("*** CLASS SCHEDULE ***")
user_input_str = input("Lesson times / periods: ")

parts = user_input_str.split('/')
lessons_str = parts[0].strip()
k_str = parts[1].strip()
lessons = [int(t) for t in lessons_str.split()]
k = int(k_str)

max_period, diff, groups = solve_class_schedule(lessons, k)

print(f"Max period: {max_period}")
print(f"Diff: {diff}")
print("Groups:")
for i, group in enumerate(groups, 1):
   group_sum = sum(group)
   print(f"  Group {i}: {group} → sum = {group_sum}")