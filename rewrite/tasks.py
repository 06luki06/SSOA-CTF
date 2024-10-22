# tasks.py

from invoke import task
import time
import platform

@task
def db(ctx):
    ctx.run("docker compose down -v")
    print("Docker containers have been stopped.")
    time.sleep(1)
    ctx.run("docker compose up -d")
    time.sleep(3)
    
        # Determine platform-specific command for setting PYTHONPATH
    if platform.system() == "Windows":
        pythonpath_command = "set PYTHONPATH=%cd% &&"
    else:
        pythonpath_command = "PYTHONPATH=$(pwd)"

    ctx.run(f"{pythonpath_command} python ./database/create_schema.py")
    time.sleep(1)
    ctx.run(f"{pythonpath_command} python ./database/seed.py")
    time.sleep(1)
    
@task
def serve(ctx):
    ctx.run("uvicorn main:app --reload")

@task(pre=[db, serve])
def start(ctx):
    print("Application has started.")

