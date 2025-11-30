import sqlite3

class StatsDB:
    def __init__(self, db_path="stats.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS daily_stats (
                date TEXT,
                campaign_id TEXT,
                spend REAL,
                conversions INTEGER,
                cpa REAL,
                PRIMARY KEY(date, campaign_id)
            )
        """)
        conn.commit()
        conn.close()

    def already_loaded(self, date, campaign_id):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        cur.execute("SELECT spend, conversions FROM daily_stats WHERE date=? AND campaign_id=?", (date, campaign_id))
        row = cur.fetchone()
        conn.close()
        if not row:
            return False
        spend, conversions = row
        return not (spend == 0 or conversions == 0)

    def upsert(self, results):
        conn = sqlite3.connect(self.db_path)
        cur = conn.cursor()
        for row in results:
            cur.execute("""
                INSERT INTO daily_stats (date, campaign_id, spend, conversions, cpa)
                VALUES (?, ?, ?, ?, ?)
                ON CONFLICT(date, campaign_id) DO UPDATE SET
                    spend=excluded.spend,
                    conversions=excluded.conversions,
                    cpa=excluded.cpa
            """, row)
        conn.commit()
        conn.close()


