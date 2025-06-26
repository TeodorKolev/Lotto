from environments import ENVIRONMENTS

# Set your environment here
ENV = "fdj"  # or "test", etc.

config = ENVIRONMENTS[ENV]
url_to_zip = config["url_to_zip"]
file_name = config["file_name"]
row_range = config["row_range"]
