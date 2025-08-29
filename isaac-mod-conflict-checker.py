import os
from collections import defaultdict

TARGET_FOLDERS = {"resources", "resources-dlc3"}
SKIP_SUBFOLDERS = {
    os.path.normpath("resources/gfx/ui/deadseascrolls"),
    os.path.normpath("resources/sfx/ui/deadseascrolls"),
    os.path.normpath("resources/sfx/deadseascrolls"),
}
MODS_ROOT = r"C:\Program Files (x86)\Steam\steamapps\common\The Binding of Isaac Rebirth\mods"
FILE_LIST = False
DENSITY = True
HIDE_DUPLICATES = True

def find_conflicts(mods_root):
    conflicts = defaultdict(list)

    for mod_name in os.listdir(mods_root):
        mod_path = os.path.join(mods_root, mod_name)
        if not os.path.isdir(mod_path):
            continue

        for folder in TARGET_FOLDERS:
            folder_path = os.path.join(mod_path, folder)
            if not os.path.exists(folder_path):
                continue

            for root, dirs, files in os.walk(folder_path):
                rel_root = os.path.relpath(root, mod_path)
                if any(rel_root.startswith(skip) for skip in SKIP_SUBFOLDERS):
                    continue
                for f in files:
                    if f.lower().endswith(".xml"):  # skip XML files
                        continue
                    rel_path = os.path.relpath(os.path.join(root, f), mod_path)
                    conflicts[rel_path].append(mod_name)

    return {path: mods for path, mods in conflicts.items() if len(mods) > 1}


def conflict_density(conflicts):
    """
    Build a dictionary of mod -> (conflict_file_count, partners_set)
    """
    conflict_files = defaultdict(int)
    conflict_partners = defaultdict(set)

    for path, mods in conflicts.items():
        for mod in mods:
            conflict_files[mod] += 1
            conflict_partners[mod].update(m for m in mods if m != mod)

    density = {}
    for mod in conflict_files:
        density[mod] = (conflict_files[mod], conflict_partners[mod])

    return density


if __name__ == "__main__":
    mods_root = MODS_ROOT
    print(f"Scanning mods in: {mods_root}\n")
    conflicts = find_conflicts(mods_root)

    if conflicts:
        if FILE_LIST:
            print("⚠ File Conflicts:")
            for path in sorted(conflicts):
                mods = sorted(conflicts[path])
                print(f"{path}: {', '.join(mods)}")
        if DENSITY:
            # Build density and pair conflict mapping
            density = conflict_density(conflicts)
            pair_conflicts = defaultdict(list)
            for path, mods in conflicts.items():
                for i in range(len(mods)):
                    for j in range(i + 1, len(mods)):
                        pair = tuple(sorted((mods[i], mods[j])))
                        pair_conflicts[pair].append(path)

            print("\n⚠ Conflict Density (detailed, sorted by partners):")
            covered = set()
            for mod, (file_count, partners) in sorted(
                density.items(),
                key=lambda x: (-len(x[1][1]), -x[1][0], x[0])
            ):
                # Skip mod if all its conflicts were already shown
                if HIDE_DUPLICATES and all((tuple(sorted((mod, p))) in covered) for p in partners):
                    continue

                print(f"{mod} ({file_count} files, {len(partners)} partners):")
                idx = 1
                for partner in sorted(partners):
                    pair = tuple(sorted((mod, partner)))
                    # only print if this pair wasn't printed yet
                    if not HIDE_DUPLICATES or pair not in covered:
                        files = pair_conflicts.get(pair, [])
                        print(f"  {idx}. {partner} ({len(files)} files)")
                        for f in sorted(files):
                            print(f"     - {f}")
                        covered.add(pair)
                        idx += 1

    else:
        print("✅ No conflicts found.")
