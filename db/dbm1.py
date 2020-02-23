import dbm  #Import Get DBM implementation
file=dbm.open('filename', 'c') # Open Create or open an existing DBM file for I/O
file['key'] = 'value'  #Store Create or change the entry for key
value = file['key'] #Fetch Load the value for the entry key
count = len(file) #Size Return the number of entries stored
index = file.keys() #Index Fetch the stored keys list (not a view)
found = 'key' in file #Query See if there’s an entry for key
del file['key'] #Delete Remove the entry for key
for key in file: #Iterate Iterate over stored keys
file.close() #Close Manual close, not always needed