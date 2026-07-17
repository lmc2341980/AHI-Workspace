import os
import json

ROOT = "."

IGNORE = {
    ".git",
    ".github",
    "__pycache__",
    "node_modules",
    ".idea",
    ".vscode",
    "AHI-INDEX"
}

folders = []
files = []

knowledge_map = {}

os.makedirs("90_SYSTEM/AHI-INDEX/knowledge", exist_ok=True)


def safe_name(path):

    if path == ".":
        return "ROOT"

    return (
        path
        .replace("./", "")
        .replace("/", "__")
        .replace("\\", "__")
        .replace(" ", "_")
    )


for path, dirs, fs in os.walk(ROOT):

    dirs[:] = [
        d for d in dirs
        if d not in IGNORE
    ]

    rel = os.path.relpath(path, ROOT)

    folders.append(rel)

    manifest = []

    folder_key = safe_name(rel)

    knowledge_map[folder_key] = []


    for d in dirs:

        manifest.append(
            f"- 📁 {d}"
        )


    for file in fs:

        if file == "MANIFEST.md":
            continue


        full_path = os.path.join(
            path,
            file
        )


        rel_path = os.path.join(
            rel,
            file
        )


        manifest.append(
            f"- 📄 {file}"
        )


        files.append(rel_path)


        if file.lower().endswith(".md"):

            try:

                with open(
                    full_path,
                    "r",
                    encoding="utf8"
                ) as md:

                    content = md.read()


                knowledge_map[folder_key].append(
                    {
                        "path": rel_path,
                        "content": content
                    }
                )


            except Exception:

                pass



    with open(
        os.path.join(
            path,
            "MANIFEST.md"
        ),
        "w",
        encoding="utf8"
    ) as out:


        out.write(
            "# MANIFEST\n\n"
        )

        out.write(
            f"Folder: `{rel}`\n\n"
        )

        out.write(
            "## Contents\n\n"
        )

        out.write(
            "\n".join(manifest)
        )



with open(
    "90_SYSTEM/AHI-INDEX/repository.json",
    "w",
    encoding="utf8"
) as f:


    json.dump(
        {
            "folders": len(folders),
            "files": len(files)
        },
        f,
        indent=2
    )



with open(
    "90_SYSTEM/AHI-INDEX/tree.txt",
    "w",
    encoding="utf8"
) as f:


    for folder in folders:

        f.write(
            folder + "\n"
        )


    for file in files:

        f.write(
            file + "\n"
        )



with open(
    "90_SYSTEM/AHI-INDEX/files.json",
    "w",
    encoding="utf8"
) as f:


    json.dump(
        files,
        f,
        indent=2
    )



knowledge_path = (
    "90_SYSTEM/AHI-INDEX/knowledge"
)


for name, items in knowledge_map.items():

    if len(items) == 0:
        continue


    filename = os.path.join(
        knowledge_path,
        name + ".jsonl"
    )


    with open(
        filename,
        "w",
        encoding="utf8"
    ) as f:


        for item in items:

            f.write(
                json.dumps(
                    item,
                    ensure_ascii=False
                )
            )

            f.write("\n")



print("Done")
