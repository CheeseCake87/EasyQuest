from datetime import datetime
from datetime import timedelta

from pytz import timezone
from sqlalchemy import schema, types, select, update, insert

from app import db


def dater(ltz: str = "Europe/London", mask: str = "%Y-%m-%d %H:%M:%S", days_delta: int = 0) -> datetime:
    local_tz = timezone(ltz)
    if days_delta < 0:
        apply_delta = (datetime.now(local_tz) - timedelta(days=abs(days_delta))).strftime(mask)
        return datetime.strptime(apply_delta, mask)
    if days_delta > 0:
        apply_delta = (datetime.now(local_tz) + timedelta(days=days_delta)).strftime(mask)
        return datetime.strptime(apply_delta, mask)
    return datetime.strptime(datetime.now(local_tz).strftime(mask), mask)


def forkey(table_dot_field: str) -> schema.Column:
    return schema.Column(types.Integer, schema.ForeignKey(table_dot_field), nullable=False)


__all__ = ["db", "dater", "forkey", "schema", "types", "select", "update", "insert"]
