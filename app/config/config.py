import os
import re
import yaml
import collections.abc

from constants import CONFIG_DIR_PATH


# https://stackoverflow.com/questions/3232943/update-value-of-a-nested-dictionary-of-varying-depth
def _update(d, u):
    for k, v in u.items():
        if isinstance(v, collections.abc.Mapping):
            d[k] = _update(d.get(k, {}), v)
        else:
            d[k] = v
    return d


# https://medium.com/swlh/python-yaml-configuration-with-environment-variables-parsing-77930f4273ac
def parse_config(basepath, tag='!ENV'):
    """
    Load a yaml configuration file and resolve any environment variables
    The environment variables must have !ENV before them and be in this format
    to be parsed: ${VAR_NAME}.
    E.g.:
    database:
        host: !ENV ${HOST}
        port: !ENV ${PORT}
    app:
        log_path: !ENV '/var/${LOG_PATH}'
        something_else: !ENV '${AWESOME_ENV_VAR}/var/${A_SECOND_AWESOME_VAR}'
    :param str basepath: the path to the yaml files
    :param str tag: the tag to look for
    :return: the dict configuration
    :rtype: dict[str, T]
    """
    # pattern for global vars: look for ${word}
    pattern = re.compile('.*?\${(\w+)}.*?')
    loader = yaml.SafeLoader

    # the tag will be used to mark where to start searching for the pattern
    # e.g. somekey: !ENV somestring${MYENVVAR}blah blah blah
    loader.add_implicit_resolver(tag, pattern, None)

    def constructor_env_variables(loader, node):
        """
        Extracts the environment variable from the node's value
        :param yaml.Loader loader: the yaml loader
        :param node: the current node in the yaml
        :return: the parsed string that contains the value of the environment
        variable
        """
        value = loader.construct_scalar(node)
        match = pattern.findall(value)  # to find all env variables in line
        if match:
            full_value = value
            for g in match:
                full_value = full_value.replace(
                    f'${{{g}}}', os.environ.get(g, g)
                )
            return full_value
        return value

    loader.add_constructor(tag, constructor_env_variables)

    with open(os.path.join(basepath, "base.yaml")) as conf_data:
        base_yaml = yaml.load(conf_data, Loader=loader)
    if os.environ.get("PYTHONDEVMODE", "0") == "1":
        with open(os.path.join(basepath, "dev.yaml")) as conf_data:
            update_yaml = yaml.load(conf_data, Loader=loader)
    else:
        with open(os.path.join(basepath, "production.yaml")) as conf_data:
            update_yaml = yaml.load(conf_data, Loader=loader)
    return _update(base_yaml, update_yaml)


class DB:
    def __init__(self, db):
        self.db = db

    @property
    def dir_location(self):
        return self.db['dirlocation']

    def __repr__(self):
        return str(self.db)

    def __str__(self):
        return str(self.db)


class Server:
    def __init__(self, server):
        self.server = server

    @property
    def host(self):
        return self.server['host']

    @property
    def port(self):
        return self.server['port']

    def __repr__(self):
        return str(self.server)

    def __str__(self):
        return str(self.server)


class Config:
    def __init__(self):
        self.config = parse_config(CONFIG_DIR_PATH)
        self.db = DB(self.config['db'])
        self.server = Server(self.config['server'])

    def __repr__(self):
        return str(self.config)

    def __str__(self):
        return str(self.config)
