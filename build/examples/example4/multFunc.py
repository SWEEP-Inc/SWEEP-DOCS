import json

def lambda_handler(event, context):
	print("Received event: " + json.dumps(event, indent=2))
	# print("hello = world" )

	predecessor_outputs = event['predecessor_outputs']
	for id in predecessor_outputs.keys():
		print("predecessor {} returned {}".format(str(id), str(predecessor_outputs[id])))

	try:
		response = {"received_tile" : predecessor_outputs['1']["tile"]["tile_id"]}
	except Exception as e:
		response = event
	return response # Echo back the first key value
	#raise Exception('Something went wrong')
