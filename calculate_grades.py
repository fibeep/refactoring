# Written by Kamran Bigdely
# Example for Compose Methods: Extract Method.
import math

def calculate_mean(grades):
    mean = 0
    for grade in grades:
        mean += grade
    return mean / len(grades)

def calculate_sd(grades, mean):
    sum_of_sqrs = 0
    for grade in grades:
        sum_of_sqrs += (grade - mean) ** 2
    sd = math.sqrt(sum_of_sqrs / len(grades))
    return sd



def print_stat():
    grade_list = []
    # Get the inputs from the user
    n_student = 5
    for _ in range(n_student):
        grade_list.append(int(input('Enter a number: ')))

    # Calculate the mean and standard deviation of the grades

    mean = calculate_mean(grade_list)
    sd = calculate_sd(grade_list, mean)

    # print out the mean and standard deviation in a nice format.
    print('****** Grade Statistics ******')
    print("The grades's mean is:", mean)
    print('The population standard deviation of grades is: ', round(sd, 3))
    print('****** END ******')

print_stat()