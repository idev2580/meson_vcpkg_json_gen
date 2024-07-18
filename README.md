# meson_vcpkg_json_gen

An automatic `vcpkg.json` generator based on `meson.build`.

## How to use

Paste this code into your meson project's directory and run.

After running this script, `vcpkg.json` will be generated.

## Limitations
- Version is always `1`
- Description is always `Auto-generated vcpkg.json`
- Conditional dependency not work. All `dependency()` code must be assignment expression outside any loop or conditional code block.
