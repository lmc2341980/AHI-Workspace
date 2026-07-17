import os
import json

ROOT = "."

IGNORE = {
    ".git",
    ".github",
    "__pycache__",
    "node_modules",
    ".idea",
    ".vscode"
}

folders=[]
files=[]

for path,dirs,fs in os.walk(ROOT):

    dirs[:] = [d for d in dirs if d not in IGNORE]

    rel=os.path.relpath(path,ROOT)

    folders.append(rel)

    manifest=[]

    for d in dirs:
        manifest.append(f"- 📁 {d}")

    for f in fs:

        if f=="MANIFEST.md":
            continue

        manifest.append(f"- 📄 {f}")

        files.append(os.path.join(rel,f))

    with open(os.path.join(path,"MANIFEST.md"),"w",encoding="utf8") as out:

        out.write("# MANIFEST\n\n")

        out.write(f"Folder: `{rel}`\n\n")

        out.write("## Contents\n\n")

        out.write("\n".join(manifest))

os.makedirs("90_SYSTEM/AHI-INDEX",exist_ok=True)

with open("90_SYSTEM/AHI-INDEX/repository.json","w",encoding="utf8") as f:

    json.dump({

        "folders":len(folders),

        "files":len(files),

        "folder_list":folders,

        "file_list":files

    },f,indent=2)

print("Done")
with open("90_SYSTEM/AHI-INDEX/tree.txt","w",encoding="utf8") as f:

    for folder in folders:
        f.write(folder+"\n")

    for file in files:
        f.write(file+"\n")
        with open("90_SYSTEM/AHI-INDEX/files.json","w",encoding="utf8") as f:

    json.dump(files,f,indent=2)
