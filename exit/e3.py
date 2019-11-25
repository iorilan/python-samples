import sys
def later():
    print('Bye sys world')
    sys.exit(42)
    print('Never reached')

if __name__ == '__main__':
    try:
        later()
    except SystemExit:
        print('exception raised')
    finally:
        print('clean up job')