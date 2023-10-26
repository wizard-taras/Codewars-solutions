def basic_op(operator, value1, value2):
    math_ops = ['+', '-', '*', '/']
    if operator in math_ops:
    	if operator == '+': return value1 + value2
    	elif operator == '-': return value1 - value2
    	elif operator == '*': return value1 * value2
    	elif operator == '/': return value1 / value2
    else:
    	return 'Please enter valid operator'