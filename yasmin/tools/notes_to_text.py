"""COPY-NOTES-FOR-CLIENT.md -> COPY-NOTES-FOR-CLIENT.txt (plain text for an Upwork message).
Run from yasmin/. Regenerate whenever the .md changes."""
import re

md = open("COPY-NOTES-FOR-CLIENT.md").read().splitlines()


def plain(t):
    t = t.replace("\\|", "|")
    t = re.sub(r"\*\*(.+?)\*\*", r"\1", t)
    t = re.sub(r"`([^`]+)`", r"\1", t)
    t = re.sub(r"(?<!\w)\*(.+?)\*(?!\w)", r"\1", t)
    return t.strip()


out, head = [], None
for line in md:
    if line.startswith("# "):
        out += [plain(line[2:]).upper(), "=" * len(line[2:]), ""]
    elif line.startswith("## "):
        out += ["", plain(line[3:]).upper(), "-" * len(line[3:]), ""]
    elif line.startswith("### "):
        out += ["", plain(line[4:]), ""]
    elif line.startswith("|"):
        cells = [c.strip() for c in re.split(r"(?<!\\)\|", line.strip())[1:-1]]
        if set("".join(cells)) <= set("-: "):
            continue
        if head is None:
            head = cells
            continue
        if cells[0].isdigit():                     # numbered correction row
            n, where, was, sug, note = cells
            out += [f"{n}. {plain(where)}",
                    f"   Now:        {plain(was)}",
                    f"   Suggested:  {plain(sug)}",
                    f"   Why:        {plain(note)}", ""]
        else:                                      # the "change already made" row
            out += [f"- {plain(cells[0])}", f"  {plain(cells[1])}", f"  Why: {plain(cells[2])}", ""]
    else:
        if not line.strip():
            head = None
            if out and out[-1] == "":
                continue
        out.append(plain(line) if not line.startswith("- ") else "- " + plain(line[2:]))

text = "\n".join(out).strip() + "\n"
text = text.replace("Location key: the ID (e.g. J-023) matches our copy inventory; \"p\" is the page of your case-study PDF.",
                    "Each note says where it is (project, section, page of your case-study PDF). The code, e.g. J-023, is just our reference number.")
open("COPY-NOTES-FOR-CLIENT.txt", "w").write(text)
print(len(text), "chars,", text.count("Suggested:"), "suggestions")
