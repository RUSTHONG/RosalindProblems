import sets  
magic_char = sets.Set('ATTAGACCTG')  
poppins_chars = sets.Set('CCTGCCGGAA')  
print ''.join(magic_char & poppins_chars)   #InterSection  
print ''.join(magic_char | poppins_chars)