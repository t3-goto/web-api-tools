import nox


def install_dependencies(session):
    session.run("poetry", "install", external=True)


@nox.session
def tests(session):
    install_dependencies(session)
    session.run("poetry", "run", "pytest", external=True)


@nox.session
def lint(session):
    install_dependencies(session)
    session.run("poetry", "run", "flake8", external=True)


@nox.session
def format(session):
    install_dependencies(session)
    session.run(
        "poetry", "run", "isort", "--profile", "black", ".", external=True
    )
    session.run("poetry", "run", "black", ".", external=True)


# @nox.session
# def type_check(session):
#     install_dependencies(session)
#     session.run("poetry", "run", "mypy", ".", external=True)
