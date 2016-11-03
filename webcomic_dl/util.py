import json
def prettyprint(data, indent='\t'):
    return json.dumps(data, sort_keys=True, indent=indent, separators=(",", ": "))
