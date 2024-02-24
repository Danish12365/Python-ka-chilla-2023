
# defining a function
# 1
# def print_codenics():
#     print("we are learning with Aammar")
#     print("we are learning with Aammar")
#     print("we are learning with Aammar")

    
# print_codenics()

# 2

# def print_codenics():
#    text = "we are learning with Aammar in codanics youtub channl"

#    print(text)
#    print(text)
#    print(text)
# print_codenics()   

# 3
# def print_codenics(text):
#    print(text)
#    print(text)
#    print(text)
# print_codenics("we are learning with Aammar in codanics youtub channl")


#  defining a function with if, elif and else statements

# def school_calculator(age):
#    if age==5:
#       print("Hammad can join the school")
#    elif age >6:
#       print("Aammar should go higher school")
#    else:
#       print("Hammad is still baby")

# school_calculator(8)


# define a function of future

# def future_age(age):
#     return (age + 10)
# print(future_age(7))



# def future_age(age):
#     new_age=age+20
#     return new_age
#     print(new_age)

# futur_predicted_age= future_age(18)
# print(futur_predicted_age)

# # i understand function really well.


# practice my self

# def danish():
#     print("hello word")
#     print("i am learning python")
#     print("we are learning")
    


# def danish():
#     text="we love pakistan and iran"
#     print(text)
#     print(text)
#     print(text)


# danish()


# def danish(text):
#     print(text)
#     print(text)
#     print(text)
# danish("we knows")


# def school_calculator(age):
#     if age==5:
#         print("hammad can go to school")
#     elif age<5:
#         print("hammad is still babay")
#     else :
#         print("hammad should join higher school")        


# school_calculator(2)

# def future_age(age):
#     new_age=(age+10)
#     return new_age
#     print(new_age)
# future_predicted_age=future_age(10)
# print(future_predicted_age)


# def future_age(age):
#     new_age = age + 10
#     print(new_age)  # This line will be executed before returning the result
#     return new_age

# future_predicted_age = future_age(10)
# print(future_predicted_age)


# def add_number(x,y):
#     result= x+y
#     return result

# sum_result= add_number(3,6)
# print("sum = ", sum_result)



# def rectangle_area(length, width):
#     area = length * width
#     return area


# area_result = rectangle_area(10, 5)
# print("Area of the rectangle:", area_result)


# def greet(name):
#     """This function greets the user."""
#     message = f"Hello, {name}!"
#     return message

# # Example usage
# user_name = "Alice"
# greeting_message = greet(user_name)
# print(greeting_message)


# def check_number(number):
#     """This function checks if a number is positive, negative, or zero."""
#     if number > 0:
#         return "Positive"
#     elif number < 0:
#         return "Negative"
#     else:
#         return "Zero"

# # Example usage
# result = check_number(-7)
# print(result)


def simple_calculator(x, y, operation):
    """This function performs basic calculations."""
    if operation == "add":
        return x + y
    elif operation == "subtract":
        return x - y
    elif operation == "multiply":
        return x * y
    elif operation == "divide":
        return x / y
    else:
        return "Invalid operation"

# Example usage
result = simple_calculator(10, 5, "multiply")
print("Result:", result)
