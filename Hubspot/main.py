import requests
from datetime import datetime, timedelta, timezone
from collections import defaultdict

# DATASET
GET_URL = "https://candidate.hubteam.com/candidateTest/v3/problem/dataset?userKey=9113aecf15389a76f09495136ba8"
POST_URL = "https://candidate.hubteam.com/candidateTest/v3/problem/result?userKey=9113aecf15389a76f09495136ba8"

# TEST DATASET
# GET_URL = "https://candidate.hubteam.com/candidateTest/v3/problem/test-dataset?userKey=9113aecf15389a76f09495136ba8"
# POST_URL = "https://candidate.hubteam.com/candidateTest/v3/problem/test-dataset-answer?userKey=9113aecf15389a76f09495136ba8"


def fetch_data():
    """Fetch call data from the specified URL."""
    response = requests.get(GET_URL)
    response.raise_for_status()
    return response.json()["callRecords"]


def get_customer_calls_per_date(calls):
    """
    Organize calls by customer and date.
    Handle calls that span multiple days and midnight edge cases.
    """
    customer_calls_per_date = defaultdict(lambda: defaultdict(list))
    for call in calls:
        customer_id = call["customerId"]
        start = datetime.fromtimestamp(call["startTimestamp"] / 1000, tz=timezone.utc)
        end = datetime.fromtimestamp(call["endTimestamp"] / 1000, tz=timezone.utc)

        # Determine which days this call spans
        current_date = start.date()
        end_date = end.date()

        # If the call ends exactly at midnight, we don't include the next day
        if end.time() == datetime.min.time():
            end_date -= timedelta(days=1)

        # Add the call to each day it spans
        while current_date <= end_date:
            customer_calls_per_date[customer_id][current_date.isoformat()].append(call)
            current_date += timedelta(days=1)

    return customer_calls_per_date


def calculate_max_concurrent(date, calls):
    """
    Calculate the maximum number of concurrent calls for a given date
    with prefix sum and adjacent diff algorithm.
    """
    events = []
    date_start = int(
        datetime.combine(date, datetime.min.time(), tzinfo=timezone.utc).timestamp()
        * 1000
    )
    date_end = int(
        (
            datetime.combine(date, datetime.min.time(), tzinfo=timezone.utc)
            + timedelta(days=1)
        ).timestamp()
        * 1000
    )

    for call in calls:
        start = max(call["startTimestamp"], date_start)
        end = min(call["endTimestamp"], date_end)
        events.append((start, 1, call["callId"]))
        events.append((end, -1, call["callId"]))

    events.sort()

    max_concurrent, curr_concurrent = 0, 0
    active_calls, max_active_calls = set(), set()
    max_timestamp = 0

    # Process events to find max concurrent calls
    for timestamp, event_type, call_id in events:
        if event_type == 1:  # Call start
            curr_concurrent += 1
            active_calls.add(call_id)
        else:  # Call end
            curr_concurrent -= 1
            active_calls.remove(call_id)

        if curr_concurrent > max_concurrent:
            max_concurrent = curr_concurrent
            max_timestamp = timestamp
            max_active_calls = set(active_calls)

    return max_concurrent, max_timestamp, list(max_active_calls)


def format_results(customer_dates):
    """Format the results as required by the API."""
    results = []
    for customer_id, dates in customer_dates.items():
        for date_str, calls in dates.items():
            date = datetime.fromisoformat(date_str).date()
            max_concurrent, timestamp, call_ids = calculate_max_concurrent(date, calls)
            results.append(
                {
                    "customerId": customer_id,
                    "date": date_str,
                    "maxConcurrentCalls": max_concurrent,
                    "timestamp": timestamp,
                    "callIds": call_ids,
                }
            )
    return {"results": sorted(results, key=lambda x: (x["customerId"], x["date"]))}


def post_results(results):
    response = requests.post(POST_URL, json=results)
    response.raise_for_status()
    print(f"Results posted successfully. Status code: {response.status_code}")


def main():
    try:
        calls = fetch_data()
        customer_dates = get_customer_calls_per_date(calls)
        results = format_results(customer_dates)
        post_results(results)
    except requests.RequestException as e:
        print(f"An error occurred while making a request: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        raise


if __name__ == "__main__":
    main()