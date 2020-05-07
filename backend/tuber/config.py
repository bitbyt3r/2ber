import json
import os

conf = {
    "verbose": False,
    "flask_env": "development",
    "static_path": os.path.abspath("../dist"),
    "migrations_path": "migrations",
    "alembic_ini": "alembic.ini",
    "database_url": "sqlite:///database.db",
    "session_duration": 7200,
    "uber_api_token": "",
    "uber_api_url": "",
    "config": "/etc/tuber/tuber.json",
    "background_tasks": False,
    "sentry_dsn": "",
    "csp_directives": "",
    "force_https": False,
}

environment = {}
for i in conf.keys():
    if i.upper() in os.environ:
        environment[i] = os.environ[i.upper()]

conf.update(environment)
if os.path.isfile("./tuber.json") and not os.path.isfile(conf['config']):
    print("Reading from config file: {}".format("./tuber.json"))
    with open("./tuber.json", "r") as FILE:
        configfile = json.loads(FILE.read())
    configfile.update(environment)
    conf.update(configfile)

if os.path.isfile(conf['config']):
    print("Reading from config file: {}".format(conf['config']))
    with open(conf['config'], "r") as FILE:
        configfile = json.loads(FILE.read())
    configfile.update(environment)
    conf.update(configfile)

for i in ["verbose", "background_tasks", "force_https"]:
    if isinstance(conf[i], str):
        conf[i] = conf[i].lower() == "true"

for i in conf:
    vars()[i] = conf[i]
    print("{}: {}".format(i, conf[i]))