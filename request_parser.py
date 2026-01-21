from dataclasses import dataclass
@dataclass(frozen=True)
class Request: text:str; path:str; dry_run:bool=True

def parse(argv_or_text, path)->Request:
    return Request(text=str(argv_or_text), path=str(path), dry_run=True)