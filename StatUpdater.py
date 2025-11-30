from apscheduler.schedulers.background import BackgroundScheduler
from DataLoader import DataLoader
from StatsDB import StatsDB

class StatsUpdater:
    def __init__(self, db: StatsDB, fb_file="fb_spend.json", net_file="network_conv.json"):
        self.db = db
        self.fb_file = fb_file
        self.net_file = net_file

    def fetch_and_update(self, start_date, end_date):
        data1 = DataLoader.load_json(self.fb_file)
        data2 = DataLoader.load_json(self.net_file)
        all_data = data1 + data2

        aggregated = {}
        for row in all_data:
            date = DataLoader.parse_date(row["date"])
            if not (start_date <= date <= end_date):
                continue
            key = (date.isoformat(), row["campaign_id"])
            if self.db.already_loaded(*key):
                continue
            if key not in aggregated:
                aggregated[key] = {"spend": 0, "conversions": 0}
            aggregated[key]["spend"] += row.get("spend", 0)
            aggregated[key]["conversions"] += row.get("conversions", 0)

        results = []
        for (date, campaign_id), vals in aggregated.items():
            spend = vals["spend"]
            conversions = vals["conversions"]
            cpa = DataLoader.calculate_cpa(spend, conversions)
            results.append((date, campaign_id, spend, conversions, cpa))

        self.db.upsert(results)
        print(f"Обновлено {len(results)} записів")

    def schedule_updates(self, start_date, end_date):
        scheduler = BackgroundScheduler()
        scheduler.add_job(self.fetch_and_update, "interval", hours=1,
                          args=[start_date, end_date],
                          max_instances=1)
        scheduler.start()
        print("Планувальник запущено. Оновлення кожну годину.")