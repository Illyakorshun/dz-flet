def main():
    print("Привіт")
    name = input("Введіть ваше імя: ")
    print(f"Привіт, {name}!")

if __name__ == "__main__":
    main()

def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

try:
    num = int(input("Введіть число: "))
    if num < 0:
        print("Факторіал визначений тільки для невід'ємних чисел.")
    else:
        print(f"Факторіал {num} дорівнює {factorial(num)}")
except ValueError:
    print("Будь ласка, введіть ціле число.")
