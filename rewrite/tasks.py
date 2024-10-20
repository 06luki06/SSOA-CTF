# tasks.py

from invoke import task
import time

@task
def db(ctx):
    ctx.run("export PYTHONPATH=$(pwd)")
    ctx.run("docker compose down -v")
    print("Docker containers have been stopped.")
    time.sleep(1)
    ctx.run("docker compose up -d")
    time.sleep(3)
    ctx.run("python3 ./database/create_schema.py")
    time.sleep(1)
    ctx.run("python3 ./database/seed.py")
    time.sleep(1)

@task
def serve(ctx):
    ctx.run("uvicorn main:app --reload")

@task(pre=[db, serve])
def start(ctx):
    print("Application has started.")

