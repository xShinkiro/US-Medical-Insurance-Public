# U.S. Medical Insurance 

# Look over your dataset
# Open insurance.cvs and take a look at the file. Take note of how information is organized.
# How will this affect how you analyze the data in Python?
# Is there anything of particular interest to you in the dataset that you want to investigate?
# Think about these things before you jump into Python.

import csv

insurance_ls = []
age = []
sex = []
bmi =  []
children = []
smoker = []
region = []
charges = []

with open('insurance.csv') as insurance:
    rows = csv.DictReader(insurance)
    for i in rows:
        insurance_ls.append(i)

# print(insurance_ls)
# print(insurance_ls[-1]['charges'])

#to find the total and average for each numeric column and create seperate list of each fieldname
num_of_insurees = 0
sum_of_ages = 0
total_charges = 0
sum_of_bmi = 0
sum_of_children = 0
max_charge = 0
max_age = 0


for i in range(len(insurance_ls)):
        total_charges += float(insurance_ls[i]['charges'])
        sum_of_ages += int(insurance_ls[i]['age'])
        sum_of_bmi+= float(insurance_ls[i]['bmi'])
        sum_of_children += int(insurance_ls[i]['children'])
        num_of_insurees += 1
        
        charges.append(float(insurance_ls[i]['charges']))
        age.append(insurance_ls[i]['age'])
        bmi.append(insurance_ls[i]['bmi'])
        sex.append(insurance_ls[i]['sex'])
        region.append(insurance_ls[i]['region'])
        smoker.append(insurance_ls[i]['smoker'])
        children.append(insurance_ls[i]['children'])

# Thinking about focusing the differences in charges thought I would include highest and lowest charges to go with the average. 
 
        if float(insurance_ls[i]['age']) > float(max_age):
           max_age = round(float(insurance_ls[i]['age']),2)
        if float(insurance_ls[i]['charges']) > float(max_charge):
           max_charge = round(float(insurance_ls[i]['charges']),2)
lowest_age = max_age
for i in range(len(insurance_ls)):       
  if float(insurance_ls[i]['age']) < float(lowest_age):
           lowest_age = round(float(insurance_ls[i]['age']),2)       
lowest_charge = max_charge
for i in range(len(insurance_ls)):       
  if float(insurance_ls[i]['charges']) < float(lowest_charge):
           lowest_charge = round(float(insurance_ls[i]['charges']),2)       
  

avg_age = round(sum_of_ages/len(insurance_ls))
avg_bmi = round(sum_of_bmi/len(insurance_ls), 3)
avg_num_children = round(sum_of_children/len(insurance_ls))
avg_charge =  round(total_charges/len(insurance_ls), 2)


print('Number of people insured are', num_of_insurees, '.')

print('The highest charge is', max_charge, 'and the lowest charge is', lowest_charge, 'and the average of all charges is', avg_charge)

print('The highest age is', max_age, 'and the lowest age is', lowest_age, 'and the average of all ages is', avg_age)

print("Based on the numeric columns the average of each are: Average age - " + str(avg_age) + ' Average BMI - '
       + str(avg_bmi) + ' Average number of children - ' + str(avg_num_children) + ' Average charge - ' + str(avg_charge) + '.')

# print(round(total_charges, 2))

# Charges based on region and regional 
southwest_charges_ls = []
southeast_charges_ls = []
northwest_charges_ls = []
northeast_charges_ls = []
southwest_ls = []
southeast_ls = []
northwest_ls = []
northeast_ls = []
regional_dict = {'southwest' : southwest_ls,'southeast' : southeast_ls,'northwest' : northwest_ls,'northeast' : northeast_ls }
regional_charges = {'southwest' : southwest_charges_ls,'southeast' : southeast_charges_ls,'northwest' : northwest_charges_ls,'northeast' : northeast_charges_ls } 

def count_per_region(dict):
        southwest_c = 0
        southeast_c = 0
        northwest_c = 0
        northeast_c = 0
        for i in range(len(dict)):
              if dict[i]['region'] == 'southwest':
                southwest_c += 1
                southwest_charges_ls.append(dict[i]['charges'])
                southwest_ls.append(dict[i])
              elif  dict[i]['region'] == 'southeast':
                southeast_c += 1
                southeast_charges_ls.append(dict[i]['charges'])
                southeast_ls.append(dict[i])
              elif dict[i]['region'] == 'northwest':
                northwest_c += 1
                northwest_charges_ls.append(dict[i]['charges'])
                northwest_ls.append(dict[i])  
              elif dict[i]['region'] == 'northeast':
                northeast_c += 1
                northeast_charges_ls.append(dict[i]['charges'])
                northeast_ls.append(dict[i])
              else:
                  continue 
              
        return print('Amount of  insurees in southwest is', southwest_c, 'and in the southeast is', str(southeast_c) + ', and in the northwest is', str(northwest_c),'and in the north east is',  str(northeast_c))
