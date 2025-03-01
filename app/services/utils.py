from slugify import slugify


def generate_slug(data: str,seperator: str='-',max_length:int =0, lowercase: bool = True) -> str:
    return slugify(data, separator=seperator, max_length=max_length, lowercase=lowercase)