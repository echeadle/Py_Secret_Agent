from collections import defaultdict
corpus_file = "/usr/share/dict/words"
digram_count = defaultdict( int )
with open(corpus_file, "r") as corpus:
    for line in corpus:
        word= line.lower().strip()
        for position in range(len(word)-1):
            digram= word[position:position+2]
            digram_count[digram] += 1


#oprint(digram_count)

from collections import Counter
corpus_file = "/usr/share/dict/words"
digram_count = Counter()
with open(corpus_file, "r") as corpus:
    for line in corpus:
        word= line.lower().strip()
        for position in range(len(word)-1):
            new_word= word[position:position+2]
            if "'" not in new_word:
                digram= new_word    
                digram_count[digram] += 1

print( digram_count.most_common( 10 ) )
print(f"\n\nThe WINNER diagram is: {digram_count.most_common( 1 )}")

total = sum(digram_count.values() )
for digram, count in digram_count.items():
    print( "{:2s} {:7d} {:.3%}".format(digram, count, count/total) )
