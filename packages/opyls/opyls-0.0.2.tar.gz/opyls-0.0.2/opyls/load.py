from configparser import ConfigParser


# https://www.postgresqltutorial.com/postgresql-python/connect/
def load_ini(filename: str, section: str) -> dict:
    parser = ConfigParser()
    parser.read(filename)

    config = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            config[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))

    return config
