'''Python Program to Delete Specific Line from File
'''
# deleting a line
# based on the position

# opening the file in
# reading mode

try:
    with open('months.txt', 'r') as fr:
        # reading line by line
        lines = fr.readlines()
        
        # pointer for position
        ptr = 1
    
        # opening in writing mode
        with open('months.txt', 'w') as fw:
            for line in lines:
              
                # we want to remove 5th line
                if ptr != 5:
                    fw.write(line)
                ptr += 1
    print("Deleted")
    
except:
    print("Oops! something error")