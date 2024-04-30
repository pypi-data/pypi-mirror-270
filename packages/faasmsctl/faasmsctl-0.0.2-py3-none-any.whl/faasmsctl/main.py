from invoke import Program
from faasmsctl.tasks import task_ns
from faasmsctl.util.version import get_version


def main():
    program = Program(
        name="faasmctl",
        binary="faasmctl",
        binary_names=["faasmctl"],
        namespace=task_ns,
        version=get_version(),
    )
    program.run()
