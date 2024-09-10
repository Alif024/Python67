def analyze_log_file(log_file_path: str) -> dict:
    result = {
        'requests_by_ip': {},
        'most_requested_resource': None,
        'total_bytes': 0,
        'total_404_errors': 0,
    }
    with open(log_file_path, 'r') as log_file:
        lines = [line.strip().split() for line in log_file.readlines()]
    if len(lines) != 0:
        list_of_requests = []
        for line in lines:
            if len(line) != 5:
                continue
            if line[0] not in result['requests_by_ip']:
                result['requests_by_ip'][line[0]] = 1
            else:
                result['requests_by_ip'][line[0]] += 1
            list_of_requests.append(line[2])
            if line[3] == '404':
                result['total_404_errors'] += 1
            result['total_bytes'] += int(line[4])
        for resource in list_of_requests:
            try:
                if list_of_requests.count(result["most_requested_resource"]) < list_of_requests.count(resource):
                    result["most_requested_resource"] = resource
            except KeyError:
                result["most_requested_resource"] = resource
        return result
    else:
        return result


log_file_path = 'server_log.txt'  # Replace with the path to your log file
result = analyze_log_file(log_file_path)

# Print the analysis result
print("Log File Analysis Result:")
print(f"Requests by IP: {result['requests_by_ip']}")
print(f"Most Requested Resource: {result['most_requested_resource']}")
print(f"Total 404 Errors: {result['total_404_errors']}")
print(f"Total Bytes Transferred: {result['total_bytes']}")
