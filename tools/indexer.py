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
artifacts = []

INDEX_PATH = "90_SYSTEM/AHI-INDEX"

os.makedirs(
    INDEX_PATH,
    exist_ok=True
)

os.makedirs(
    INDEX_PATH + "/knowledge",
    exist_ok=True
)


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


def read_metadata(content):

    if not content.startswith("---"):
        return None

    try:

        end = content.find(
            "---",
            3
        )

        if end == -1:
            return None


        yaml_text = content[3:end]


        metadata = {}


        for line in yaml_text.splitlines():

            if ":" in line:

                key, value = line.split(
                    ":",
                    1
                )

                key = key.strip()
                value = value.strip()


                if value:

                    metadata[key] = value


        return metadata


    except Exception:

        return None



for path, dirs, fs in os.walk(ROOT):

    dirs[:] = [
        d for d in dirs
        if d not in IGNORE
    ]

    rel = os.path.relpath(
        path,
        ROOT
    )

    folders.append(rel)


    folder_key = safe_name(rel)

    knowledge_map[folder_key] = []


    manifest = []


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


        files.append(
            rel_path
        )


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


                metadata = read_metadata(
                    content
                )


                if metadata:

                    metadata["path"] = rel_path

                    artifacts.append(
                        metadata
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
    INDEX_PATH + "/repository.json",
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
    INDEX_PATH + "/files.json",
    "w",
    encoding="utf8"
) as f:

    json.dump(
        files,
        f,
        indent=2
    )



with open(
    INDEX_PATH + "/tree.txt",
    "w",
    encoding="utf8"
) as f:


    for item in folders:
        f.write(item + "\n")

    for item in files:
        f.write(item + "\n")



for name, items in knowledge_map.items():


    if not items:
        continue


    with open(
        INDEX_PATH + "/knowledge/" + name + ".jsonl",
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



with open(
    INDEX_PATH + "/artifact.json",
    "w",
    encoding="utf8"
) as f:


    json.dump(
        artifacts,
        f,
        indent=2,
        ensure_ascii=False
    )



with open(
    INDEX_PATH + "/metadata.json",
    "w",
    encoding="utf8"
) as f:


    json.dump(
        {
            "artifact_count": len(artifacts),
            "generated_by": "AHI Repository Indexer"
        },
        f,
        indent=2
    )



print("Done")
