# Tyler Pettigrew
# CS362-HW1

""""To run this program, an IDE like Pycharm or the command line can be used
    command line: run "python Tyler_Pettigrew_hw1.py" in the terminal where the file is located
    Pycharm/Other IDE: Use the IDE's internal run function
"""




"""leap_year
    Inputs:
        year: a positive integer number
    Outputs:
        If the given year is a leap year based on the given criteria, print that the year is a leap year.
        Otherwise, say it isn't
"""

def leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(year, "is a leap year.")
            else:
                print(year, "is not a leap year")
        else:
            print(year, "is a leap year")
    else:
        print(year, "is not a leap year")


if __name__ == '__main__':
    year = input("Enter the year, or 'q' to quit: ")

    #Run the program without any checking the input

    year = int(year)
    leap_year(year)
