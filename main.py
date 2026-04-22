from sqlalchemy.orm import Session
from .models import Lead

SAMPLE_LEADS = [
    {
        "company_name": "Atlantic Auto Export",
        "website": "https://example.com",
        "contact_email": "ops@atlanticautoexport.com",
        "industry": "Auto Parts",
        "estimated_refund": 42000,
        "status": "new",
    },
    {
        "company_name": "Blue Ridge Components",
        "website": "https://example.com",
        "contact_email": "finance@blueridgecomponents.com",
        "industry": "Manufacturing",
        "estimated_refund": 18000,
        "status": "new",
    },
    {
        "company_name": "Carolina Industrial Supply",
        "website": "https://example.com",
        "contact_email": "owner@carolinaindustrial.com",
        "industry": "Machinery",
        "estimated_refund": 69000,
        "status": "queued",
    },
]

def seed_if_empty(db: Session) -> int:
    existing = db.query(Lead).count()
    if existing > 0:
        return 0
    for row in SAMPLE_LEADS:
        db.add(Lead(**row))
    db.commit()
    return len(SAMPLE_LEADS)
