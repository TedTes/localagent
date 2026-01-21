from dataclasses import dataclass
from pathlib import Path

@dataclass(frozen=True)
class Policy: base:Path; require_confirm_delete:bool=True

def enforce_scope(policy:Policy, path:str)->Path:
    base = Path(policy.base).expanduser().resolve()
    p = Path(path.strip()).expanduser()
    p = (base / p).resolve() if not p.is_absolute() else p.resolve()
    p.relative_to(base)
    return p
