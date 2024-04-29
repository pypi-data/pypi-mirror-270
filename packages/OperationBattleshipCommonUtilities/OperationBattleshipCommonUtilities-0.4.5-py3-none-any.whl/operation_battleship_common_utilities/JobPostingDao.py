import os
import pandas as pd
import psycopg2
import logging
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv('.env')

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class JobPostingDao:
    def __init__(self):
        self.db_params = {
            "host": os.getenv("host"),
            "database": os.getenv("database"),
            "user": os.getenv("digitalOcean"),
            "password": os.getenv("password"),
            "port": os.getenv("port")
        }
        logging.info(f"{self.__class__.__name__} class initialized")

    def execute_query(self, sql, data=None, fetch=True):
        """
        General function to execute a database query
        Returns a DataFrame if fetch=True, otherwise None.
        """
        try:
            with psycopg2.connect(**self.db_params) as conn:
                with conn.cursor() as cur:
                    cur.execute(sql, data)
                    if fetch:
                        rows = cur.fetchall()
                        if rows:
                            return pd.DataFrame(rows, columns=[desc[0] for desc in cur.description])
                        return pd.DataFrame()
                    else:
                        conn.commit()
        except Exception as e:
            logging.error(f"Database error during query execution: {e}")
            return None

    def get_all_data_science_or_product_jobs(self):
        sql = "SELECT * FROM job_postings WHERE job_category IN ('Product_Management', 'Data_Science')"
        return self.execute_query(sql)

    def get_all_product_manager_jobs(self):
        sql = "SELECT * FROM job_postings WHERE job_title ILIKE '%AI%' OR job_title ILIKE '%Product Manager%'"
        return self.execute_query(sql)

    def update_linkedin_job_record_updated_date(self, job_url):
        sql = """
        UPDATE job_postings
        SET job_last_collected_date = %s
        WHERE posting_url = %s;
        """
        todays_date = datetime.now().replace(hour=0, minute=0, second=0, microsecond=0).strftime('%Y-%m-%d %H:%M:%S')
        data = (todays_date, job_url)
        result = self.execute_query(sql, data, fetch=False)
        return "Update successful!" if result is not None else None

    def update_job_posting(self, job_posting):
        set_sql = ', '.join([f"{col} = %s" for col in job_posting.index if col != 'job_posting_id'])
        sql = f"UPDATE job_postings SET {set_sql} WHERE job_posting_id = %s;"
        data = tuple(job_posting[col] for col in job_posting.index if col != 'job_posting_id') + (job_posting['job_posting_id'],)
        return self.execute_query(sql, data, fetch=False)

    def fetch_jobs_requiring_enrichment(self):
        sql = "SELECT * FROM job_postings WHERE is_ai IS NULL"
        return self.execute_query(sql)

    def check_if_job_exists(self, cleaned_linkedin_job_url):
        sql = "SELECT 1 FROM job_postings WHERE posting_url = %s"
        result = self.execute_query(sql, (cleaned_linkedin_job_url,), fetch=True)
        return not result.empty

    def insert_new_job_record(self, job_posting):
        columns = job_posting.columns.tolist()
        placeholders = ', '.join(['%s' for _ in columns])
        column_names = ', '.join(columns)
        sql = f"INSERT INTO job_postings ({column_names}) VALUES ({placeholders})"
        data = tuple(job_posting.iloc[0])
        result = self.execute_query(sql, data, fetch=False)
        return "Insert successful!" if result is not None else None

    def get_all_jobs(self):
        sql = "SELECT * FROM job_postings"
        return self.execute_query(sql)

    def get_active_jobs_ids_as_dataframe(self):
        sql = "SELECT * FROM job_postings WHERE job_active = true"
        return self.execute_query(sql)

    def get_job_by_job_posting_id(self, job_posting_id):
        sql = "SELECT * FROM job_postings WHERE job_posting_id = %s"
        return self.execute_query(sql, (job_posting_id,))
