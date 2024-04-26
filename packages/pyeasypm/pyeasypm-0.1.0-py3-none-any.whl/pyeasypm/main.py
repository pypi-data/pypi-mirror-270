import typer
import subprocess

app = typer.Typer()

@app.command()
def hello_world():
    print("hello world")

@app.command()
def pyprojsetup():
    print("Setting up:")
    # First arg
    pyversion = input("Which python version?")
    cmdp = "python"+ pyversion + " -m venv env"
    subprocess.run([cmdp], shell=True)
    subprocess.run(["source env/bin/activate"], shell=True)
    subprocess.run(["mkdir src"], shell=True)
    
    
    subprocess.run(["touch requirements.txt"], shell=True)


def projbuild():
    print("Building Project: (currently a placeholder for now)")
