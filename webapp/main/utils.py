import random
import string


def generate_random_cookie_pid(stringLength=8):
    """Generate a random string of fixed length """
    lettersAndDigits = string.ascii_letters + string.digits
    return ''.join(random.choice(lettersAndDigits) for i in range(stringLength))