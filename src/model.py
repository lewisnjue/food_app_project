# Use a pipeline as a high-level helper
from transformers import pipeline

pipe = pipeline("image-classification", model="lewisnjue/my_awesome_food_model")

