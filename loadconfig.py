import os


class Config:
    def __init__(self):
        # default db settings
        self.db_config = dict(
                  host='localhost',
                  user='root',
                  port=3306,
                  password='Huawei@123',
                  db='mypolls'
                )

        # default redis settings
        self.cache_config = dict(
                 host='127.0.0.1',
                 port=6379,
                 password='Huawei@123'
        )

        # load db settings from environment variables if set
        if os.environ.get('relational_database.parameters.db_host') is not None:
            self.db_config['host'] = os.environ.get('relational_database.parameters.db_host')

        if os.environ.get('relational_database.parameters.db_user') is not None:
            self.db_config['user'] = os.environ.get('relational_database.parameters.db_user')

        if os.environ.get('relational_database.parameters.db_port') is not None:
            self.db_config['port'] = int(os.environ.get('relational_database.parameters.db_port'))

        if os.environ.get('relational_database.parameters.password') is not None:
            self.db_config['password'] = os.environ.get('relational_database.parameters.password')

        if os.environ.get('relational_database.parameters.db_name') is not None:
            self.db_config['db'] = os.environ.get('relational_database.parameters.db_name')

        print(self.db_config)

        # load redis settings from environment variables if set
        if os.environ.get('distributed_session.parameters.host') is not None:
            self.cache_config['host'] = os.environ.get('distributed_session.parameters.host')

        if os.environ.get('distributed_session.parameters.port') is not None:
            self.cache_config['port'] = os.environ.get('distributed_session.parameters.port')

        if os.environ.get('distributed_session.parameters.password') is not None:
            self.cache_config['password'] = int(os.environ.get('distributed_session.parameters.password'))

        print(self.cache_config)

    def get_db_config(self):
        return self.db_config

    def get_cache_config(self):
        return self.cache_config
