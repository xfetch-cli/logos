<div align="center">
  <h1> Contributing to the Logo Catalog</h1>
  <p>Thank you for your interest in contributing logos!</p>
</div>

<br>

<h2>Code of Conduct</h2>

<p>
  This project is open and welcoming. Be respectful, constructive, and collaborative.
  Harassment, trolling, and personal attacks are not tolerated.
</p>

<h2>How to Contribute</h2>

<ol>
  <li><strong>Fork</strong> the repository on GitHub.</li>
  <li><strong>Clone</strong> your fork locally.</li>
  <li>Create a <strong>feature branch</strong> (<code>git checkout -b feature/my-logo</code>).</li>
  <li>Add your logo and index entry following the rules below.</li>
  <li>Verify with <code>xfetch --gen-config --logo &lt;your-distro&gt;</code>.</li>
  <li><strong>Commit</strong> your changes with a clear message.</li>
  <li><strong>Push</strong> to your fork.</li>
  <li>Open a <strong>Pull Request</strong> from your branch to the main repository.</li>
</ol>

<h2>Adding a New Logo</h2>

<h3>1. The art file (<code>defaults/&lt;category&gt;/&lt;id&gt;.txt</code>)</h3>

<ul>
  <li>Plain UTF-8 text, <strong>LF</strong> line endings, <strong>no control characters</strong> (no tabs, no NUL).</li>
  <li>Rectangular block of ~<strong>12 rows</strong>; pad shorter rows with spaces so every line has the same width.</li>
  <li>Width may vary up to ~60 columns; keep it consistent with the distro's existing art.</li>
  <li>Optional ANSI escape codes are allowed for colored logos.</li>
</ul>

<h3>2. The index entry (<code>logos.json</code>)</h3>

<pre><code class="language-jsonc">{
    "id": "my-distro",                 // os-release ID (lowercase, dashes)
    "name": "My Distro",
    "category": "linux",               // linux | macos | windows
    "family": "debian",                // debian | arch | fedora | opensuse | independent | macos | windows
    "aliases": ["my distro", "mydistro"],   // include the os-release ID and ID_LIKE tokens
    "file": "defaults/linux/my-distro.txt",
    "colors": { "primary": "#A81D33", "secondary": "#D70A53" },
    "url": "https://example.org",
    "ansi": { "primary": 125, "secondary": 161 }
}
</code></pre>

<p>
  The <code>aliases</code> array is what makes detection work: it must include the real
  <code>ID</code> of the distro in <code>/etc/os-release</code> (e.g. <code>linuxmint</code> for
  Linux Mint, whose file is <code>linux-mint.txt</code>).
</p>

<h2>Verify</h2>

<p>
  Once the catalog is pushed, test the entry end-to-end:
</p>

<pre><code>xfetch --gen-config --logo my-distro</code></pre>
