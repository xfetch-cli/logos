<h1 align="center">Logo Catalog for xfetch</h1>

<div align="center">

[![License](https://img.shields.io/badge/license-MIT-blue?style=flat-square)](https://github.com/xfetch-cli/logos/blob/main/LICENSE)
[![Platform](https://img.shields.io/badge/platform-linux%20%7C%20macOS%20%7C%20windows-lightgrey?style=flat-square)](https://github.com/xfetch-cli/xfetch)

<p>ASCII logos of Linux distributions, macOS and Windows, consumed by <strong>xfetch</strong>.</p>

</div>

<!--Menu-->
<div align="left">
  <h2>Menu</h2>
  <ul>
    <li><a href="#features">Features</a></li>
    <li><a href="#structure">Structure</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#related-repos">Related Repos</a></li>
  </ul>
</div>

<h2 id="features" align="center"> Features</h2>

- **127+ logos**: Linux distributions (Arch, Debian/Ubuntu, Fedora/RHEL, openSUSE, Void, Gentoo, ...), macOS (version-specific from Cheetah to Sequoia) and Windows (3.x to 11).
- **Standard sizing**: each logo is a rectangular block of ~12 rows, world-readable UTF-8 text.
- **Machine-readable index**: `logos.json` maps every distro id, aliases, family, colors and ANSI codes to its file.
- **Resolution chain**: exact `ID` → `ID_LIKE` → generic logo (used by `xfetch --gen-config`).

<h2 id="structure" align="center"> Structure</h2>

```
logos/
├── defaults/          # canonical logo per OS/distro
│   ├── linux/         # one file per distribution
│   ├── macos/         # version-specific macOS logos
│   └── windows/       # version-specific Windows logos
└── logos.json         # the index (contract between catalog and xfetch)
```

<h2 id="usage" align="center"> Usage</h2>

xfetch fetches the index and the raw art over HTTPS:

```bash
xfetch --gen-config                    # embed the detected distro's logo
xfetch --gen-config --logo arch        # force a specific logo
xfetch --gen-config --logo windows-11  # any catalog id works
```

The catalog base URL can be overridden for testing forks:

```bash
XFETCH_LOGOS_URL=https://raw.githubusercontent.com/<user>/logos/main xfetch --gen-config
```

<h2 align="center" id="related-repos">Related Repos</h2>

<ul>
  <li><a href="https://github.com/xfetch-cli/xfetch">XFetch</a> — the system info tool that consumes this catalog</li>
  <li><a href="https://github.com/xfetch-cli/api">XFetch API</a> — shared crates for the ecosystem</li>
  <li><a href="https://github.com/xfetch-cli/configs">XFetch Configs</a> — curated presets and examples</li>
  <li><a href="https://github.com/xfetch-cli/plugins">XFetch Plugins</a> — official plugins</li>
</ul>

<div id="about-the-developer" align="center">
<h2>X</h2>

<a href="https://dev.xscriptor.com">
  <img src="https://xscriptor.github.io/icons/icons/code/product-design/xsvg/verified-filled.svg" width="24" alt="X Web" />
</a>
 & 
<a href="https://github.com/xscriptor">
  <img src="https://xscriptor.github.io/icons/icons/code/product-design/xsvg/github.svg" width="24" alt="X Github Profile" />
</a>
 & 
<a href="https://www.xscriptor.com">
  <img src="https://xscriptor.github.io/icons/icons/code/product-design/xsvg/quotes.svg" width="24" alt="Xscriptor web" />
</a>

</div>
