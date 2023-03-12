import json


def json_encoder(obj):
    try:
        json.dumps(obj)
        return obj
    except Exception as e:
        return None

def human_readable_size(size, decimal_place=1):
    for unit in ['B', 'KiB', 'MiB', 'GiB', 'TiB']:
        if size < 1024.0:
            break
        size /= 1024.0
    
    return f"{size:.{decimal_place}f} {unit}"