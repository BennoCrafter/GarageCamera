import argparse
import yaml


class EditConfig:
    def __init__(self, yaml_key, yaml_value, filename):
        self.yaml_key = yaml_key
        self.yaml_value = yaml_value
        self.filename = filename

        self.data = self.load_data(file_path=self.filename)

        self.run()

    def run(self):  
        print(f"Changing {self.yaml_key.split(';')} to {self.yaml_value} in file {self.filename.split('/')[-1]}")
        new_data = self.change_settings(self.data, self.yaml_key.split(";"), self.yaml_value)
        self.save_data(new_data)

    def load_data(self, file_path):
        try:
            with open(file_path, 'r') as file:
                data = yaml.safe_load(file)
            return data
        except FileNotFoundError:
            print(f"Error: File '{self.file_path}' not found.")
            return None
        except yaml.error:
            print(f"Error: From File '{self.file_path}'.")
            return None
        
    def change_settings(self, data, keys_list, new_value):
        current_dict = data
        for key in keys_list[:-1]:
            current_dict = current_dict.get(key, {})
        
        current_dict[keys_list[-1]] = new_value
        return data

    def save_data(self, d):
        with open(self.filename, 'w') as file:
            yaml.dump(d, file)
        
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Edit the settings via command line")
    parser.add_argument("-k", "--key", type=str, help="Sets the key. (Use ';' for diving one category deeper)")
    parser.add_argument("-v", "--value", type=str, help="Sets the value.")
    parser.add_argument("-fn", "--filename", type=str, help="Sets the file path.", default="config/config.yaml")

    args = parser.parse_args()
    
    if args.key and args.value:
        config_editor = EditConfig(args.key, args.value, args.filename)
    else:
        print("Please provide missing arguments.")
