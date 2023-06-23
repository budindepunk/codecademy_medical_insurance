# # U.S. Medical Insurance Costs

# %%
import csv

# %%
ages = []
sexes = []
bmis = []
num_children = []
smoker_statuses = []
regions = []
insurance_charges = []

# %%
# open the csv file in context and add the data to the appropriate list
with open("insurance.csv") as insurance_csv:
    insurance_dict = csv.DictReader(insurance_csv)
    for row in insurance_dict:
        ages.append(row["age"])
        sexes.append(row["sex"])
        bmis.append(row["bmi"])
        num_children.append(row["children"])
        smoker_statuses.append(row["smoker"])
        regions.append(row["region"])
        insurance_charges.append(row["charges"])

# %%
# create a dictionary with the patient data
keys = ["ages", "sexes", "bmis", "num_children", "smoker_statuses", "regions", "insurance_charges"]
values = [ages, sexes, bmis, num_children, smoker_statuses, regions, insurance_charges]
data_dictionary = dict(zip(keys, values))

# %%
# find average age
total_age = 0
for age in ages:
    total_age += int(age)
average_age = round(total_age / len(ages), 1)
print("the average age in the dataset is {} years".format(str(average_age)))

# %%
# find average age with at least 1 child and average number of children among people with children
total_age_child = 0
for i in range(0, len(ages)):
    if int(num_children[i]) > 0:
        total_age_child += int(ages[i])
avg_age_child = round(total_age_child / len(ages), 1)

total_parents = 0
total_children = 0
for i_str in num_children:
    i = int(i_str)
    if i > 0:
        total_parents += 1
        total_children += i
avg_children = round(total_children / total_parents, 1)
print("the average age for someone with children is {} years and the average amount of children is {}".format(avg_age_child, avg_children))

# %%
# find number of males and females in the dataset
males = 0
females = 0
other = 0
for i in sexes:
    if i.lower() == "male":
        males += 1
    elif i.lower() == "female":
        females += 1
    else:
        others += 1
print("there are {} men, {} women and {} others in this dataset".format(males, females, other))

# %%
# calculate average cost of insurance
total_cost = 0
for i in insurance_charges:
    total_cost += float(i)
avg_cost = round(total_cost / len(insurance_charges), 2)
print("the average cost of insurance in this dataset is {} dollars".format(avg_cost))

# %%
# creates a dictionary with each unique region and its number of occurrences
unique_regions = []
for region in regions:
    if region not in unique_regions:
        unique_regions.append(region)

region_occurrences = {}
for i in range(0, len(unique_regions)):
    counter = 0
    for region in regions:
        if region == unique_regions[i]:
            counter += 1
    region_occurrences[unique_regions[i]] = counter

# this one checks if a pair in the new dictionary is the one with the highest value and prints its info (most common area)
search = max(region_occurrences.values())
for key, value in region_occurrences.items(): 
    if value == search:
        print("the region with most occurrences is {} and appears {} times in this dataset".format(key, value))


# %%
# finds number of smokers and nonsmokers
smokers = 0
for i in smoker_statuses:
    if i.lower() == "yes":
        smokers += 1
print("{} people in this dataset are smokers".format(smokers))


