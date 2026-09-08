from urllib.parse import parse_qs, urlparse

from django import template

register = template.Library()


@register.filter
def drive_image_url(value):
    """Convert common Google Drive share URLs to an image thumbnail URL."""
    if not value:
        return value

    parsed_url = urlparse(str(value))
    file_id = parse_qs(parsed_url.query).get("id", [None])[0]

    if not file_id and parsed_url.netloc in {
        "drive.google.com",
        "www.drive.google.com",
    }:
        path_parts = parsed_url.path.strip("/").split("/")
        if len(path_parts) >= 3 and path_parts[0] == "file" and path_parts[1] == "d":
            file_id = path_parts[2]

    if file_id and parsed_url.netloc.endswith("google.com"):
        return f"https://drive.google.com/thumbnail?id={file_id}&sz=w1000"

    return value
