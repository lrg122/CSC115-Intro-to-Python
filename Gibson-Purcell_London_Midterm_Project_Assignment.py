print('London Gibson-Purcell')
print('lrg122@miami.edu')
print('CSC-115')
print('Data Science & AI')


python_program = ('This Python program display Roman Numerals and Population.'
                  '\nEnter option 1 to display Roman Numerals. '
                  '\nEnter option 2 to Predict Population.'
                  '\nEnter 9 to Exit the program.')
print(python_program)
python_program_input = input("Please enter a choice 1,2,9:")
while (python_program_input != "9"):

    if(python_program_input == '1'):
        print('Here is the ROMAN NUMERALS')
        user_input_numeral = int(input('Please enter a number between 1 to 10 only:'))
        while user_input_numeral < 1 or user_input_numeral > 10:
            user_input_numeral = int(input('Invalid Input. Please enter a number between 1 to 10 only:'))
        if user_input_numeral == 1:
            print("Number 1 -----> I")
        elif user_input_numeral == 2:
            print("Number 2 -----> II")
        elif user_input_numeral == 3:
            print("Number 3 -----> III")
        elif user_input_numeral == 4:
            print("Number 4 -----> IV")
        elif user_input_numeral == 5:
            print("Number 5 -----> V")
        elif user_input_numeral == 6:
            print("Number 6 -----> VI")
        elif user_input_numeral == 7:
            print("Number 7 -----> VII")
        elif user_input_numeral == 8:
            print("Number 8 -----> VIII")
        elif user_input_numeral == 9:
            print("Number 9 -----> IX")
        else:
            print("Number 10 ----> X")

        python_program_input = input(" Do you want to run this program again? Please enter a choice 1,2,9:")


    elif(python_program_input == '2'):
        print('Here is the PREDICTION POPULATION')
        starting_num_organisms = int(input('Please input the number of Starting Organisms:'))

        while starting_num_organisms < 1:
            starting_num_organisms = int(input('Invalid Input. Please reenter input the number of Starting Organisms:'))

        avg_pop_increase = float(input("Please enter the average population increase:"))
        while avg_pop_increase < 1 or avg_pop_increase > 100:
            avg_pop_increase = float(input(" Invalid Input. Please reenter the average population increase: "))

        num_days_multiply = int(input('Please Input the Number of days to multiply:'))
        while num_days_multiply < 2 or num_days_multiply > 30:
            num_days_multiply = int(input('Invalid Input. Please reenter Input the Number of days to multiply:'))
        days = 1
        population = starting_num_organisms
        print('Day Approximate \t Population')
        print('-' * 45)
        for each_day in range(1, num_days_multiply + 1):
            while days < num_days_multiply:
                population += ((avg_pop_increase / 100) * population)
                days += 1
            print(f'{each_day} \t\t\t\t {population}')



    else:
        print('Invalid Input')

    print(python_program)
    python_program_input = input('Please enter a choice 1,2,9:')

print('User select option 9. Exit Program. Good-bye.')





