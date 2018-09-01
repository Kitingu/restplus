# from flask.ext.script import Manager, Server
from restApi.app import create_app
config_name="development"
app=create_app(config_mame=config_name)
# manager=Manager(client)
# manager.add_command("runserver",Server(
#     use_debugger=True,
#     use_reloader=True,
#     host=os.getenv('0.0.0.0'),
#     port=int(5000)
# ))
if __name__ == '__main__':
    app.run()