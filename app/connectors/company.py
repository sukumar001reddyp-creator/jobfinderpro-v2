import requests
from bs4 import BeautifulSoup
from datetime import datetime
from .base import JobConnector
from app import db
from app.models.job import Job

class CompanyConnector(JobConnector):
    def fetch_jobs(self, keywords, location=None, limit=10):
        print(f"🔍 Fetching jobs for: {keywords}")
        jobs = []
        
        try:
            url = f"https://careers.google.com/jobs/results/?q={keywords.replace(' ', '+')}"
            headers = {'User-Agent': 'Mozilla/5.0 (compatible; JobFinderPro/1.0)'}
            response = requests.get(url, headers=headers, timeout=10)
            
            print(f"✅ Status Code: {response.status_code}")
            
            if response.status_code == 200:
                # Save demo job
                new_job = Job(
                    title="Senior Python Developer",
                    company="Google",
                    location="Hyderabad",
                    salary="₹20-35 LPA",
                    url="https://careers.google.com",
                    source="Google Careers",
                    posted_date=datetime.utcnow()
                )
                db.session.add(new_job)
                db.session.commit()
                print("✅ Job saved to database!")
                
        except Exception as e:
            print(f"❌ Error: {e}")
        
        return jobs[:limit]