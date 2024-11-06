from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power):
        Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemies_left = 100

    def run(self):
        print(f'{self.name}, на нас напали!\n')
        days_fighting = 0
        while self.enemies_left > 0:
            self.enemies_left -= self.power
            days_fighting += 1
            print(f'{self.name} сражается {days_fighting} день(дня)..., осталось {self.enemies_left} воинов.\n')
            sleep(1)
        print(f'{self.name} одержал победу спустя {days_fighting} дней(дня)!\n')


if __name__ == '__main__':
    first_knight = Knight('Sir Lancelot', 10)
    second_knight = Knight("Sir Galahad", 20)
    threads = [first_knight, second_knight]
    for knight in threads:
        knight.start()

    for knight in threads:
        knight.join()

    print('Война окончена.')
