import nox

@nox.session(python=["3.10.12", "3.11.4"])
def tests(session):
    session.install("-r", "requirements.txt", "pytest")
    session.run("pytest")
