# Herdr Sidebar Menu

Add the Herdr Sidebar toggle to pane and workspace menus.

Requires the separate `alexarthurs/herdr-sidebar/plugins/herdr-sidebar` plugin. This plugin only supplies menu entries.

## Install

[Herdr Setup](https://github.com/ariel-ps/herdr-setup) installs prerequisites and lets you select this plugin in `dependencies.json`.

With Herdr 0.9.3+ already installed:

```sh
herdr plugin install ariel-ps/herdr-sidebar-menu --ref main --yes
```

Use a commit or release tag instead of `main` to pin a version. Supports macOS and Ubuntu/Debian Linux.

## Development

This is a minimal, manifest-only plugin. Its `sidebar` action delegates to
`herdr-sidebar.open-sidebar`; it has no local runtime entrypoint.

Run the manifest contract test with:

```sh
python3 tests/test_manifest.py
```

## License

Original project code is licensed under the [MIT License](LICENSE). Third-party code and media retain their own terms; this license does not grant rights to game assets, downloaded themes, or other third-party content.
