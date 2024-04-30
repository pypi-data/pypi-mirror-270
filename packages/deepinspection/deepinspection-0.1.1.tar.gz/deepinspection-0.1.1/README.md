# deepinspection python

Python client library for deepinspection. Designed to simplify and exemplify interaction with the External API.

See the [Optram example](examples/optram) for a complete example including converting to a custom format for internal use.

## Install

Use your preferred package manager:

```bash
poetry add deepinspection
```

or

```bash
pip install deepinspection
```

## Usage

```python
import deepinspection


client = deepinspection.track.client(
    customer_id="customer-id",
    # subdomain="subdomain",  # optional, defaults to customer_id
    client_id="XYZ",
    client_secret="XYZ",
)

# list exports
exports = client.exports.fastenings.list()

# get export data
export = exports[0]

for fastening in client.exports.fastenings.get_data(export["id"]):
    pass
```

_The customer id should match with the website url `https://customer-id.track.deepinspection.io/`._

exports

```json
[
  {
    "updated": "2024-02-01T23:20:20.605136+00:00",
    "id": "461731a1-96c8-4ed6-99e4-9fe424eb9c40",
    "measurement_name": "20231001_124327_2011T",
    "measured": "2023-10-01T12:43:27.605136+00:00",
    "type": "fastenings",
    "downloaded": null,
    "created": "2024-02-01T23:20:20.605136+00:00",
    "user_id": "a338595f-6eba-481b-9f0f-112290a1078b"
  },
...
```

export_data

```json
{"id": "56fb582a-0280-43fa-81f3-2a444e7e4273", "position_geographical": {"track_section": "111",
...
```
