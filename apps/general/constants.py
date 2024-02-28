import environ

env = environ.Env()

OMDb_API_KEY = env("OMDb_API_KEY", default="Enter your key")
