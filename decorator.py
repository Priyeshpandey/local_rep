import random
import time


def retry(func):
    def wrapper(*args, **kwargs):
        MAX_RETRY = kwargs['max_retry']
        INTERVAL = kwargs['interval']
        attempt = 1
        while attempt <= MAX_RETRY:
            try:
                func(*args, **kwargs)
                break
            except AssertionError as e:
                if attempt >= MAX_RETRY:
                    raise e
                pass
            time.sleep(INTERVAL)
            print(f"Let's try again! attempt = {attempt}")
            attempt += 1

    return wrapper

def repeat_till_success_based_on_actual_arguments(func):
    """
        To be used as a decorator for repeatedly calling a validation function until the success is observed
        or max iterations reached.
        This shall act only when arguments to original function indicate so.
        :param max_iterations: Number of times, the function call should be made.
        :param interval: Sleep after every failure. Retry after the sleep.
        :param retry: Boolean. Mandatory for this method to activate.
        :return:
        """
    def inner(*args, **kwargs):
        if 'retry' in kwargs and kwargs['retry'] is True:
            if 'max_iterations' in kwargs:
                max_iterations = int(kwargs['max_iterations'])
            else:
                max_iterations = 3
            if 'interval' in kwargs:
                interval = int(kwargs['interval'])
            else:
                interval = 10
            iteration = 1
            while iteration <= max_iterations:
                iteration += 1
                try:
                    func(*args, **kwargs)
                    break
                except Exception:
                    print("Try again!")
                    time.sleep(interval)
        else:
            func(*args, **kwargs)
    return inner


@repeat_till_success_based_on_actual_arguments
def check_me(x, *args, **kwargs):
    interval = kwargs['interval']
    target = random.randint(1, 10)
    assert x == target, f'{x} is not {target}'
    print("Success!")


def f(x):
    print('Enter f')
    if x==0:
        return f(x=1)
    print('done')




if __name__ == '__main__':
    f(0)
    # check_me(2, retry=True, max_iterations=10, interval=0)
