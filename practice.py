# # Array reverse
# def reverse(array):
#     start = 0
#     end = len(array) - 1

#     while start < end:
#         # array_temp = array[start]
#         # array[start] = array[end]
#         # array[end] = array_temp
#         array[start], array[end] = array[end], array[start] #another way
#         start += 1 
#         end -= 1
#     return array


# def reverse_pythonic(array):
#     return array[::-1]

# if __name__ == "__main__":
#     arr = [1,3,5,7,9,11]
#     print(reverse(arr))
#     print(reverse_pythonic(arr))

# Interger reversion
# Leetcode example: (7) https://leetcode.com/problems/reverse-integer/

# # Solution1
# def reverse1(x: int)-> int:
#     if x > 0:
#         x_string = str(x)
#         x = int(x_string[::-1])
#     elif x < 0:
#         x_string = str(-1*x)
#         x = -1*int(x_string[::-1])

#     if x < -(2**31) or x > (2**31-1):
#         return 0
#     else:
#         return x
    
# if __name__ == "__main__":
#     interger = -123
#     print(reverse(interger))

# Solution 2
def reverse2(x: int)-> int:
    if x > 0:
        y = ""
        x_arr = str(x) 
        len_init = len(x_arr) 
        for i in range(len_init-1): # 餘數最後剩下的那一位不需要再進迴圈，留在最外層直接加入 y string，所以長度少跑一個
            y = y + str(x%10) # [5,4,3]，，假設x=2345為例
            length = len(x_arr) 
            x_arr = x_arr[0:(length-1)] #[0:3]-> 234 [0:2]->23 [0:1]->2 
            x = int(x_arr)
        y = int(y + str(x))
    elif x < 0:
        x = -1 * x
        y = ""
        x_arr = str(x) 
        len_init = len(x_arr)
        for i in range(len_init-1): # 餘數最後剩下的那一位不需要再進迴圈，留在最外層直接加入 y string，所以長度少跑一個 
            y = y + str(x%10) # [5,4,3]，假設x=2345為例
            length = len(x_arr) 
            x_arr = x_arr[0:(length-1)] #[0:3]-> 234 [0:2]->23 [0:1]->2 
            x = int(x_arr)
        y = -int((y + str(x)))
    if y < -(2**31) or y > (2**31-1):
        return 0
    else:
        return y

if __name__ == "__main__":
#     interger = -123
#     print(reverse1(interger))
    interger = -100
    print(reverse2(interger))



