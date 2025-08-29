# isaac-mod-conflict-checker
## Simple python script to check file conflicts between mods

You need python interpreter to run the script
[Python.org](https://www.python.org/)

I strongly advise using this script alongside
[isaac-mod-manager](https://github.com/Anahkiasen/isaac-mod-manager)

### Config:
- TARGET_FOLDERS - what folders inside mod folder should be scanned (default: "resources", "resources-dlc3")
- SKIP_SUBFOLDERS - what subfolders inside mod folder should be skipped (default: "resources/gfx/ui/deadseascrolls", "resources/sfx/ui/deadseascrolls", "resources/sfx/deadseascrolls")
- MODS_ROOT - location of the mods folder (default: "C:\Program Files (x86)\Steam\steamapps\common\The Binding of Isaac Rebirth\mods")
- FILE_LIST - boolean flag if raw file list should be printed (default: False)
- DENSITY - boolean flag if density report should be printed (default: True)
- HIDE_DUPLICATES - boolean flag if density raport should include duplicates (default: True)

### Density report structure
{mod folder name} ({total numer of conflicting files}, {total number of conflicting mods}):
  1. {conflicting mod folder name} ({total number of conflicting files with the partner mod})
    - {file path and name}

#### Warning
Mod folder name may not be the same as it's metadata.xml name (the one you see in mod list in the game).

### Example density report
uniquecoins_2565331478 (20 files, 6 partners):
  1. (rep) faster animations_2499964071 (8 files)
     - resources-dlc3\gfx\006.013_battery bum.anm2
     - resources-dlc3\gfx\006.015_hell game.anm2
     - resources-dlc3\gfx\006.018_rotten beggar.anm2
     - resources\gfx\006.004_beggar.anm2
     - resources\gfx\006.005_devil beggar.anm2
     - resources\gfx\006.006_shell game.anm2
     - resources\gfx\006.007_key master.anm2
     - resources\gfx\006.009_bomb bum.anm2
  2. better health_834199494 (1 files)
     - resources\gfx\items\slots\slot_005_devil_beggar.png
  3. fancy trinkets_2604587574 (8 files)
     - resources-dlc3\gfx\items\trinkets\trinket_131_blessedpenny.png
     - resources-dlc3\gfx\items\trinkets\trinket_147_chargedpenny.png
     - resources-dlc3\gfx\items\trinkets\trinket_172_cursedpenny.png
     - resources\gfx\items\trinkets\trinket_024_buttpenny.png
     - resources\gfx\items\trinkets\trinket_049_bloodypenny.png
     - resources\gfx\items\trinkets\trinket_050_burntpenny.png
     - resources\gfx\items\trinkets\trinket_051_flatpenny.png
     - resources\gfx\items\trinkets\trinket_052_counterfeitpenny.png
  4. keys resprites_2667333547 (2 files)
     - resources\gfx\items\slots\slot_006_shell_game.png
     - resources\gfx\items\slots\slot_007_key_master.png
  5. luckier pennies_2487805547 (1 files)
     - resources\gfx\items\pick ups\pickup_002_lucky_penny.png
  6. more shell game items_2923100205 (1 files)
     - resources\gfx\items\slots\slot_006_shell_game.png
