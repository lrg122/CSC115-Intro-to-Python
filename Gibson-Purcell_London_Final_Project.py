import random


class Course:
    def __init__(self, name, credit_hours, letter_grade):
        self.name = name
        self.credit_hours = credit_hours
        self.letter_grade = letter_grade

    def __str__(self):
        return f"Course: {self.name}, Credit Hours:{self.credit_hours}, Grade: {self.letter_grade}"



class Student:
    # A defined class with all the required parameters according to what information needs to be collected
    def __init__(self, full_name, email, major, project_info):
        self.full_name = full_name
        self.email = email
        self.major = major
        self.project_info = project_info
        self.courses = []
        self.letter_grade_to_gpa_dictionary = {"A+":4.0,"A":4.0,"A-":3.7,"B+":3.3,"B":3.0,"B-":2.7,"C+":2.3,"C":2.0,"C-":1.7,"D+":1.3,"D":1.0}

    def add_course(self,course):
        self.courses.append(course)


    def letter_grade_to_gpa(self,letter_grade):
        return self.letter_grade_to_gpa_dictionary.get(letter_grade,0)

    def calculate_gpa(self):

        total_quality_points = 0
        total_credit_hours = 0
        for course in self.courses:
            course_gpa = self.letter_grade_to_gpa(course.letter_grade)
            quality_points = course_gpa * course.credit_hours
            total_quality_points += quality_points
            total_credit_hours += course.credit_hours
        return total_quality_points / total_credit_hours



    def print_student_gpa(self): # str function
        print(f"Student Name: {self.full_name}")
        print(f"Email: {self.email}")
        print(f" Major: {self.major}")
        print(f"Project Info: {self.project_info}")
        for each_course in self.courses:
            print(each_course)

        final_gpa = self.calculate_gpa()
        print(f" Final GPA: {final_gpa:.2f}")



def calculate_student_gpa():
    # main function that calls the defined functions within the two classes to output results for specific user input information
    print("-" * 50)
    print(f"Student GPA")
    print("-" * 50)
    student_input_info = input(f"Enter student information - full name, email, major, and project information (separated by commas):")
    My_Student = Student()
    number_of_courses = int(input("How many courses do you want to add? (2-6)"))

    while (number_of_courses < 2 and number_of_courses > 6):
        number_of_courses = int(input("Invalid Input. How many courses do you want to add? (2-6)"))

    for each_course in range(number_of_courses):
        input_course_info = input("Enter course name, credit hours, and letter grade (separated by commas):").split(',')
        credit_hours = int(credit_hours)
        course_name, credit_hours, letter_grade = [info.strip() for info in input_course_info]
        My_Course = Course()
        My_Student.add_course(My_Course)


    My_Student.print_student_gpa()







def lottery_number_generator():
    # This generator simulates the lottery system by producing 5 unique random numbers and one power ball number
    print("-" * 50)
    print(f"Lottery Number Generator")
    print("-" * 50)
    random_lottery_numbers_ = sorted(random.sample(range(1,70),5))


    power_ball_number = random.randint(1,26)
    random_lottery_numbers_.append(power_ball_number)
    print(*random_lottery_numbers_)





def pig_latin():
    # converts a user input sentence into pig latin by slicing the first letter, moving it to the end and adding "ay".
    print("-" * 50)
    print(f"Pig Latin")
    print("-" * 50)
    input_sentence = input("Enter sentence to be converted into Pig Latin:").upper()
    sentence_list = input_sentence.split()
    print(input_sentence)

    for each_word in sentence_list:
        print(f"{each_word[1:]}{each_word[0]}AY", end = " ")






def rock_paper_scissors_game():
    # This program allows a user to play rock, paper, scissors against the computer using a randomly generated choice.
    print("-" * 50)
    print(f"Rock Paper Scissors Game")
    print("-" * 50)
    game_choice_dictionary = {1: "rock", 2: "paper", 3: "scissors"}
    user_input_choice = input("Enter a choice - rock, paper, scissor:")
    computer_random_number_choice = random.randint(1,3)
    computer_choice_word = game_choice_dictionary[computer_random_number_choice]

    if user_input_choice not in game_choice_dictionary.values(): # validation
        user_input_choice = input("Enter a choice - rock, paper, scissor:")

    if user_input_choice == computer_choice_word:
            print("TIE PLAY AGAIN.")
            user_input_choice = input("Enter a choice - rock, paper, scissor:")
    elif user_input_choice == "scissors" and computer_choice_word == "paper":
        print("Player wins")
        print(f"Player's Choice: {user_input_choice}")
        print(f"Computer's Choice: {computer_choice_word}")
    elif user_input_choice == "rock" and computer_choice_word == "scissors":
        print("Player wins")
        print(f"Player's Choice: {user_input_choice}")
        print(f"Computer's Choice: {computer_choice_word}")
    elif user_input_choice == "paper" and computer_choice_word == "rock":
        print("Player wins")
        print(f"Player's Choice: {user_input_choice}")
        print(f"Computer's Choice: {computer_choice_word}")
    else:
        print("Computer wins")
        print(f"Player's Choice: {user_input_choice}")
        print(f"Computer's Choice: {computer_choice_word}")













def main():
    # The menu for the program that lists the different options user can select to interact with and allows them to exit.
    menu_program =('Welcome to the CSC115 final project.' 
                  '\nEnter 1 to calculate GPA '
                  '\nEnter 2 for Lottery Number Generator'
                  '\nEnter 3 for Pig Latin'
                   '\nEnter 4 for Rock, Paper, Scissors')

    print(menu_program)
    menu_program_input = (input("Enter menu option 1,2,3,4, or 9 to exit:"))

    while (menu_program_input !="9"):

        if (menu_program_input == "1"):
            calculate_student_gpa()
        elif(menu_program_input == "2"):
            lottery_number_generator()
        elif(menu_program_input == "3"):
            pig_latin()
        elif(menu_program_input == "4"):
            rock_paper_scissors_game()
        else:
           print("Invalid Option")

        print(menu_program)
        menu_program_input = (input(" Enter menu option 1,2,3,4, or 9 to exit:"))

    print("You selected option 9. Exiting program. Good-Bye.")


if __name__ == '__main__':
    main()