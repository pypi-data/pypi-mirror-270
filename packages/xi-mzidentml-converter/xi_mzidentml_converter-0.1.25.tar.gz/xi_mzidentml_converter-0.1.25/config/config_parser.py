from configparser import ConfigParser
import os


def parse_config(filename, section='postgresql'):
    # create a parser
    parser = ConfigParser()
    # read config file
    parser.read(filename)

    # get section, default to postgresql
    configs = {}
    if parser.has_section(section):
        params = parser.items(section)
        for param in params:
            configs[param[0]] = param[1]
    else:
        raise Exception('Section {0} not found in the {1} file'.format(section, filename))
    return configs


def get_conn_str():
    """
    Get database related configurations
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config = os.environ.get('DB_CONFIG', os.path.join(script_dir, "database.ini"))
    db_info = parse_config(config)
    hostname = os.environ.get('DB_HOST') or db_info.get("host")
    database = os.environ.get('DB_DATABASE_NAME') or db_info.get("database")
    username = os.environ.get('DB_USER') or db_info.get("user")
    password = os.environ.get('DB_PASSWORD') or db_info.get("password")
    port = os.environ.get('DB_PORT') or db_info.get("port")
    conn_str = f"postgresql://{username}:{password}@{hostname}:{port}/{database}"
    return conn_str


# def security_API_key():
#     config = os.environ.get('DB_CONFIG', '../database.ini')
#     security_info = parse_config(config, 'security')
#     apikey = security_info.get("apikey")
#     return apikey


def get_api_configs():
    """
    Get API related configurations
    """
    script_dir = os.path.dirname(os.path.abspath(__file__))
    config = os.environ.get('DB_CONFIG', os.path.join(script_dir, "database.ini"))
    api_configs = parse_config(config, "api")
    config= {"base_url": os.environ.get('BASE_URL') or api_configs.get("base_url"),
             "api_key": os.environ.get('API_KEY') or api_configs.get("api_key"),
             "api_key_value": os.environ.get('API_KEY_VALUE') or api_configs.get("api_key_value")}
    return config
