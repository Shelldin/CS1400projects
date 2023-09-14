# total crew number input
pirates_string = "How many pirates:"
print(pirates_string)
crew_size = int(input(""))

print('')

# total units input
units_string = "How many units:"
print(units_string)
total_units = int(input(""))

# Yondu give the crew 3 units a piece before divvying out the plunder
crew_initial_share = 3 * (crew_size - 2)

# Yondu takes 13% of the remaining amount
yondu_first_share = round((total_units - crew_initial_share) * 0.13, 2)

# Peter gets 11% of the amount remaining after Yondu's cut
peter_first_share = round((total_units - crew_initial_share - yondu_first_share) * 0.11, 2)

# The remaining amount after Yondu's and Peter's initial cuts is divided equal with everyone
crew_share = round((total_units - crew_initial_share - yondu_first_share - peter_first_share) / crew_size, 2)

# each crew member's share after everything has been divided after initial cuts
yondu_total_share = yondu_first_share + crew_share
peter_total_share = peter_first_share + crew_share
other_crew_total_share = 3 + crew_share

yondu_string = "Yondu's Share: "
peter_string = "Peter's Share: "
crew_string = "Crew's share: "

# print the number of crew and units, as well as the final shares that will be received
print('')
print(f"Yondu's Share: {yondu_total_share :,.2f}")
print(f"Peter's Share: {peter_total_share :,.2f}")
print(f"Crew's Share: {other_crew_total_share:,.2f}")
