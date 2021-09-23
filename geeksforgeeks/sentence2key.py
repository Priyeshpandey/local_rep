import time
import logging

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)


def timer(func):
    start = time.time()

    def inner_func(*args, **kwargs):
        res = func(*args, **kwargs)
        logger.info(f"Time elapsed : {time.time() - start}s")
        return res

    return inner_func


@timer
def sentence2key(sentence: str) -> str:
    store = {
        'A': '2', 'B': '22', 'C': '222',
        'D': '3', 'E': '33', 'F': '333',
        'G': '4', 'H': '44', 'I': '444',
        'J': '5', 'K': '55', 'L': '555',
        'M': '6', 'N': '66', 'O': '666',
        'P': '7', 'Q': '77', 'R': '777',
        'S': '7777', 'T': '8', 'U': '88',
        'V': '888', 'W': '9', 'X': '99',
        'Y': '999', 'Z': '9999', ' ': '0'
    }

    response = ''
    for x in sentence:
        time.sleep(0.1)
        response += store[x]

    return response


if __name__ == '__main__':
    # sentence = input()
    # print(sentence2key(sentence))
    # input("Press any key and enter to exit ...")
    print(sentence2key('GEEKSFORGEEKS'))
    print(sentence2key('HELLO WORLD'))
