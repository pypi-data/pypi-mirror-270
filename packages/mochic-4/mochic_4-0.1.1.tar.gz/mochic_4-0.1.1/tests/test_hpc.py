import os
import pytest
import dotenv
import fabric
import uuid
from mochic_4 import hpc

hpc.logger.setLevel("DEBUG")

dotenv.load_dotenv()

username = os.getenv("MOCHIC_HPC_USERNAME")
email_address = os.getenv("MOCHIC_HPC_EMAIL_ADDRESS") or ""
user_dir = f"/home/{username}"

exp_dir_root = os.environ.get("MOCHIC_SESSION_EXP_DIR_ROOT") or ""
output_dir = os.environ.get("MOCHIC_HPC_OUTPUT_DIR") or ""

test_job_id_0 = uuid.uuid4().hex
test_job_id_1 = uuid.uuid4().hex

@pytest.mark.e2e
@pytest.mark.parametrize("args", [
    # simple test
    (
        hpc.HPCJob(
            name=f"mochic-4_test-job_{test_job_id_0}",
            email_address=email_address,
            entry_point="echo 'Hello, World!'",
            output_path=f"{user_dir}/job-logs-dev/mochic-4_test-job_{test_job_id_0}.log",
        ),
        f"{user_dir}/jobs-dev",
    ),
    (
        hpc.HPCJob(
            name=f"mochic-4_test-job_{test_job_id_1}",
            email_address=email_address,
            entry_point=" ".join([
                "np-upload-validation",
                "--debug",
                "batch-validate-sessions",
                f'"{exp_dir_root}"',  # in case of spaces in path
                "--output-dir",
                f'"{output_dir}"',
            ]),
            output_path=f"{user_dir}/job-logs-dev/mochic-4_test-job_{test_job_id_1}.log",
            sif_context=hpc.SIFContext(
                sif_path=os.environ.get("HPC_SIF_PATH") or "",
                env_vars=[
                    (
                        "CODE_OCEAN_API_TOKEN",
                        os.getenv("CODE_OCEAN_API_TOKEN"),
                    ),
                    (
                        "CODE_OCEAN_DOMAIN",
                        os.getenv("CODE_OCEAN_DOMAIN"),
                    ),
                    (
                        "AWS_ACCESS_KEY_ID",
                        os.getenv("AWS_ACCESS_KEY_ID"),
                    ),
                    (
                        "AWS_SECRET_ACCESS_KEY",
                        os.getenv("AWS_SECRET_ACCESS_KEY"),
                    ),
                    (
                        "AWS_DEFAULT_REGION",
                        os.getenv("AWS_DEFAULT_REGION"),
                    ),
                ]
            )
        ),
        f"{user_dir}/jobs-dev",
    ),
])
def test_trigger_hpc_job(args) -> None:
    with fabric.Connection(
        host=os.getenv("MOCHIC_HPC_HOST"),
        user=username,
        connect_kwargs={
            "password": os.getenv("MOCHIC_HPC_PASSWORD")
        }
    ) as con:
        hpc.trigger_hpc_job(con, *args)
