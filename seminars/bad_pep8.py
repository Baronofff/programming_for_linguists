def greet_name(name):
    print(f'Hello, {name}!')


def get_sum_of_numbers(num1: int, num2: int):
    if isinstance(num1, int) and isinstance(num2, int):
        return num1 + num2
    raise TypeError('The arguments should be integers')

if __name__ == '__main__':

    names=['Alice', 'Bob', 'Charlie']
    for name in names:
        greet_name(name)

    print(get_sum_of_numbers(
        num1=1,
        num2=5
    ))
