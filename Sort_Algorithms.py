"""
File:         Sort_Algorithms.py
Author:       Ethan Cheung, Antionne Andries, Manuela Rugemintgwaza, Darwin Xue
Date:         5/25/2022
E-mail:       echeung801@gmail.com, antionne03@gmail.com, xxxxxx
Description:  This is sort algorithms.
"""


sorted = False

UNSORTED_DATA = [170, 45, 75, 90, 802, 24, 2, 66]

ALGORITHMS = ["radix", "bubble", "quick", "merge", "insertion", "comb"]



def max_digit(nums = UNSORTED_DATA):
    """
    This helper function returns the size of the largest number in the data set.
    """

    # list comprehension? need to do more research
    
    return max([len(str(num)) for num in nums])


def radix_sort():
    # initialization of array and data
    sorted_data = []
    length_of_data = len(UNSORTED_DATA)

    # deep copy of global constant array
    for i in range(length_of_data):
        sorted_data.append(UNSORTED_DATA[i])

    # count how many times we need to loop by using the max digit helper function.
    loop_times = max_digit(UNSORTED_DATA)

    # perform bucket split: which will categorize data by least significant digit, ten buckets as a dictionary
    bucketMap = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 0:[]}

    for i in range(loop_times):
        # this will loop max digit times, and mod to the max digit's power, getting our one's, two's, i'th many places.
        for num in sorted_data:
            # i'th digit of num??? lol
            integer = (str(num % (10 ** (i + 1))))

            while(len(integer) < loop_times):
                integer = "0" + integer
            bucketMap[int(integer[loop_times - i - 1])].append(num)
            
        # clear and then refill buckets
        sorted_data = []
        
        for j in range(10):
            sorted_data += bucketMap[j]

        bucketMap = {n:[] for n in range(10)}

    return sorted_data





# def bubble_sort(DATA, sorted):
    
# def quick_sort(DATA, sorted):
    
# def merge_sort(DATA, sorted):
    
# def insertion_sort(DATA, sorted):

# def comb_sort(DATA, sorted):




if __name__ == '__main__':

    print("This is the driver code")

    # print("Select which sort algorithm to use: ")
    # for i in range(len(ALGORITHMS)):
    #     print(ALGORITHMS[i])
    
    the_data = radix_sort()

    if(the_data != UNSORTED_DATA):
        print("Operation completed successfully!")
        print(the_data)

    else:
        print("Operation failed")
        print(the_data)
