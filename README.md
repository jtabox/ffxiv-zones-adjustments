# ffxiv-zones-adjustments
Just a simple Blender addon that performs some fixes and adjustments in batch, after importing a FFXIV zone as fbx-file created with ZoneFBX.
Wrote it for me, so I don't have to manually select each material one by one and change the settings myself. But if someone else also finds it useful it's even better :)

The available fixes/adjustments are the following:
- Changes the viewport's Blend Mode in Material Preview to Alpha Hashed.
- Changes the materials' metallic property to 0 (they're exported with 1 by default).
- Changes Normal Maps' Shaders to World Space.
- Sets Normal Map Shader Strength to 50%.

For details see the posts (here)[https://forums.nexusmods.com/index.php?showtopic=12190758/#entry117011953].

**If you have an idea for more fixes/adjustments that could be added feel free to open an issue and I'll add them.**

### To install and use:
- Just download the zip file from [Releases](https://github.com/jtabox/ffxiv-zones-adjustments/releases/tag/v0.2.0) and install it as an addon in Blender [normally](https://docs.blender.org/manual/en/latest/editors/preferences/addons.html).
- When you activate it there should be a tab named `XIVZones` in the right side panel, with 4 buttons for each of the functions above.


### Credits:
- lmcintyre for ZoneFbx (https://github.com/lmcintyre/ZoneFbx).
- zwansanwan for manually extracting, organizing and uploading all available zones (https://www.nexusmods.com/finalfantasy14/mods/1709).
