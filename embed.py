import os
from embedchain import App

# load embedding model configuration from config.yaml file
app = App.from_config(config_path="config.yaml")
app.add('titanic.csv', data_type='csv')
response = app.query("Donne moi le nombre de male et female")
print(response)