import os


class Config:
    def __init__(self):
        # default db settings
        self.db_config = dict(
                  host='localhost',
                  user='root',
                  port=3306,
                  password='password',
                  db='mypolls'
                )

        # default redis settings
        self.cache_config = dict(
                 host='127.0.0.1',
                 port=6379,
                 password='password'
        )

        # load db settings from environment variables if set
        if os.environ.get('relational_database_parameters_db_host') is not None:
            self.db_config['host'] = os.environ.get('relational_database_parameters_db_host')

        if os.environ.get('relational_database_parameters_db_user') is not None:
            self.db_config['user'] = os.environ.get('relational_database_parameters_db_user')

        if os.environ.get('relational_database_parameters_db_port') is not None:
            self.db_config['port'] = int(os.environ.get('relational_database_parameters_db_port'))

        if os.environ.get('relational_database_parameters_password') is not None:
            self.db_config['password'] = os.environ.get('relational_database_parameters_password')

        if os.environ.get('relational_database_parameters_db_name') is not None:
            self.db_config['db'] = os.environ.get('relational_database_parameters_db_name')

        # print(self.db_config)

        # load redis settings from environment variables if set
        if os.environ.get('distributed_session_parameters_host') is not None:
            self.cache_config['host'] = os.environ.get('distributed_session_parameters_host')

        if os.environ.get('distributed_session_parameters_port') is not None:
            self.cache_config['port'] = os.environ.get('distributed_session_parameters_port')

        if os.environ.get('distributed_session_parameters_password') is not None:
            self.cache_config['password'] = os.environ.get('distributed_session_parameters_password')

        # print(self.cache_config)

    def get_db_config(self):
        return self.db_config

    def get_cache_config(self):
        return self.cache_config
