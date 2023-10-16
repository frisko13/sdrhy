def count_trailing_zeros(n):
    count = 0
  
    # Пока n делится на 5
    while n >= 5:
        n //= 5
        count += n

    return count

number = 900
trailing_zeros = count_trailing_zeros(number)
print("Количество нулей в конце факториала", number, "равно:", trailing_zeros)
