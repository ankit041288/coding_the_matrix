filePath = ('resources/Data/voting_record_dump109.txt')
import sys

# Reading the file
with open(filePath) as fp :
    line = fp.readline()
    count=1
    while line :
        print("Line {} : {}".format(count,line.strip()))
        line = fp.readline()
        count+=1


# Method for dot_product of each list from file

def dot_product(a,b):
        return sum(int(a[d])*int(b[d]) for d in range(len(a)))


# create a dict with senator name as key
def create_voting_dict():
    res ={}
    with open(filePath) as fp:
        line = fp.readline()
        while line:
            l = line.split( );
            res[l[0]]=l[3:]
            line = fp.readline()
    return res


data_map=create_voting_dict()


# Comparing senator similarity
def policy_compare(sen_a,sen_b):
    return dot_product(data_map[sen_a],data_map[sen_b])

# policy_compare('Akaka','Alexander')  = 11

def most_similar(sen, d):
    mx=-sys.maxsize -1
    res=""
    for sen_b in d.keys():
        l = policy_compare(sen,sen_b) if sen_b!=sen else -sys.maxsize -1
        res = sen_b if(l>mx) else res
        mx = max(mx,l)
    return res

def least_similar(sen, d):
    mx=sys.maxsize
    res=""
    for sen_b in d.keys():
        l = policy_compare(sen,sen_b) if sen_b!=sen else sys.maxsize
        res = sen_b if(l<mx) else res
        mx = min(mx,l)
    return res


least_similar('Akaka',data_map)