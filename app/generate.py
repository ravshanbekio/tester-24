import random
from value_list import words

def generate_random_value(query_type):
    value = None
    if query_type == 'integer':
        value = random.randint(1, 100)
    elif query_type == 'string':
        value = random.choice(words)
    elif query_type == 'boolean':
        value = random.choice([True, False])
    elif query_type == 'float':
        value = random.uniform(1.0, 5.0)
    return value