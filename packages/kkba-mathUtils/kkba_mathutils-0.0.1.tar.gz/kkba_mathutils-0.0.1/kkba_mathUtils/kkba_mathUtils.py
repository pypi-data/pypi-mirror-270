import math

def mean_of_list(list):
    return (1/len(list)) * sum(list)

def harmonic_mean(list):
    sum_liste = 0
    for num in list:
        sum_liste += (1/num)
        
    return len(list) / sum_liste

def isbigprime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True

def get_divisors(n):
    dividers_list = []
    for divider in range(1, n+1):
        if n % divider == 0:
            dividers_list.append(divider)

    return dividers_list

def isprime(n):
    for d in range(2,n):
        if n % d == 0:
            return False
    return True

def ispower_another_number(n,p):
    for i in range(1, n):
        if i**p > n:
            return False
        elif i**p == n:
            return True
        
def perfect_numbers_list(min, max):
    perfect_numbers_list = []
    for n in range(min, max+1):
        if isperfect(n):
            perfect_numbers_list.append(n)
    return perfect_numbers_list

def isperfect(nb):
    print(get_divisors(28))
    if sum(get_divisors(nb)[:-1]) == nb:
        return True
    else:
        return False

def primes_list(min, max):
    primes_list = []
    for num in range(min, max+1):
        if isprime(num):
            primes_list.append(num)
    return primes_list

def prime_divisors(n):
    dividers_prime_list = []
    for divider in get_divisors(n):
        if isprime(divider):
            dividers_prime_list.append(divider)

    return dividers_prime_list

def fibonacci(n):

    if n==1 or n==2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
def variance(liste):
    moy = mean_of_list(liste)
    var = 0

    for nb in liste:
        var += (nb - moy)**2

    return var / len(liste)



def standard_deviation(liste):
    moy = mean_of_list(liste)
    var = 0
    for nb in liste:
        var += (nb - moy)**2

    return math.sqrt(var/len(liste))

def merge_map(dict1, dict2):
    
    final_dict = dict1.copy()
    final_dict.update(dict2)
    return final_dict



def merge_map_for(dict1, dict2):

    final_dict = dict()
    for dictionnaire in [dict1,dict2]:
        for key, value in dictionnaire.items():
            final_dict[key] = value

    return final_dict

def decimal_to_binary(n):
    
    binary = ""
    while n > 0 :
        binary = str(n%2) + binary
        n = n // 2

    return binary

def binary_to_decimal(binary):
    
    if "0b" in binary:
        binary = binary.replace("0b", "")
        
    total = 0
    for i, bit in enumerate(binary[::-1]):
        total += int(bit) * 2**i

    return total

def decimal_to_hexadecimal(n):
    hexadecimal = ""
    hexa_values = {"0" : "0", "1" : "1", "2" : "2", "3" : "3", "4" : "4", "5" : "5", "6" : "6",
            "7" : "7", "8" : "8", "9" : "9", "10" : "A", "11" : "B", "12" : "C",
            "13" : "D", "14" : "E", "15" : "F"}

    while n > 0:
        hexadecimal = hexa_values[str(n%16)] + hexadecimal
        n = n // 16

    return hexadecimal

def hexadecimal_to_decimal(hexadecimal):
    
    hexa_values = {"0" : 0, "1" : 1, "2" : 2, "3" : 3, "4" : 4, "5" : 5, "6" : 6,
                   "7" : 7, "8" : 8, "9" : 9 , "A" : 10, "B" : 11, "C" : 12,
                   "D" : 13, "E" : 14, "F" : 15}

    if "0x" in hexadecimal:
        hexadecimal = hexadecimal.replace("0x", "")

    hexadecimal = hexadecimal.upper()
    total = 0
    for i, digit in enumerate(hexadecimal[::-1]):
        total += hexa_values[digit] * 16**i

    return total

def vector_add(vector1, vector2):
    
    if len(vector1) != len(vector2):
        return None
    
    new_vector = list()
    for i in range(len(vector1)):
        new_vector.append(vector1[i] + vector2[i])

    return new_vector

def show_matrix(matrice):
    """Affiche la matrice dans la console"""
    
    for line in matrice:
        print(line)

        

def generate_random_matrix(M, N, inf=1, sup=100):
    
    matrix = []

    for i in range(M):
        line = []
        for j in range(N):
            line.append(math.randint(inf, sup))
        matrix.append(line)

    return matrix

def area_circle(rayon):
    return 2*math.pi*rayon**2

def circumference_circle(rayon):
    return 2*math.pi*rayon

def perimeter_triangle(ab,bc,ca):
    return ab+bc+ca

def area_triangle(b, h):
    return (b+h)/2

def perimeter_rectangle(length, width):
    return 2*length + 2*width

def area_rectangle(lenght, width):
    return lenght*width

def unique_elements(liste):
    if len(liste) == len(list(set(liste))):
        return True

    else:
        return False
    
def trimorphic(n):
    return str(n**3).endswith(str(n))

def natural_to_roman(n):
    int_rom = [(1000, "M"),
               (900, "CM"),
               (500, "D"),
               (400, "CD"),
               (100, "C"),
               (90, "XC"),
               (50, "L"),
               (40, "XL"),
               (10, "X"),
               (9, "IX"),
               (5, "V"),
               (4, "IV"),
               (1, "I")]

    romain = []

    for i, num in int_rom:
        while n >= i:
            n -= i
            #print(n)
            romain.append(num)

    return "".join(romain)

def roman_to_natural(romain):
    
    double = {"CM" : 900, "CD" : 400, "XC" : 90, "XL" : 40, "IX" : 9, "IV" : 4}
    unique = {"M" : 1000, "D" : 500, "C" : 100, "L" : 50, "X" : 10, "V" : 5, "I" : 1}

    entier = 0
    i = 0

    #Tant qu'on a pas parcouru le nombre romain en entier
    while i < len(romain):
        if i < len(romain) - 1 and romain[i:i+2] in double:
            entier += double[romain[i:i+2]]
            i += 2
        else:
            entier += unique[romain[i]]
            i += 1
    return entier

def gcd(x,y):
    
    if x < y:
        x, y = y, x

    if x % y == 0:
        return y

    for k in range(y//2, 0, -1):
        if x % k == 0 and y % k == 0:
            return k

def geometric(liste):
    """Renvoie la moyenne géométrique des éléments d'une liste"""
    product_list = 1
    for nb in liste:
        product_list *= nb

    return product_list**(1/len(liste))

def quadratic(liste):
    """Renvoie la moyenne quadratique des éléments d'une liste"""
    sum_liste = 0
    for nb in liste:
        sum_liste += nb**2
    return math.sqrt(sum_liste/len(liste))

