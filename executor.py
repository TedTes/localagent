from pathlib import Path
from datetime import datetime



def run(plan, tools,undo_path=Path("undo.log")):
    out = []
    log=Path(undo_path).open("a",encoding="utf-8")
    log.write(f"# RUN {datetime.utcnow().isoformat()}\n")
    for step in plan.get("steps", []):
        r=tools[step["tool"]].fn(**s["args"]);
        out.append(r); 
        [log.write(f"{a}\t{b}\n") for a,b in (r or [])]
    log.close();
    return out