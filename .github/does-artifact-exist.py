
# python
import sys
# requests
import requests

artifact_name = sys.argv[1]
github_env = sys.argv[2]
print(f'Looking for {artifact_name}...', file=sys.stderr)

response = requests.get(
    'https://api.github.com/repos/esoma/gamut/actions/artifacts'
)
if response.status_code != 200:
    print(
        f'Unable to check if artifact exists: {response.status_code}',
        file=sys.stderr
    )
    sys.exit(1)
for artifact in response.json()["artifacts"]:
    if artifact["name"] == artifact_name:
        print('Artifact already exists.', file=sys.stderr)
        with open(github_env, 'a') as f:
            f.write(f'ARTIFACT_EXISTS=1\n')
        sys.exit(0)

print('Artifact does not exist.', file=sys.stderr)
with open(github_env, 'a') as f:
    f.write(f'ARTIFACT_EXISTS=0\n')
