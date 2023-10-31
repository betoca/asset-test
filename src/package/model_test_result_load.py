import json
#useless comment
#Edit one more time

# modelop.metrics
def metrics(df):
	with open("model_test_results.json", "r") as f:
		contents = f.read()
	test_results = json.loads(contents)
	yield test_results
