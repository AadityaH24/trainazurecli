import json
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google.oauth2.service_account import Credentials as ServiceAccountCredentials
from google.analytics.data_v1beta import BetaAnalyticsDataClient
from google.analytics.data_v1beta.types import (
    DateRange,
    Dimension,
    Metric,
    MetricType,
    RunRealtimeReportRequest
)
import time

def main():
    print("we are running")

# def run_realtime_report(property_id="YOUR-GA4-PROPERTY-ID"):
#     # Load service account credentials
#     with open('GA4Project-bbef1eaef1b5.json', 'r') as f:
#         key_data = json.load(f)

#     credentials = ServiceAccountCredentials.from_service_account_info(key_data, scopes=["https://www.googleapis.com/auth/analytics.readonly"])

#     """Runs a simple report on a Google Analytics 4 property."""
#     # Using a default constructor instructs the client to use the credentials
#     # specified in GOOGLE_APPLICATION_CREDENTIALS environment variable.
#     client = BetaAnalyticsDataClient(credentials=credentials)

#     request = RunRealtimeReportRequest(
#         property=f"properties/{property_id}",
#         dimensions=[Dimension(name="country")],
#         metrics=[Metric(name="activeUsers")],
#     )

#     try:
#         while True:
#             response = client.run_realtime_report(request)
#             print_run_report_response(response)
#             time.sleep(5)
#     except Exception as e:
#         print(f"Error while running the report: {str(e)}")
#         return

# def print_run_report_response(response):
#     # Instead of Printing the response, you can also save it to a file
#     # OR, process it using libraries like Pandas and push the output to a database
#     """Prints results of a runReport call."""
#     print(f"{response.row_count} rows received")
#     for dimensionHeader in response.dimension_headers:
#         print(f"Dimension header name: {dimensionHeader.name}")
#     for metricHeader in response.metric_headers:
#         metric_type = MetricType(metricHeader.type_).name
#         print(f"Metric header name: {metricHeader.name} ({metric_type})")

#     print("Report result:")
#     for rowIdx, row in enumerate(response.rows):
#         print(f"\nRow {rowIdx}")
#         for i, dimension_value in enumerate(row.dimension_values):
#             dimension_name = response.dimension_headers[i].name
#             print(f"{dimension_name}: {dimension_value.value}")

#         for i, metric_value in enumerate(row.metric_values):
#             metric_name = response.metric_headers[i].name
#             print(f"{metric_name}: {metric_value.value}")


if __name__ == "__main__":
    main()
    
    
    # https://cuteprogramming.blog/2023/05/21/using-docker-and-kubernetes-without-docker-desktop-on-windows-11/