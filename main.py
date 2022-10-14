import contextlib
import glob
import random


def main():
    all_dirs = glob.glob('seeds\\*.txt')
    count = int(input("Введите кол-во фраз: "))
    for j in all_dirs:
        lines = open(j, encoding='UTF-8').readlines()
        for i in range(1000):
            with open(f'result.txt', 'a') as o:
                with contextlib.redirect_stdout(o):
                    random_seeds = random.sample(lines, count)
                    random_seeds = list(map(str.strip, random_seeds))
                    seed = ' '.join(random_seeds)
                    print(seed)
    input("Finished. Press any key...")

if __name__ == '__main__':
    main()