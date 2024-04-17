import yaml


class Config:
    def __init__(self, config_file_path):
        self.file_path = config_file_path
        self.data = self.load_data()

    def load_data(self):
        try:
            with open('config.yaml', 'r') as file:
                data = yaml.safe_load(file)
            return data
        except FileNotFoundError:
            print(f"Error: File '{self.file_path}' not found.")
            return None
        except yaml.error:
            print(f"Error: From File '{self.file_path}'.")
            return None

    def get_value(self, category, key):
        if self.data:
            if category in self.data:
                if key in self.data[category]:
                    return self.data[category][key]
                else:
                    print(f"Error: Key '{key}' not found in '{category}'")
                    return None                   
            else:
                print(f"Error: Category '{category}' not found in the yaml data.")
                return None
        else:
            print("Error: No data loaded.")
            return None
