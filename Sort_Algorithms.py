"""
File:         Sort_Algorithms.py
Author:       Ethan Cheung, Antionne Andries, Manuela Rugemintgwaza, Darwin Xue
Date:         5/25/2022
E-mail:       echeung801@gmail.com, antionne03@gmail.com, xxxxxx
Description:  This is sort algorithms.
"""


UNSORTED_DATA = [170, 45, 75, 90, 802, 24, 2, 66]

ALGORITHMS = ["radix", "bubble", "quick", "merge", "insertion", "comb"]



def max_digit(nums = UNSORTED_DATA):
    """
    This helper function returns the size of the largest number in the data set.
    """

    # list comprehension? need to do more research
    
    return max([len(str(num)) for num in nums])


def deep_copy():
    data = []
    length_of_data = len(UNSORTED_DATA)

    # deep copy of global constant array
    for i in range(length_of_data):
        data.append(UNSORTED_DATA[i])
    
    # process is now finished, return
    return data


def radix_sort():
    # initialization of array and data
    sorted_data = []

    # deep copy of global constant array, use deep copy function
    sorted_data = deep_copy()

    # count how many times we need to loop by using the max digit helper function.
    loop_times = max_digit(UNSORTED_DATA)


    # perform bucket split: which will categorize data by least significant digit, ten buckets as a dictionary
    bucketMap = {1:[], 2:[], 3:[], 4:[], 5:[], 6:[], 7:[], 8:[], 9:[], 0:[]}


    for i in range(loop_times):
        # this will loop max digit times, and mod to the max digit's power, getting our one's, two's, i'th many places.
        for num in sorted_data:
            # i'th digit of num
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


def pass_once_sort(sorted_data):
    """
    This function will swap and sort values if they are not in descending order.
    """
    
    for i in range(len(sorted_data)):
        # bounds checking inside the data array
        if ( ((i + 1) < len(sorted_data)) and sorted_data[i] > sorted_data[i + 1] ):
            # swap positions
            sorted_data[i], sorted_data[i + 1] = sorted_data[i + 1], sorted_data[i]
    
    # return swapped data
    return sorted_data


def bubble_sort():
    """
    This is bubble sort, it is n^2 (nested for loop)
    """
    # make deep copy
    sorted_data = deep_copy()

    # for loop to make n^2
    for i in range(len(sorted_data)):
        # pass once
        pass_once_sort(sorted_data)

    # end of bubble sort function
    return sorted_data


    
def partition(data):

    if len(data) <= 1:
       return data

    pivot_left = []
    pivot_right = []

    for i in range(len(data)):
        # for loop, data separation between left and right

        if data[i] < data[-1]:
           pivot_left.append(data[i])

        if data[i] > data[-1]:
            pivot_right.append(data[i])

        
    pivot_left = partition(pivot_left)
    
    # recursive calls

    pivot_right = partition(pivot_right)

    # end return 
    return pivot_left + [data[-1]] + pivot_right



def quick_sort():

    # initialization of array and data
    sorted_data = []

    # deep copy of global constant array, use deep copy function
    sorted_data = deep_copy()

    pivot_trace = partition(sorted_data)
    
    print(pivot_trace)

    
# def merge_sort(DATA, sorted):
    
# def insertion_sort(DATA, sorted):

# def comb_sort(DATA, sorted):


if __name__ == '__main__':

    print("This is the driver code")

    # print("Select which sort algorithm to use: ")
    # for i in range(len(ALGORITHMS)):
    #     print(ALGORITHMS[i])
    
    the_data = bubble_sort()

    if(the_data != UNSORTED_DATA):
        print("Operation completed successfully!")
        print(the_data)

    else:
        print("Operation failed")
        print(the_data)
