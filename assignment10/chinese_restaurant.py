import random
import json

def generateChineseRestaurant(customers):
    # First customer always sits at the first table
    tables = [1]
    #for all other customers do
    for cust in range(2, customers+1):
            # rand between 0 and 1
            rand = random.random()
            # Total probability to sit at a table
            prob = 0
            # No table found yet
            table_found = False
            # Iterate over tables
            for table, guests in enumerate(tables):
                # calc probability for actual table an add it to total probability
                prob += guests / (cust)
                # If rand is smaller than the current total prob., customer will sit down at current table
                if rand < prob:
                    # incr. #customers for that table
                    tables[table] += 1
                    # customer has found table
                    table_found = True
                    # no more tables need to be iterated, break out for loop
                    break
            # If table iteration is over and no table was found, open new table
            if not table_found:
                tables.append(1)
    return tables


restaurants = [200,400,600,800,1000]
#print(restaurants)

single_simulation_data = []
final_simulation_data = []
for i in range(5):
    for customers in restaurants:
        network = generateChineseRestaurant(customers)
        single_simulation_data.append(network)
    #with open('network_' + str(customers) + '.json', 'w') as out:
    final_simulation_data.append(single_simulation_data)
    single_simulation_data = []

with open('network_' + str(customers) + '.json', 'w') as out:
    json.dump(final_simulation_data, out)