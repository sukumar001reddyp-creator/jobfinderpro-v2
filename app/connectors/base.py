from abc import ABC, abstractmethod

class JobConnector(ABC):
    @abstractmethod
    def fetch_jobs(self, keywords, location=None, limit=10):
        pass