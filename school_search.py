# -*- coding: utf-8 -*-
"""
Created on Tue Jan 21 23:07:27 2020

@author: Chaitali
"""

import  csv, time, os

def search_schools():
    t1 = time.time()
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'sl051bai.csv')
    find_school = input()
    school_len = len(find_school.split(" "))
    matching_school = dict()
    #filename = os.path.join(dirname, 'abc.csv')
    with open(filename,'r', encoding='mac_roman') as f:
        csv_reader = csv.reader(f)
        next(csv_reader, None)
        included_cols = [3,4,5]
        #data = [tuple(line[i]) for i in [3,4,5] for line in csv_reader]
        for row in csv_reader:
            data = tuple(row[i] for i in included_cols)
            #print(data[0], data[0].split(" "))
            #return
            score = match_school(data[0], find_school)
            #print(type(matching_school))
            if score > 0:
                matching_school[data] = score
            matching_school = dict(sorted(matching_school.items(), key = lambda kv: kv[1], reverse = True))
            if len(matching_school) > 2 and list(matching_school.values())[0] >= school_len:
                break

    t2 = time.time()
    t = (t2 - t1) / 1000
    print('Results for "{}" (search took: {}s)'.format(find_school, t))
    limit = 3 if 3 < len(matching_school) else len(matching_school)
    for i in range(limit):
        print("{}. {}".format(i+1, list(matching_school.keys())[i][0]))
        print("{}, {}".format(list(matching_school.keys())[i][1], list(matching_school.keys())[i][2]))
            


def match_school(given_school, target_school):
    score = 0
    if given_school.casefold() == target_school:
        score = len(target_school.split(" ")) +1

    else:
        #print(given_school.split(" ")) 
        for x in given_school.split(" "):
            #print(x)
            if x.strip().casefold() in target_school.split(" "):
                #print(x.strip())
                score += 1
    #print(given_school, score)
    
    return score


if __name__=="__main__":
    search_schools()
    #match_school("HIGHLAND PARK ELEMENTARY SCHOOL", "elementary school highland park")





'''
elementary school highland park
>>> school_search.search_schools("elementary school highland park")
Results for "elementary school highland park" (search took: 0.009s)
1. HIGHLAND PARK ELEMENTARY SCHOOL
MUSCLE SHOALS, AL
2. HIGHLAND PARK ELEMENTARY SCHOOL
PUEBLO, CO
3. [Next Best Hit]
jefferson belleville
>>> school_search.search_schools("jefferson belleville")
Results for "jefferson belleville" (search took: 0.000s)
1. JEFFERSON ELEM SCHOOL
BELLEVILLE, IL
2. [Next Best Hit]
3. [Next Best Hit]
riverside school 44
>>> school_search.search_schools("riverside school 44")
Results for "riverside school 44" (search took: 0.002s)
1. RIVERSIDE SCHOOL 44
INDIANAPOLIS, IN
2. [Next Best Hit]
3. [Next Best Hit]
granada charter school
>>> school_search.search_schools("granada charter school")
Results for "granada charter school" (search took: 0.001s)
1. NORTH VALLEY CHARTER ACADEMY
GRANADA HILLS, CA
2. GRANADA HILLS CHARTER HIGH
GRANADA HILLS, CA
3. [Next Best Hit]
foley high alabama
>>> school_search.search_schools("foley high alabama")
Results for "foley high alabama" (search took: 0.001s)
1. FOLEY HIGH SCHOOL
FOLEY, AL
2. [Next Best Hit]
3. [Next Best Hit]
KUSKOKWIM
>>> school_search.search_schools("KUSKOKWIM")
Results for "KUSKOKWIM" (search took: 0.001s)
1. TOP OF THE KUSKOKWIM SCHOOL
NIKOLAI, AK
(No additional results should be returned)
'''
