import yaml


def get_config():
    with open("config.yaml", "r") as yml:
        return yaml.safe_load(yml)