import random as r

def generate_seq():
    s = ''
    p1 = 'ggcca'
    p2 = 'cccag'

    for i in range(0, 5):
        b = r.randint(1, 4)
        if b == 1:
            s += 'a'
        elif b == 2:
            s += 'c'
        elif b == 3:
            s += 'g'
        elif b == 4:
            s += 't'
        
    flag = False
            
    if r.randint(0, 100) < 75:    
        s += p1
        flag = True

    for i in range(0, 5):
        b = r.randint(1, 4)
        if b == 1:
            s += 'a'
        elif b == 2:
            s += 'c'
        elif b == 3:
            s += 'g'
        elif b == 4:
            s += 't'
        
    
    tmp = r.randint(0, 100)    
    if not flag:
        s += p2
    elif tmp > 25:
        s += p2

    for i in range(0, 5):
        b = r.randint(1, 4)
        if b == 1:
            s += 'a'
        elif b == 2:
            s += 'c'
        elif b == 3:
            s += 'g'
        elif b == 4:
            s += 't'
    return s


out = open('seqs.fasta', 'a')
for i in range(0,100):
    out.write('>Sequence_' + str(i) + '\n')
    out.write(generate_seq() + '\n')