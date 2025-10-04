def create_sorted_team_list(input_str):
   teams_data = []
   teams_list = input_str.split('/')

   for team_info in teams_list:
      details = team_info.split(',')
      name = details[0]
      wins = int(details[1])
      # loss = int(details[2]) --> 0
      draws = int(details[3])
      scored = int(details[4])
      conceded = int(details[5])

      points = (wins * 3) + (draws * 1)
      goal_difference = scored - conceded

      team_record = [name, {'points': points}, {'gd': goal_difference}]
      teams_data.append(team_record)

   for i in range(len(teams_data)):
      for j in range(0, len(teams_data) - i - 1):
         team1_points = teams_data[j][1]['points']
         team1_gd = teams_data[j][2]['gd']
         team2_points = teams_data[j + 1][1]['points']
         team2_gd = teams_data[j + 1][2]['gd']

         if team1_points < team2_points:
               teams_data[j], teams_data[j + 1] = teams_data[j + 1], teams_data[j]

         elif team1_points == team2_points:
               if team1_gd < team2_gd:
                  teams_data[j], teams_data[j + 1] = teams_data[j + 1], teams_data[j]
   return teams_data


inp = input("Enter Input : ")
sorted_teams = create_sorted_team_list(inp)

print("== results ==")
for team in sorted_teams:
   print(team)