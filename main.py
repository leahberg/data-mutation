import sqlite3

# Create SQLite table postings
with sqlite3.connect("data_mutation.db") as conn:
    cursor = conn.cursor()

    create_table_query = """CREATE TABLE IF NOT EXISTS postings
         (job_id INT PRIMARY KEY NOT NULL,
         company_name       TEXT,
         title              TEXT,
         description        TEXT,
         max_salary         INT,
         pay_period         TEXT,
         location           TEXT,
         company_id         INT,
         views              INT,
         med_salary         INT,
         min_salary         INT,
         formatted_work_type TEXT,
         applies            INT,
         original_listed_time DATETIME,
         remote_allowed     INT,
         job_posting_url    TEXT,
         application_url    TEXT,
         application_type   TEXT,
         expiry             DATETIME,
         closed_time        DATETIME,
         formatted_experience_level TEXT,
         skills_desc        TEXT,
         listed_time        DATETIME,
         posting_domain     TEXT,
         sponsored          INT,
         work_type          TEXT,
         currency           TEXT,
         compensation_type  TEXT,
         normalized_salary  INT,
         zip_code           INT,
         fips               INT
         );"""

    cursor.execute(create_table_query)

    # validate
    cursor.execute("PRAGMA table_info(postings)")
    print(cursor.fetchall())
