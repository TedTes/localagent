def summarize(results):
    lines=[f"{i+1}. {type(r).__name__}: {str(r)[:160]}" for i,r in enumerate(results)]
    return "\n".join(lines) if lines else "No actions taken."
