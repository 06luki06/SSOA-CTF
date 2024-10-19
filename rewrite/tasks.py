# tasks.py

from invoke import task

@task
def docker_up(ctx):
    ctx.run("docker compose up -d")

@task
def clear_db(ctx):
    ctx.run("python3 clear_db.py")

@task
def create_schema(ctx):
    ctx.run("python3 create_schema.py")

@task(pre=[clear_db, create_schema])
def seed(ctx):
    ctx.run("python3 seed.py")

@task(pre=[seed])
def serve(ctx):
    ctx.run("uvicorn main:app --reload")

@task(pre=[docker_up, serve])
def start(ctx):
    print("Application has started.")

@task
def docker_down(ctx):
    ctx.run("docker compose down")
    print("Docker containers have been stopped.")
