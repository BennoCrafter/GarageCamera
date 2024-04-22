exampleData = {"discord":{"token": "1234ff", "channel": 12345}, "general": {"image_data": {"scale": {"width": 100, "height": 200}, "type": "lol"}}, "homeassistant": {"token": "12"}}

print(exampleData["general"]["image_data"]["type"])
print(list(exampleData.keys()))