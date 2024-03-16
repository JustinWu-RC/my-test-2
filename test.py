from prefect import flow, task
from prefect.filesystems import RemoteFileSystem

rfs = RemoteFileSystem.load("prefect-bucket")


@task(log_prints=True)
def test_task():
    print(rfs.read_path("CallNote Dataset - 40 - Sheet1.csv"))


@flow(log_prints=True)
def test_flow():
    test_task()


if __name__ == "__main__":
    test_flow.from_source(
        source=rfs,
        entrypoint="test.py:test_flow"
    ).deploy(
        name="test s3 storage 2",
        work_pool_name="default-agent-pool",
        work_queue_name="DefaultAgentQueue",
    )

