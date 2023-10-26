def DNA_strand(dna_specimen):
	p = 0
	rdna = ''
	while p < len(dna_specimen):
		if dna_specimen[p] == 'A': rdna = rdna + 'T'
		elif dna_specimen[p] == 'T': rdna = rdna + 'A'
		elif dna_specimen[p] == 'C': rdna = rdna + 'G'
		elif dna_specimen[p] == 'G': rdna = rdna + 'C'
		p += 1
	return rdna