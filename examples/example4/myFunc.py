import json

def lambda_handler(event, context):
	print("Received event: " + json.dumps(event, indent=2))
	# print("hello = world" )

	predecessor_outputs = event['predecessor_outputs']
	for id in predecessor_outputs.keys():
		print("predecessor {} returned {}".format(str(id), str(predecessor_outputs[id])))


	response = {"utc_offset": "+0h", "interval": "day", "buckets": [{"count": 3, "start_time": "2018-07-03T00:00:00.000000Z"}], "tile" : [{"tile_id" : 1}, {"tile_id" : 2},{"tile_id" : 3}]}
	return response # Echo back the first key value
	#raise Exception('Something went wrong')
