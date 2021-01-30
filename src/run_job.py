from askanna import run

"""
askanna.core.exceptions.PostError: 404 - Something went wrong while starting a run: Not Found
"""

json_data = {"example": "payload-python"}
run_info = run.start(job_name="hello", data=json_data)
