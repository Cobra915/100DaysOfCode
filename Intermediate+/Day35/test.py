import os 
import pprint

env_var = os.environ

print('Your Environment Variables:')

pprint.pprint(dict(env_var), width = 1)