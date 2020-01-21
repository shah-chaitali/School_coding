import  csv, time, itertools, os

def print_counts():
    dirname = os.path.dirname(__file__)
    filename = os.path.join(dirname, 'sl051bai.csv')
    #filename = os.path.join(dirname, 'abc.csv')
    with open(filename,'r', encoding='mac_roman') as f:
        csv_reader = csv.reader(f)
        next(csv_reader, None)
        data = [tuple(line) for line in csv_reader]

    #print(data[:10])
    total_school = len(set([row[3] for row in data]))
    print("Total Schools:", total_school)
    
    print("......")
    print("Schools by State:")
    for key, group in itertools.groupby(sorted(data, key =  lambda y: y[5]), lambda x: x[5]):
        total_school = len(set([row[3] for row in group]))
        print("{}: {}".format(key,total_school))

    print("......")
    print("Schools by Metro-centric locale:")
    for key, group in itertools.groupby(sorted(data, key =  lambda y: y[8]), lambda x: x[8]):
        total_school = len(set([row[3] for row in group]))
        print("{}: {}".format(key,total_school))

    print("......")
    city_school =dict()
    for key, group in itertools.groupby(sorted(data, key =  lambda y: y[4]), lambda x: x[4]):
        city_school[key] = len(set([row[3] for row in group]))
    result = sorted(city_school.items(), key = lambda kv: (kv[1], kv[0]), reverse=True)		
    print("City with most schools: {} ({} schools)".format(result[0][0],result[0][1]))
    #print(result[-1])
    #print(len(result))
    print("......")
    city_count = len(list(filter(lambda x: x[1] > 0, result)))
    print("Unique cities with at least one school: {}".format(city_count))








if __name__=="__main__":
    print_counts()





"""
>>> count_schools.print_counts()
Total Schools: 10000
Schools by State:
CO: 1000
DC: 200
AK: 600
DE: 300
AL: 1500
AR: 1100
...
Schools by Metro-centric locale:
1: 3000
3: 2000
2: 5000
5: 300
...
City with most schools: CHICAGO (50 schools)
Unique cities with at least one school: 1000
"""
