# total crew number and units input
pirates_string = "How many pirates:"
pirates_int = 20

units_string = "How many units:"
units_int = 1000

# Yondu give the crew 3 units a piece before divvying out the plunder
crew_initial_share = 3 * (pirates_int - 2)

# Yondu takes 13% of the remaining amount
yondu_first_cut = round((units_int - crew_initial_share) * 0.13, 2)

# Peter gets 11% of the amount remaining after Yondu's cut
peter_first_cut = round((units_int - crew_initial_share - yondu_first_cut) * 0.11, 2)

# The remaining amount after Yondu's and Peter's initial cuts is divided equal with everyone
crew_share = round((units_int - crew_initial_share - yondu_first_cut - peter_first_cut) / pirates_int, 2)

# each crew member's share after everything has been divided after initial cuts
yondu_total_share = yondu_first_cut + crew_share
peter_total_share = peter_first_cut + crew_share
other_crew_total_share = 3 + crew_share

yondu_string = "Yondu's Share: "
peter_string = "Peter's Share: "
crew_string = "Crew's share: "

# print the number of crew and units, as well as the final shares that will be received
print(pirates_string, '\n', pirates_int)
print(units_string, '\n', units_int)
print('')
print(yondu_string + "{:.2f}".format(yondu_total_share))
print(peter_string + "{:.2f}".format(peter_total_share))
print(crew_string + "{:.2f}".format(other_crew_total_share))

