from StatsDB import StatsDB
from DataLoader import DataLoader
from StatUpdater import StatsUpdater

def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--start-date", required=True)
    parser.add_argument("--end-date", required=True)
    parser.add_argument("--schedule", action="store_true")
    args = parser.parse_args()

    db = StatsDB()
    updater = StatsUpdater(db)

    start_date = DataLoader.parse_date(args.start_date)
    end_date = DataLoader.parse_date(args.end_date)

    if args.schedule:
        updater.schedule_updates(start_date, end_date)
    else:
        updater.fetch_and_update(start_date, end_date)
