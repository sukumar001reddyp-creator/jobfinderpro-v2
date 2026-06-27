from apscheduler.schedulers.background import BackgroundScheduler
from app.connectors.company import CompanyConnector

scheduler = BackgroundScheduler()

def fetch_jobs_task():
    connector = CompanyConnector()
    jobs = connector.fetch_jobs("python developer", limit=20)
    print(f"Fetched {len(jobs)} jobs")

scheduler.add_job(fetch_jobs_task, 'interval', hours=6)
scheduler.start()