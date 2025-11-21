import yaml

def load_env(var):
    with open("secret.yml") as stream:
        try:
            return yaml.safe_load(stream)[var]
        except yaml.YAMLError as exc:
            print(exc)