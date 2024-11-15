from transformers import pipeline

specific_model = pipeline(model="finiteautomata/bertweet-base-sentiment-analysis")

data = ["I love you", "I hate you"]
specific_model(data)
