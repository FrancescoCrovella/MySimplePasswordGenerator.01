
#Developer: Francesco_Crovella

#This script is aimed at creating random 16 characters password.

#------------------------------README------------------------------#

    # The necessary steps to use this script are the following:

        # 1- open cmd prompt in Windows
        # 2- move to the directory Folder in which the .py file is saved by using this command: <cd Folder1\Folder2\Folder3>
        # 3- run the .py file by using this command: <python3 script_MySimplePasswordGenerator_01.py>

#------------------------------README------------------------------#






#------------------------------SOURCE CODE------------------------------#

import random

lower_characters='abcdefghijklmnopqrstuvwxyz'
upper_characters='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
special_characters='|!""£$%&/()=?^ìéè*+[]çò@°à#§ù'
numeric_characters='1234567890'

# For generating a random password we can use the python INBUILT FUNCTION of RANDOM MODULE called SAMPLE

# <random.sample(sequenceListString,k-sampleLenght)>

# This function is aimed at creating the list of k-random characters

password_structure=(lower_characters)+(upper_characters)+(special_characters)+(numeric_characters)

password_lenght=16

password_characters_list=random.sample(password_structure,password_lenght)

# Now we can merge/join all the list characters in a single joined string by using the INBUILT FUNCTION called JOIN

# <string.join()>

password=''.join(password_characters_list)

print(password)

#------------------------------SOURCE CODE------------------------------#