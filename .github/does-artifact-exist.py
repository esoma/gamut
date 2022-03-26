
# python
import sys
# requests
import requests

artifact_name = sys.argv[1]
print(f'Looking for {artifact_name}...', file=sys.stderr)

response = requests.get(
    'https://api.github.com/repos/esoma/gamut/actions/artifacts'
)
for artifact in response.json()["artifacts"]:
    if artifact["name"] == artifact_name:
        print('Artifact already exists.', file=sys.stderr)
        print('1')
        sys.exit(0)

print('Artifact does not exist.', file=sys.stderr)
