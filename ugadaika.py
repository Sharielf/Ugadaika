import random
print('Добро пожаловать в числовую угадайку')


def play_game():
    n = random.randint(1, 101)

    def is_valid(num):
        if 1 <= int(num) <= 100:
            return True
        else:
            print('А может быть все-таки введем целое число от 1 до 100?')
            return False

    while True:
        num = int(input('Введите число от 1 до 100'))
        if is_valid(num):
            num = int(num)
            if n < num:
                print('Ваше число больше загаданного, попробуйте еще разок')
            elif n > num:
                print('Ваше число меньше загаданного, попробуйте еще разок')
            else:
                print('Вы угадали, поздравляем!')
                break
    replay = input('Хотите сыграть еще раз? (да/нет): ')
    if replay.lower() == 'да':
        play_game()
    else:
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')


print('Добро пожаловать в числовую угадайку')
play_game()
