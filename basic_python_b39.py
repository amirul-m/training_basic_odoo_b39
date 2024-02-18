# print('Training Arkana Batch 39')

print('Petik satu')
print("Petik dua")

print(100)
print(1500.5)
print([100, 105.5, 'string 1'])

print(100-30)
print(100.0 + 50)

# print(5<10)
# print(5>10)
# print(5==5)

print(5<10 and 10>20)
print(5<10 or 10>20)

print('\nnot operation')
print(not 5<10)

print('\nvariable')
alpha = 100-30
print(alpha)
# print(alpha)

alpha = 1000 - 30
print(alpha)

# alpha = alpha - 30
alpha -= 30
print(alpha)

beta = 100 + 30
print(beta)

print('\nlooping')
print(1)
print(2)
print(3)
print(4)
print(5)

number = 1
while number <= 10:
    print(number)
    if number % 2 == 0:
        print('Bilangan Genap')
    else:
        print('Bilangan Ganjil')
    number += 1

# Looping with For
print('\nlooping for')

words = ['The', 'cat', 'sat', 'on', 'the', 'mat.']
# for idx, word in enumerate(words):
#     print(idx)
#     print(word)

print(words[0])
print(words[-1])

try:
    print(words[1])
except Exception as e:
    print(e)

print(words)
del words[2]
print(words)

print('\nGenap')
genap = [2, 4, 6, 8]
print(genap)
genap.append(10)
print(genap)

# genap.append([12, 14])
genap.extend([12, 14])
print(genap)


def print_bilangan(until_number, from_number=1):
    number = from_number
    while number <= until_number:
        print(number)
        if number % 2 == 0:
            print('Bilangan Genap')
        else:
            print('Bilangan Ganjil')
        number += 1

# print_bilangan(16)
# print_bilangan(20)
# print_bilangan(10, 5)
print_bilangan(until_number=10, from_number=5)
print_bilangan(from_number=5, until_number=10)