count_per_region(insurance_ls)
# print(southeast_ls)

#to find the most expensive region for insurance                                

def most_expensive(regional_charges):
    r_one_sum =0
    r_two_sum = 0
    r_three_sum = 0
    r_four_sum = 0
    the_expensive = 0
    for i in regional_charges['southwest']:
        r_one_sum += float(i)
    for i in regional_charges['southeast']:
        r_two_sum += float(i)
    for i in regional_charges['northwest']:
        r_three_sum += float(i)
    for i in regional_charges['northeast']:
        r_four_sum += float(i)

    if r_one_sum > r_two_sum and r_one_sum > r_three_sum and r_one_sum > r_four_sum:
      the_expensive = r_one_sum
      region = list(regional_charges.keys())[0]
    elif r_two_sum > r_one_sum and r_two_sum > r_three_sum and r_two_sum > r_four_sum:
      the_expensive = r_two_sum
      region = list(regional_charges.keys())[1]
    elif r_three_sum > r_one_sum and r_three_sum > r_two_sum and r_three_sum > r_four_sum:
      the_expensive = r_three_sum
      region = list(regional_charges.keys())[2]
    elif r_four_sum > r_three_sum and r_four_sum > r_two_sum and r_four_sum > r_one_sum:
      the_expensive = r_four_sum
      region = list(regional_charges.keys())[3]
    else:
       pass
    
    #by average
    r_one_avg =  r_one_sum/ len(regional_charges['southwest'])
    r_two_avg = r_two_sum/len(regional_charges['southeast'])
    r_three_avg = r_three_sum/len(regional_charges['northwest'])
    r_four_avg = r_four_sum/len(regional_charges['northeast'])
    
    if r_one_avg > r_two_avg and r_one_avg > r_three_avg and r_one_avg > r_four_avg:
      avg_most_expensive = r_one_avg
      region2 = list(regional_charges.keys())[0]
    elif r_two_avg > r_one_avg and r_two_avg > r_three_avg and r_two_avg > r_four_avg:
      avg_most_expensive = r_two_avg
      region2 = list(regional_charges.keys())[1]
    elif r_three_avg > r_one_avg and r_three_avg > r_two_avg and r_three_avg > r_four_avg:
      avg_most_expensive = r_three_avg
      region2 = list(regional_charges.keys())[2]
    elif r_four_avg > r_three_avg and r_four_avg > r_two_avg and r_four_avg > r_one_avg:
      avg_most_expensive = r_four_avg
      region2 = list(regional_charges.keys())[3]
    else:
       pass
  
  
    return print('The most expensive region is', region, 'at a total of', round(the_expensive,2), 'by average it is', region2, round(avg_most_expensive,2))
      

most_expensive(regional_charges)


def least_expensive(regional_charges):
    r_one_sum =0
    r_two_sum = 0
    r_three_sum = 0
    r_four_sum = 0
    least_expensive = 0
    for i in regional_charges['southwest']:
        r_one_sum += float(i)
    for i in regional_charges['southeast']:
        r_two_sum += float(i)
    for i in regional_charges['northwest']:
        r_three_sum += float(i)
    for i in regional_charges['northeast']:
        r_four_sum += float(i)

    if r_one_sum < r_two_sum and r_one_sum < r_three_sum and r_one_sum < r_four_sum:
      least_expensive = r_one_sum
      region = list(regional_charges.keys())[0]
    elif r_two_sum < r_one_sum and r_two_sum < r_three_sum and r_two_sum < r_four_sum:
      least_expensive = r_two_sum
      region = list(regional_charges.keys())[1]
    elif r_three_sum < r_one_sum and r_three_sum < r_two_sum and r_three_sum < r_four_sum:
      least_expensive = r_three_sum
      region = list(regional_charges.keys())[2]
    elif r_four_sum < r_three_sum and r_four_sum < r_two_sum and r_four_sum < r_one_sum:
      least_expensive = r_four_sum
      region = list(regional_charges.keys())[3]
    else:
       pass
    
    #by average
    r_one_avg =  r_one_sum/ len(regional_charges['southwest'])
    r_two_avg = r_two_sum/len(regional_charges['southeast'])
    r_three_avg = r_three_sum/len(regional_charges['northwest'])
    r_four_avg = r_four_sum/len(regional_charges['northeast'])
    
    if r_one_avg < r_two_avg and r_one_avg < r_three_avg and r_one_avg < r_four_avg:
      avg_least_expensive = r_one_avg
      region_avg = list(regional_charges.keys())[0]
    elif r_two_avg < r_one_avg and r_two_avg < r_three_avg and r_two_avg < r_four_avg:
      avg_least_expensive = r_two_avg
      region_avg = list(regional_charges.keys())[1]
    elif r_three_avg < r_one_avg and r_three_avg < r_two_avg and r_three_avg < r_four_avg:
      avg_least_expensive = r_three_avg
      region_avg = list(regional_charges.keys())[2]
    elif r_four_avg < r_three_avg and r_four_avg < r_two_avg and r_four_avg < r_one_avg:
      avg_least_expensive = r_four_avg
      region_avg = list(regional_charges.keys())[3]
    else:
       pass
  
    return print('The least expensive region is', region, 'at a total of', round(least_expensive,2), 'by average it is', region_avg, round(avg_least_expensive,2))



