import re
from collections import namedtuple

if __name__ == '__main__':
    file_name='/Users/gowthamkannan/Desktop/interview questions.txt'
    words=re.findall(r'\w+',open(file_name).read().lower())
    # Counter(words).most_common(10)
    print (collections.Counter(['a', 'b', 'c', 'a', 'b', 'b']))
    # Point=namedtuple('Point')
    # p_1=Point(11,10)
    # print (p_1)