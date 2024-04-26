import logging
import re
import tempfile
import typing

import fabric
import pydantic

logging.basicConfig()
logger = logging.getLogger(__name__)


EnvVar = tuple[str, str]


class SIFContext(pydantic.BaseModel):

    sif_path: str
    env_vars: typing.Optional[list[EnvVar]]


class HPCJob(pydantic.BaseModel):

    name: str
    email_address: str
    entry_point: str
    mem_size: int = 12
    output_path: typing.Optional[str] = None
    sif_context: typing.Optional[SIFContext] = None


def _build_singularity_exec(
    context: SIFContext,
) -> str:
    """Builds the singularity exec command from context."""
    _cmd = [
        "singularity",
        "exec",
        "--cleanenv",
    ]
    if context.env_vars:
        _cmd.extend([f"--env {k}={v}" for k, v in context.env_vars])

    _cmd.append(context.sif_path)

    return " ".join(_cmd)


def generate_hpc_job_content(
    job: HPCJob,
) -> str:
    """Generates the content of an hpc job script."""
    if job.sif_context is not None:
        _exec = f"{_build_singularity_exec(job.sif_context)} {job.entry_point}"
    else:
        _exec = job.entry_point

    if job.output_path is None:
        output_path = f"{job.name}.log"
    else:
        output_path = job.output_path

    # parsing is highly succeptible to newline characters causing errors, TODO: use a list?
    return f"""#!/bin/bash
#SBATCH --job-name={job.name}                               # Job name
#SBATCH --mail-type=END,FAIL                                # Mail events (NONE, BEGIN, END, FAIL, ALL)
#SBATCH --mail-user={job.email_address}                         # Where to send mail
#SBATCH --ntasks=1                                          # Run on a single CPU
#SBATCH --mem={job.mem_size}gb                                           # Job memory request (per node)
#SBATCH --time=10:00:00                                     # Time limit hrs:min:sec
#SBATCH --output='{output_path}'                            # Standard output and error log
#SBATCH --partition braintv                                 # Partition used for processing
#SBATCH --tmp=100M                                          # Request the amount of space your jobs needs on /scratch/fast

pwd; hostname; date

echo 'Running {job.name} job on a single thread'

{_exec}

date
    """


def _write_to_host(
    con: fabric.Connection,
    content: str,
    remote_path: str,
) -> None:
    """Writes content to a file on the remote host.
    Notes
    -----
    - windows isnt supported?, no posixpath
    """
    with tempfile.NamedTemporaryFile(mode="w+") as temp:
        temp.write(content)
        temp.seek(0)
        result = con.put(temp.name, remote_path)

    if not result:
        raise Exception(f"Failed to transfer to host: {result}")


def get_remote_content(
    con: fabric.Connection,
    filepath: str,
) -> str:
    """Gets the content of a file on the remote host."""
    return con.run(f"cat {filepath}", hide=True).stdout.strip()


def trigger_hpc_job(
    con: fabric.Connection,
    job: HPCJob,
    jobs_dir: typing.Optional[str],
) -> tuple[str, str]:
    """Runs a job on the HPC."""
    job_content = generate_hpc_job_content(job)
    job_script_path = f"{jobs_dir}/{job.name}.sh"
    logger.debug("job_script_path: %s" % job_script_path)
    _write_to_host(
        con,
        job_content,
        job_script_path,
    )
    logger.info("Triggering job...")
    result = con.run(f"sbatch {job_script_path}", hide=True)
    result_output = result.stdout.strip()
    logger.debug("result_output: %s" % result_output)
    matches = re.match(r"Submitted batch job (\d+)", result_output)
    if matches is None or len(matches.groups()) < 1:
        raise Exception("Failed to find job id: %s" % result_output)
    slurm_job_id = matches.group(1)
    logger.debug("Parsed slurm_job_id: %s" % slurm_job_id)

    return slurm_job_id, job.name