least_expensive(regional_charges) 
male_ls = []
female_ls= []

def male_vs_female_count(dict):
  male_c = 0
  female_c = 0
  for i in range(len(dict)):
    if dict[i]['sex'] == 'male':
      male_c += 1
      male_ls.append(dict[i])
    elif  dict[i]['sex'] == 'female':
      female_c += 1
      female_ls.append(dict[i])
    else:
      pass
            
  return print('Male count is', male_c, 'representing',  ("{:.2%}".format(male_c/num_of_insurees)), 'vs the female count of', female_c, 'representing',  ("{:.2%}".format(female_c/num_of_insurees)) + '.')


male_vs_female_count(insurance_ls)
male_vs_female_dict= {'male' : male_ls, 'female' : female_ls}

def male_vs_female_charges(male_vs_female_dict):
   total_male_charges = 0
   total_female_charges = 0
   for i in male_vs_female_dict['male']:
    total_male_charges += float(i['charges'])
   for i in male_vs_female_dict['female']:
    total_female_charges += float(i['charges'])
         
   avg_male_charge = total_male_charges/len(male_vs_female_dict['male'])
   avg_female_charge = total_female_charges/len(male_vs_female_dict['female']) 

   return print('The males are charged a total of ', round(total_male_charges,2), 'with an average of',  round(avg_male_charge,2), 'per male, and women are charged a total of', round(total_female_charges,2), 'with an average of', round(avg_female_charge,2), 'per female') 

male_vs_female_charges(male_vs_female_dict)
#print(insurance_ls)

with_one_child_ls = []
no_child_ls = []
more_than_one_ls = []
total_with_children_ls = []


def child_or_not(dict):
   with_one_child = 0
   no_child = 0
   more_than_one = 0
   
  
   for i in range(len(dict)):
    if dict[i]['children'] == '0':
      no_child += 1
      no_child_ls.append(dict[i])
    elif dict[i]['children'] == '1':
      with_one_child += 1
      with_one_child_ls.append(dict[i])
      total_with_children_ls.append(dict[i])
    else:
      more_than_one += 1
      more_than_one_ls.append(dict[i])
      total_with_children_ls.append(dict[i])
   total_with_children = with_one_child + more_than_one
   
   return print('Amount of inurees with children', total_with_children, 'amount with more than one is', more_than_one,  'amount with just one child', with_one_child, ' and with no children are', no_child), total_with_children_ls, with_one_child_ls, no_child_ls, more_than_one_ls

child_or_not(insurance_ls)

child_or_not_dict = {'no child' : no_child_ls,'with one child' : with_one_child_ls, 'more than one' : more_than_one_ls, 'total with children' : total_with_children_ls }

def price_vs_child_or_not(child_or_not_dict):
  no_child_charges_total = 0
  with_one_child_charges_total = 0
  more_than_one_charges_total  = 0
  total_with_children_charges_total = 0

  for i in child_or_not_dict['no child']:
    no_child_charges_total += float(i['charges'])
  for i in child_or_not_dict['with one child']:
    with_one_child_charges_total += float(i['charges'])      
  for i in child_or_not_dict['more than one']:
    more_than_one_charges_total += float(i['charges'])
  for i in child_or_not_dict['total with children']:
    total_with_children_charges_total += float(i['charges'])
  
  no_child_avg = round(no_child_charges_total/len(child_or_not_dict['no child']),2)
  with_one_child_avg = round(with_one_child_charges_total/len(child_or_not_dict['with one child']),2)
  more_than_one_avg = round(more_than_one_charges_total/len(child_or_not_dict['more than one']),2)
  total_with_children_avg = round(total_with_children_charges_total/len(child_or_not_dict['total with children']),2)

  return print('Total charges with no children:', round(no_child_charges_total,2),'with an average of', no_child_avg, 'Total charges with one child:', round(with_one_child_charges_total,2), 'with an average of', with_one_child_avg, 'Total charges with more than one child', round(more_than_one_charges_total,2), 'with an average of', more_than_one_avg, 'Total charges with all that have children are:', round(total_with_children_charges_total,2), 'with an average of', total_with_children_avg) 

price_vs_child_or_not(child_or_not_dict)
print('The highest charge is', max_charge, 'and the lowest charge is', lowest_charge, 'and the average of all charges is', avg_charge)
#print(male_vs_female_dict)