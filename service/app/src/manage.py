from flask.cli import FlaskGroup
from register import application

cli = FlaskGroup(application)

@cli.command("placeholder")
def placeholder():
    print("placeholder")

if __name__ == "__main__":
    cli()