import glob
import os

files = [os.path.basename(f) for f in glob.glob("source/dragalia/*.rst")]

def convert_filename(name: str) -> str:
    # Strip extension
    name = name.replace(".rst", "")
    # Convert to camel case
    tokens = name.split("_")
    return "".join([t.title() for t in tokens])

documented_endpoints = [convert_filename(f) for f in files]


all_endpoints = []
with open("endpoints.txt") as f:
    all_endpoints = [l.strip() for l in f.readlines() if not l.startswith("Debug")]

undocumented_endpoints = [e for e in all_endpoints if not e in documented_endpoints]
print("\n".join(undocumented_endpoints))
print("="*50)
print(f"Documented {len(documented_endpoints)} out of {len(all_endpoints)} endpoints.")
print(f"Coverage: {len(documented_endpoints)/len(all_endpoints)*100:.2f}%.")
