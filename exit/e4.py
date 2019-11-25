import os

def outahere():
    print ('bye os world')
    os._exit(99)
    print('never reached')

if __name__ == '__main__':
    try:
        outahere()
    except SystemExit:
        print('never raise')
    finally:
        print('no cleanup')