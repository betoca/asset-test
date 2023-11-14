import json

#useless comment 2
# change 2

# modelop.metrics
def metrics(df):
	with open("model_test_results.json", "r") as f:
		contents = f.read()
	test_results = json.loads(contents)
	yield test_results
