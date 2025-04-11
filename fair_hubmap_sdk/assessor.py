from typing import Dict, Optional
import requests
from pydantic import BaseModel

class FAIRReport(BaseModel):
    findable: float
    accessible: float
    interoperable: float
    reusable: float
    details: Dict[str, str]

class Assessor:
    def __init__(self, dataset_id: str, api_url: str = "https://portal.hubmapconsortium.org"):
        self.dataset_id = dataset_id
        self.api_url = api_url

    def evaluate(self) -> FAIRReport:
        """Evaluate FAIRness of a HuBMAP dataset."""
        metadata = self._fetch_metadata()
        report = self._assess_fairness(metadata)
        return report

    def _fetch_metadata(self) -> Dict:
        """Fetch dataset metadata from HuBMAP API."""
        try:
            response = requests.get(f"{self.api_url}/api/dataset/{self.dataset_id}")
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}

    def _assess_fairness(self, metadata: Dict) -> FAIRReport:
        """Assess FAIR metrics based on metadata."""
        
        # Placeholder logic
        findable = 0.8 if "doi" in metadata else 0.2
        accessible = 1.0 if metadata.get("is_public") else 0.5
        interoperable = 0.7 if metadata.get("ontology") else 0.3
        reusable = 0.9 if metadata.get("license") else 0.4
        details = {
            "findable": "DOI present" if findable > 0.5 else "No DOI",
            "accessible": "Public access" if accessible > 0.5 else "Restricted",
            "interoperable": "Uses ontology" if interoperable > 0.5 else "No ontology",
            "reusable": "License specified" if reusable > 0.5 else "No license",
        }
        return FAIRReport(
            findable=findable,
            accessible=accessible,
            interoperable=interoperable,
            reusable=reusable,
            details=details
        )