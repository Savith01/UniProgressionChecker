# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID: w1953230

# Date: 13/12/2022

total_crd  = 0 #assigning variables
pass_crd   = 0
defer_crd  = 0
fail_crd   = 0
count_progress = 0
count_trailer = 0
count_exclude = 0
count_NotProgress = 0
count_input = 0
credit_list = []
studentsDict = {}

file = open('Credits.txt','w') #open credits.txt to write down all the creadits entered.


def inputSet(): #defining a function so I can call this function when I need to. and this make it easier to make changes in code.
    global total_crd
    global pass_crd
    global defer_crd
    global fail_crd
    global count_progress 
    global count_trailer 
    global count_exclude
    global count_NotProgress
    global count_input
    global credit_list
    global studentsDict   #from making all the variables global, so all the changes that make within the function will also be change out of the function.  

    
    while True:
        
            studentId = input('\nEnter your Student ID: ') #using a while loop so if user entered a wrong value this will loop back to getting input section, until the user enter the right value.
            studentId = studentId.lower()
            try:
                if studentId[0] != 'w' or len(studentId)!= 8:
                    print('Student ID invalid, Please try again.')
                else:
                    break
            except IndexError:
                print('Student ID invalid, Please try again.')


    while total_crd != 120:
        try:            
            while True:                              
                pass_crd = int(input("\nPlease enter your credit at pass: "))
                if pass_crd > 120 or pass_crd < 0 or pass_crd % 20 != 0:
                    print("Out of range")
                else:
                    break
                
            while True:                
                defer_crd = int(input("Please enter your credit at defer: "))
                if defer_crd > 120 or defer_crd < 0 or defer_crd % 20 != 0:
                    print("Out of range")
                else:
                    break
                                                            
            while True:    
                fail_crd = int(input("Please enter your credit at fail: "))
                if fail_crd > 120 or fail_crd < 0 or fail_crd % 20 != 0:
                    print("Out of range")
                else:
                    break

            total_crd = pass_crd + defer_crd + fail_crd
            if total_crd == 120:
                if pass_crd == 120:
                    print("Progress")
                    count_progress += 1
                    credit_list.append(['Progress - ', pass_crd,', ', defer_crd,', ', fail_crd])
                    studentsDict[studentId] = f'Progress - {pass_crd}, {defer_crd}, {fail_crd}'

                elif pass_crd == 100:
                    print("Progress (Module trailer)")
                    count_trailer += 1
                    credit_list.append(['Progress (Module Trailer) - ', pass_crd,', ', defer_crd,', ', fail_crd])
                    studentsDict[studentId] = f'Porgress (Module Trailer) - {pass_crd}, {defer_crd}, {fail_crd}'

                elif fail_crd >= 80:
                    print("Exclude")
                    count_exclude += 1
                    credit_list.append(['Excluded - ', pass_crd,', ', defer_crd,', ', fail_crd])
                    studentsDict[studentId] = f'Excluded - {pass_crd}, {defer_crd}, {fail_crd}'

                else:
                    print("Do not progress - Module retriever")
                    count_NotProgress += 1
                    credit_list.append(['Module Retriever - ', pass_crd,', ', defer_crd,', ', fail_crd])
                    studentsDict[studentId] = f'Module Retriever - {pass_crd}, {defer_crd}, {fail_crd}'
                count_input += 1
                
            else:
                print('Total incorrect!')
            
            

        except ValueError:
            print("Integer required")
            


print('Hello! Check your progression here')
print('\nSelect the mode that you want to continue') #This is to choose that the user wants to input multiple inputs or simgle input or quit the program.
print('\nStudent mode(One input at a time) --> 1 ')
print('Staff mode (Many inputs at a time) --> 2')
print('Exit --> 3')

MenuChoice = input('\nEnter the number next to the mode to choose the mode: ')
while True:
    if MenuChoice == '1': #single input
        inputSet()
        total_crd = 0
        print('\nSelect the mode that you want to continue')
        print('\nStudent mode(One input at a time) --> 1 ')
        print('Staff mode (Many inputs at a time) --> 2')
        print('Exit --> 3')

        MenuChoice = input('\nEnter the number next to the mode to choose the mode: ')
        
    elif MenuChoice == '2': #multiple inputs
        inputSet()
        total_crd = 0
        print('\nwould you like to enter another set of data?')
        another_set = input("\nif yes press 'y' to enter another set or press 'q' to quit the program and view the histogram: ")

        another_set = another_set.lower()


        while another_set == 'y' :
            inputSet()
            total_crd = 0
                            
            
            print('\nwould you like to enter another set of data?')
            another_set = input("\nif yes press 'y' to enter another set or press 'q' to quit the program and view the histogram: ")
            another_set = another_set.lower()
        else:
            while True:
                if another_set != 'q' and another_set != 'y': #incase of user inputs a invalid input.
                    print('Invalid input')
                    print('\nwould you like to enter another set of data?')
                    another_set = input("\nif yes press 'y' to enter another set or press 'q' to quit the program and view the histogram: ")
                    another_set = another_set.lower()
                
                elif another_set == 'q':
                    print('------------------------------------------------------------------------------') #this is to display the histogram. stars will be printed by multiplying it by progression count 
                    print('***Histogram***')
                    print('\n|Progress',count_progress, ' | ', '*'* count_progress)
                    print('|trailer',count_trailer, '  | ', '*'*count_trailer)
                    print('|Retriever',count_NotProgress, '| ', '*'*count_NotProgress)
                    print('|Excluded',count_exclude, ' | ', '*'*count_exclude)
                    print('\n', count_input,'outcomes in total.')
                    print('------------------------------------------------------------------------------')


                    #part 2 extention

                    print('\nPart : 2') #using a for loop to print out individual elements in credit_list line by line.
                    for e in credit_list:
                        for i in e:
                            print(i, end='')      
                        print()
                        
                    print('------------------------------------------------------------------------------')

                    #part 3 extention.


                    for e in credit_list: #Using for loop for write credits in credits.txt file
                        for i in e:
                            file.write(str(i))
                        file.write('\n')
                        
                    print('Part 3')
                    print('\ncredits have been successfully written on credits.txt')


                    file.close()

                    print('\n')

                    file1 = open('Credits.txt','r')

                    print(file1.read())

                    

                    
                    print('------------------------------------------------------------------------------')

                    #part 4
                    print('Part 4')
                    print('\n')

                    for c in studentsDict:
                        print(c,':', studentsDict[c], end =' ')
                    print()

                    print('------------------------------------------------------------------------------')
                    
                    break
                elif another_set == 'y':
                    inputSet()
                    total_crd = 0

                    print('\nwould you like to enter another set of data?')
                    another_set = input("\nif yes press 'y' to enter another set or press 'q' to quit the program and view the histogram: ")
                    another_set = another_set.lower()

                                        
            break
    elif MenuChoice == '3':
        print('\nThank you for using this program. Have a great day! :)')
        break

    else:
        print('Invalid Input. Please try again!')

        print('\nSelect the mode that you want to continue')
        print('\nStudent mode(One input at a time) --> 1 ')
        print('Staff mode (Many inputs at a time) --> 2')
        print('Exit --> 3')

        MenuChoice = input('\nEnter the number next to the mode to choose the mode: ')        
            


    
input()

