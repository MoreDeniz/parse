# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

from create import create_equation
from decoding import decode
from encoding import encode
from addition import addition

if __name__ == '__main__':
    equation1 = create_equation()
    equation2 = create_equation()
    print(equation1)
    print(equation2)
    print(decode(equation1))
    print(decode(equation2))
    print(decode(addition(equation1, equation2)))
    # str_equation = decode((equation1))
    # print(str_equation)
    # dict_equation = encode(str_equation)
    # print(dict_equation)