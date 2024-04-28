from config import Config

configData = Config("config/defaultConfig.yaml")

print(list(configData.data.keys()))