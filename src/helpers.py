# Helper functions.


def get_input_sub_func(text):
	"""
	XXX
	"""
	input_value=input(text)
	return input_value


def get_input(text, in_list=None, is_numeric=False):
	"""
	Wrapper for input sub function.
	This enables us to force input types and create mock inputs for unittesting.
	"""
	input_value=get_input_sub_func(text)
	if len(input_value) == 0:
		raise ValueError('ERROR invalid input - cannot be an empty string')
	elif in_list is not None and input_value not in in_list:
		raise ValueError('ERROR invalid input - must be in {}'.format(in_list))
	elif is_numeric and not input_value.isnumeric():
		raise ValueError('ERROR invalid input - must be numeric')
	return input_value if not is_numeric else int(input_value)


def try_again(method_to_call, *args, no_tries=3, **kwargs):
	"""
	This function enables automatic retries when exceptions occur.
	Used to enable automatic retries when user inputs invalid values.
	"""
	i=0
	valid=False
	while (i < no_tries) & (not valid):
		try:
			r=method_to_call(*args, **kwargs)
			valid=True
		except Exception as e:
			i+=1
			print(e)
	if not valid:
		raise Exception('ERROR maximum no. of retries reached - exiting :(')
	return r
