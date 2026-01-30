from enum import Enum 

class ReportType(str, Enum):
    realtime = "realtime"
    cached = "cached"

class ReportInterval(str, Enum):
    hourly = "hourly"
    daily = "daily"
    monthly = "monthly"
    annually = "annually"

class ReportStatus(str, Enum):
    active = "active"
    inactive = "inactive"

class UserRole(str, Enum):
    user = "user"
    admin = "admin"