#First I open the file with read permissions
with open('two_cities_ascii.txt', 'r') as file:
    contents = file.read()

#At this point I convert the contents of the file to their ASCII number euqivalents
converter = [ord(ele) for sub in contents for ele in sub]

#At this point I make the necessary subtractions in order to find the mirror equivalent 
mirror = [255-x for x in converter]

#At this point I create the mirror output
mirror_output = ''.join(chr(int(x)) for x in mirror)

#At this point i use the length of the mirror_output to mirror the output itself
length = len(mirror_output)
backward_file = mirror_output[length::-1]

#I print the mirrored_output to the user
print(backward_file)
