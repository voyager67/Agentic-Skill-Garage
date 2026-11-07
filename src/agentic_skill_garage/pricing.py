"""Cost estimates from explicit, user-maintained price cards. Never calls providers."""
from __future__ import annotations
import json
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import urlparse

def quote(rate_card: Path, provider: str, model: str, unit: str, quantity: Decimal):
    if not quantity.is_finite() or quantity < 0:
        return {"status":"INVALID_QUANTITY","reason":"Quantity must be a finite, non-negative decimal."}
    card=json.loads(Path(rate_card).read_text(encoding="utf-8"))
    matches=[r for r in card.get("rates",[]) if r.get("provider")==provider and r.get("model")==model and r.get("unit")==unit]
    if not matches: return {"status":"UNPRICED","reason":"No exact provider/model/unit rate exists in this price card."}
    if len(matches)>1: return {"status":"AMBIGUOUS","reason":"More than one rate matches; clean the price card before quoting."}
    rate=matches[0]; source=rate.get("source_url"); checked=rate.get("checked_at")
    parsed=urlparse(source or "")
    if parsed.scheme!="https" or not parsed.netloc or not checked:
        return {"status":"UNVERIFIED","reason":"A valid HTTPS source_url and timezone-aware checked_at timestamp are required."}
    try:
        price=Decimal(str(rate["price_per_unit"]))
        date=datetime.fromisoformat(checked.replace("Z","+00:00"))
        if date.tzinfo is None: raise ValueError("checked_at must include a timezone, e.g. +00:00 or Z")
        max_age=int(card.get("max_age_days",30))
    except (KeyError,ValueError,InvalidOperation,TypeError) as exc:
        return {"status":"INVALID_RATE","reason":str(exc)}
    if not price.is_finite() or price<0 or max_age<0:
        return {"status":"INVALID_RATE","reason":"Rate and max_age_days must be finite and non-negative."}
    now=datetime.now(timezone.utc); checked_at=date.astimezone(timezone.utc)
    age=(now-checked_at).total_seconds()/86400
    if age < -1: return {"status":"FUTURE_DATE","reason":"checked_at is more than 24 hours in the future."}
    if age>max_age: return {"status":"STALE","reason":f"Rate was checked {int(age)} days ago; refresh it before using."}
    currency=str(card.get("currency","USD"))
    total=(price*quantity).quantize(Decimal("0.0001"),rounding=ROUND_HALF_UP)
    return {"status":"ESTIMATE_ONLY","provider":provider,"model":model,"unit":unit,"quantity":str(quantity),"unit_price":str(price),"total":str(total),"currency":currency,"source_url":source,"checked_at":checked,"age_days":round(age,2),"approval_required":True}
