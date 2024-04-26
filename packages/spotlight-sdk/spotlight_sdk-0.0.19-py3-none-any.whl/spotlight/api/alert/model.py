from datetime import datetime
from typing import Optional

from pydantic import Field

from spotlight.core.common.base import Base
from spotlight.core.common.enum import IntervalType, NotificationType


class AlertRequest(Base):
    display_name: str
    description: Optional[str] = Field(default=None)
    data_rule_id: str
    interval_type: IntervalType
    interval: int
    notification_type: NotificationType
    notification_source: str


class AlertResponse(Base):
    id: str
    display_name: str
    description: Optional[str]
    data_rule_id: str
    interval_type: IntervalType
    interval: int
    notification_type: NotificationType
    notification_source: str
    created_by: str
    created_at: datetime
    updated_by: Optional[str]
    updated_at: Optional[int]
