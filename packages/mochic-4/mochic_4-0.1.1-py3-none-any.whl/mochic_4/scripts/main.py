# import datetime
# import json
# import logging
# import os
# import pathlib
# import typing

# import click
# import dotenv
# import fabric

# from mochic_4 import hpc

# dotenv.load_dotenv()


# logger = logging.getLogger(__name__)

# timestamp = datetime.datetime.now()
# base_filename = f"np-upload-validation_{timestamp.strftime('%Y%m%d_%H%M%S')}"


# @click.group()
# @click.option("--debug/--no-debug", default=False)
# @click.option("--log-to-file", default=False, is_flag=True)
# def cli(debug: bool, log_to_file: bool) -> None:
#     click.echo(f"Debug mode is {'on' if debug else 'off'}")
#     if debug:
#         hpc.logger.setLevel(logging.DEBUG)
#         logger.setLevel(logging.DEBUG)

#     if log_to_file:
#         log_path = f"{base_filename}.log"
#         click.echo(f"Logging to file: {log_path}")
#         file_handler = logging.FileHandler(log_path)
#         file_handler.setLevel(logging.DEBUG)
#         formatter = logging.Formatter(
#             "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
#         )
#         file_handler.setFormatter(formatter)
#         hpc.logger.addHandler(file_handler)
#         logger.addHandler(file_handler)


# @cli.command()
# @click.argument("job-path", type=pathlib.Path)
# @click.option("--jobs-dir", default="./jobs", type=str)
# def trigger_hpc_job(
#     job_path: pathlib.Path,
#     jobs_dir: str,
# ) -> None:
#     job = hpc.HPCJob(
#         name=job_name,
#         email_address=email_

#     with fabric.Connection(
#         host=os.getenv("MOCHIC_4_HPC_HOST"),
#         user=os.getenv("MOCHIC_4_HPC_USER"),
#         connect_kwargs={
#             "password": os.getenv("MOCHIC_4_HPC_PASSWORD"),
#         },
#     ) as con:
#         slurm_id, job_id = hpc.trigger_hpc_job(con, job, jobs_dir)
#         click.echo(f"Job {job_id} submitted with SLURM ID {slurm_id}")
