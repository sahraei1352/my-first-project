
import random

# ساخت ماتریس بازی
board = [
    [0 for col in range(10)]
    for row in range(10)
]

# تبدیل شماره خانه به مختصات ماتریس
def number_to_position(number):

    row_from_bottom = (number - 1) // 10
    col_offset = (number - 1) % 10

    row = 9 - row_from_bottom

    if row_from_bottom % 2 == 0:
        col = 9 - col_offset
    else:
        col = col_offset

    return row, col


# قرار دادن شماره خانه ها در ماتریس
for number in range(1, 101):

    row, col = number_to_position(number)
    board[row][col] = number


# تعریف مارها
snakes = {
    25: 5,
    47: 19,
    56: 34,
    98: 20
}

# تعریف نردبان ها
ladders = {
    3: 22,
    8: 30,
    28: 55,
    71: 92
}


# نمایش صفحه بازی
def show_board(position):

    print("\n--- SNAKES AND LADDERS ---\n")

    for row in range(10):

        for col in range(10):

            number = board[row][col]

            if number == position:
                print(" P ", end=" ")
            else:
                print(f"{number:3}", end=" ")

        print()


# شروع بازی
player_position = 1

while player_position < 100:

    show_board(player_position)

    input("\nبرای پرتاب تاس Enter بزنید...")

    dice = random.randint(1, 6)

    print("عدد تاس:", dice)

    new_position = player_position + dice

    if new_position > 100:
        print("برای رسیدن به خانه 100 باید عدد مناسب بیاورید.")

    else:

        player_position = new_position

        if player_position in snakes:

            print("اوه! به مار برخورد کردید!")

            player_position = snakes[player_position]

        elif player_position in ladders:

            print("عالی! از نردبان بالا رفتید!")

            player_position = ladders[player_position]

    print("موقعیت فعلی:", player_position)


print("\nتبریک! شما برنده شدید!")
show_board(player_position)
