final = []
seq = 'TATTAACCGGGTTTAAACTAGCATGCATGATTAACCAGTACATCTTTT'
for i in seq:
    if i == 'T':
        final.append('A')
    elif i == 'A':
        final.append('T')
    elif i == 'C':
        final.append('G')
    else:
        final.append('C')

final.reverse()

seq_compl = ''

for i in final:
    seq_compl += i
print('The reverse complementary sequence is: {}'.format(seq_compl))
