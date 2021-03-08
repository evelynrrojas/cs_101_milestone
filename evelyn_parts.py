# question 2
def dna2rna(dna):
    rna = dna.replace('T', 'U')
    return rna.strip()

# question 4
def mendels_law(hom, het, rec):
    pop_total = hom + het + rec
    ress = (het/pop_total) * (rec - 1)/(pop_total - 1)
    het_ress = (het/pop_total) * het/(pop_total - 1) * 0.5
    ress_het = (rec/pop_total) * het/(pop_total - 1) * 0.5
    het_het = het/pop_total * (het - 1)/(pop_total -1) * 0.25

    return (1 - (ress + het_ress + ress_het + het_het))

print (mendels_law (2, 2, 2))

# question 5
def fibonacci_rabbits(n ,k):
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        return fibonacci_rabbits(n - 1, k) + k * fibonacci_rabbits(n - 2, k)
print (fibonacci_rabbits (5, 3))
