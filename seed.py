from pydantic import BaseModel, Field
from typing import Optional

class LeadCreate(BaseModel):
    company_name: str = Field(..., min_length=1)
    website: Optional[str] = ""
    contact_email: Optional[str] = ""
    industry: Optional[str] = ""
    estimated_refund: int = 0

class LeadOut(LeadCreate):
    id: int
    status: str

    class Config:
        from_attributes = True
