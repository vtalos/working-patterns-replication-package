import json
import datetime

with open('results.json', 'r', encoding='utf-8') as file:
    data = json.load(file)
repos = data['items']
ages = []
not_counted = 0
for repo in repos:
    created_at = datetime.datetime.strptime(repo['createdAt'], '%Y-%m-%dT%H:%M:%S')
    updated_at = datetime.datetime.strptime(repo['lastCommit'], '%Y-%m-%dT%H:%M:%S')
    age = updated_at - created_at
    # if age is negative, do not include in calculations. 
    # That can be attributed to GHSearch misscalculation 
    # or migration from other version control system to Github.
    if age.days/365 <= 0:
        not_counted += 1
        continue
    else:
        ages.append(age.days/365)
average_age = sum(ages) / len(ages)
print(f'Not counted repos: {not_counted}')
std = (sum((x - average_age) ** 2 for x in ages) / len(ages)) ** 0.5
print(f'Average age: {average_age:.2f} years')
print(f'Standard deviation: {std:.2f} years')