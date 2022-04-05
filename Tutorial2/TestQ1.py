from Q1 import StopWatch


def main():
    size = 1000000
    sw = StopWatch()
    # sw.start()
    for i in range(1, size + 1):
        i += 1
    sw.stop()
    print(f'this loop took: {sw.getElapsedTime()} milliseconds')


main()
