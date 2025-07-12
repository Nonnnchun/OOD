def trans_to_int(list_of_player_bid):
   already_trans = []
   for trans in list_of_player_bid:
      trans = int(trans)
      already_trans.append(trans)
   return already_trans

player_bid = input("Enter All Bid : ").split(" ")

player_bid_in_int = trans_to_int(player_bid)

first_biggest_bid = 0
second_biggest_bid = 0
temp = 0

if len(player_bid) < 2:
   print("not enough bidder")
else:
   for i in range(0,len(player_bid_in_int)):
      if player_bid_in_int[i] > temp:
         temp = player_bid_in_int[i]
         if i == 0:
            first_biggest_bid = temp
         elif first_biggest_bid < temp:
            second_biggest_bid = first_biggest_bid
            first_biggest_bid = temp
      elif player_bid_in_int[i] > second_biggest_bid:
         second_biggest_bid = player_bid_in_int[i]
         
   count_higest = 0
   for i in player_bid_in_int:
      if i == first_biggest_bid:
         count_higest += 1
   if count_higest > 1:
      print("error : have more than one highest bid")
   else:
      print(f"winner bid is {first_biggest_bid} need to pay {second_biggest_bid}")