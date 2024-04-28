from json_criteria import meets_criteria, Config

def custom1(record_value, value):
    return record_value + value == 60

record = { 'name': 'Joe', 'age': 30 }
criteria = { 'key': 'age', 'op': 'custom1', 'value': 30 }
config = Config(custom_ops = { 'custom1': custom1 })

# `result` will be True
result = meets_criteria(record, criteria, config)
