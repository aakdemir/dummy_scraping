import scrapy
import json
from jobs_project.items import JobsProjectItem

from jobs_project.pipelines import JobsProjectPipeline

class JsonSpider(scrapy.Spider):
    name = 'json_spider'
    custom_settings = {
        'ITEM_PIPELINES': {
            'jobs_project.pipelines.JobsProjectPipeline': 300
        },
    }

    def start_requests(self):
        # Specify the path to your local file
        file_path = 'D:/Projeler/Python Projeleri/jobs_project/jobs_project/resources/s03.json'

        # Construct the URL with the file:// scheme
        url = 'file://' + file_path

        # Create a request with the constructed URL
        yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # Handle the response here
        # Parse the JSON response
        data = json.loads(response.body)

        # Extract job data
        jobs = data.get('jobs', [])

        job_item = JobsProjectItem()

        # Iterate over each job item
        for job in jobs:
            job_data = job.get('data', {})

            job_item['title'] = job_data.get('title')
            job_item['description'] = job_data.get('description')
            job_item['city'] = job_data.get('city')
            job_item['country'] = job_data.get('country')
            
            yield job_item