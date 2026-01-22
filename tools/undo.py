from pathlib import Path

lines=Path("undo.log").read_text().splitlines()
i=max(i for i,l in enumerate(lines) if l.startswith("# RUN"))
for l in reversed(lines[i+1:]):
    a,b=l.split("\t");
    Path(b).rename(a)
print("Last run undone.")