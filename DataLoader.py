import json
from datetime import datetime


class DataLoader:
    @staticmethod
    def load_json(path):
        with open(path, "r", encoding="utf-8") as f:
            return json.load(f)

    @staticmethod
    def parse_date(date_str):
        return datetime.fromisoformat(date_str).date()

    @staticmethod
    def calculate_cpa(spend, conversions):
        return spend / conversions if conversions > 0 else None


