#from numpy import insert


#counties = ["Arapahoe", "Denver", "Jefferson"]
#counties.insert(1,"El Paso")
#counties.remove("Arapahoe")
#counties[2] = "Denver"
#counties[1] = "Jefferson"
#counties.append("Arapahoe")

# counties_dict = {}

# counties_dict["Arapahoe"] = 422829
# counties_dict["Denver"] = 463353
# counties_dict["Jefferson"] = 432438

# voting_data = []
# voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
# voting_data.append({"county":"Denver", "registered_voters": 463353})
# voting_data.append({"county":"Jefferson", "registered_voters": 432438})

# voting_data.insert(1, {"county":"El Paso", "registered_voters": 461149})
# voting_data.remove({"county": "Arapahoe", "registered_voters": 422829})
# voting_data[2] = {"county":"Denver", "registered_voters": 463353}
# voting_data.insert(1, {"county":"Jefferson", "registered_voters": 432438})
# voting_data.remove({"county":"Denver", "registered_voters": 463353})
# voting_data.append({"county":"Arapahoe", "registered_voters": 422829})


# print(voting_data)

# counties = ["Arapahoe","Denver","Jefferson"]

# if counties[3] != 'Jefferson':

#     print(counties[2])

#What is the score?

# score = int(input("What is the score?"))

# if score >= 90:
#     print('Your grade is an A')

# else:

#     if score >= 80:
#         print('Your grade is a B.')
#     else:
#         if score >= 70:
#             print('Your grade is a C.')
#         else:
#             if score >= 60:
#                 print('Your grade is a D.')
#             else:
#                 print('Your grade is an F.')

# if 'El Paso' in counties:

#     print('El Paso is in the list of counties')

# else:

#     print('Nope dummy')

# if 'Arapahoe' in counties or 'El Paso' in counties:

#     print('Yea fool')

# else:
#     print('Lol nahh')

# x= 0

# while x <= 5:
#     print(x)

#     x = x + 1

# counties = ['Arapahoe', 'Denver', 'Jefferson']

# for county in counties:

#     print(county)

# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# for county, voters in counties_dict.items():

#     print(county, "has", str(voters), "registered voters.")

# voting_data = [{"county": "Arapahoe", "registered_voters": 422829},
#                 {"county": "Denver", "registered_voters": 463353},
#                 {"county": "Jefferson", "registered_voters": 432438}]


# for i in range(len(voting_data)):

#       print(voting_data['county'])


# for county_dict in voting_data:

#     for value in county_dict.values():

#         print(value)

# for county_dict in voting_data:
#     print(county_dict['registered_voters'])

# for county, voters in counties_dict.items():

# counties_dict = {"Arapahoe": 369237, "Denver": 413229, "Jefferson": 390222}

# for county, voters in counties_dict.items():

#     print(f"{county} county has {voters:,} registered voters.")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, 
               {"county":"Denver", "registered_voters": 463353}, 
               {"county":"Jefferson", "registered_voters": 432438}]

for county_dict in voting_data:

    print(f"{county_dict['county']} county has {county_dict['registered_voters']:,} registered voters.")

    




