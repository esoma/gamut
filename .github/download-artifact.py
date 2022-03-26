
# python
import os
import sys
from zipfile import ZipFile
# requests
import requests

artifact_name = sys.argv[1]
extract_path = sys.argv[2]
print(f'Finding {artifact_name}...', file=sys.stderr)

response = requests.get(
    'https://api.github.com/repos/esoma/gamut/actions/artifacts'
)
for artifact in response.json()["artifacts"]:
    if artifact["name"] == artifact_name:
        artifact_id = artifact["id"]
        break
else:
    print('Artifact does not exist.', file=sys.stderr)
    sys.exit(1)

print(f'Downloading artifact {artifact_id}...', file=sys.stderr)
response = requests.get(
    f'https://api.github.com/repos/esoma/gamut/actions/artifacts/'
    f'{artifact_id}/zip',
    headers={
        "Authorization": f'token {os.environ["GITHUB_TOKEN"]}',
    }
)
if response.status != 200:
    print(f'Failed to download: {response.status}.', file=sys.stderr)
    sys.exit(1)

print(f'Unzipping artifact...', file=sys.stderr)
os.makedirs(extract_path, exist_ok=True)
zipped_file = ZipFile(response.raw)
zipped_file.extractall(path=extract_path)
