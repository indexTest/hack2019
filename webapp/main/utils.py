import random
import string
import requests

def generate_random_cookie_pid(stringLength=8):
    """Generate a random string of fixed length """
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(stringLength))



def call_API(seg_info,pid):
	r = requests.get(
					url = "https://www.ixplus.club/api/addsegment", 
					params = {'segment':seg_info,'pid':pid}
					)
	print(f"r.content: {r.content}")
	return r
