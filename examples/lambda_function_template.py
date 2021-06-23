import sys
import traceback


def handler(event, context):
	'''
	Template for a lambda function used in SWEEP.

	:param event: (dict) contains the input arguments. always has the following two items:
				  static_input: (dict) contains the static input for this task (static input is specified in the workflow definition)
				  predecessor_outputs: (list of dicts) a list containining the output of every predecessor of the task in the task graph
	:param context: (LambdaContext) AWS Lambda uses this parameter to provide runtime information to the handler
	:return: (dict)
	'''
	predecessor_outputs = event['predecessor_outputs']

	for id in predecessor_outputs.keys():
		print("predecessor {} returned {}".format(str(id), str(predecessor_outputs[id])))

	static_input = event['static_input']

	# Fill out dict with whatever - no requirements on structure.
	out_dict = {}

	# All exceptions should be handled and added to out_dict if they are to be seen in the SWEEP logs.
	try:
		# do something
		x = static_input["some_key"]
		out_dict["result"] = x+1

	except Exception:
		exc_type, exc_value, exc_trace = sys.exc_info()
		out_dict["exception"] = repr(traceback.format_exception(exc_type, exc_value, exc_trace))

	return out_dict
