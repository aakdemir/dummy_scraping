import json
import psycopg2
from psycopg2 import sql

# Example query function to fetch data from a table
def fetch_data_from_table(self):
    try:
        cursor = self.cur
        query = sql.SQL("SELECT * FROM jobs")
        cursor.execute(query)
        rows = cursor.fetchall()
        write_to_json(self, rows)
        return rows
    except psycopg2.Error as e:
        print("Error executing query:", e)
        return None

def write_to_json(self, data):
        # Define the path to the JSON file
        json_file_path = 'selectedJobsOutput.json'

        # Open the JSON file in write mode
        with open(json_file_path, 'w') as json_file:
            # Iterate over each row of data and write it to the JSON file
            json.dump(data, json_file, indent=4)

        self.logger.info(f"Data written to {json_file_path}")

# # Example function to insert data into a table
def insert_data_into_table(self, item):
    try:
         ## Create quotes table if none exists
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS jobs(
            id serial PRIMARY KEY, 
            title text,
            description text,
            city VARCHAR(255),              
            country VARCHAR(255)
        )
        """)

         ## Define insert statement
        self.cur.execute(""" insert into jobs (title, description, city, country) values (%s,%s,%s,%s)""", (
            str(item["title"]),
            str(item["description"]),
            item["city"],
            item["country"],
        ))

    except psycopg2.Error as e:
        conn.rollback()
        print("Error inserting data:", e)

# Define any other query functions as needed
