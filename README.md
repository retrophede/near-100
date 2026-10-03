# NEAR / 100

Interactive 3D atlas of the solar neighbourhood. The Sun and the 99 nearest stellar components in the archived 2023 CDS 10 pc sample, with a true-black scene, ecliptic grid, searchable catalogue and animated glass information cards.

**Website:** https://retrophede.github.io/

## Development

No package installation or build step is required. Dependencies are pinned and vendored locally: Three.js 0.180.0 and IBM Plex Mono.

```sh
python3 -m http.server 4173
```

Open http://localhost:4173. A WebGL-capable browser is required. Direct `file://` opening is not supported by this modular version.

## Publishing and versions

GitHub Actions validates the catalogue and JavaScript and publishes only the web assets on each push to `main`. Pull requests run the same checks without deployment. The workflow can also be run manually from Actions.

Each commit is a recoverable version. To undo a published change, revert its commit and let the workflow deploy the result. No external deployment credentials are stored in the repository.

## Validation

```sh
python3 verify.py
node --check app.js
```

`verify.py` checks all 100 identities, exact selection from the source table, distance ordering, selection boundary, parallax conversion and the inverse ecliptic-coordinate transform. Browser QA should additionally cover orbit/zoom, point click and repeat click, search, components of binary stars, modal keyboard interaction and mobile layout.

## Data and reproducibility

Reylé et al., *The 10 parsec sample in the Gaia era*, A&A 650, A201 (2021), with 2023 update.

- Article: https://doi.org/10.1051/0004-6361/202140985
- Update: https://arxiv.org/abs/2302.02810
- Archive: https://cdsarc.cds.unistra.fr/ftp/J/A+A/650/A201/
- Snapshot: `tablea1.dat.gz`, CDS version 25 August 2023; retrieved 3 October 2026.
- Schema: `CDS-ReadMe.txt`.

Rebuild the selected dataset with `python3 build_catalog.py`.

The selection contains the 99 closest objects of types `*`, `LM`, `LM?`, `WD`, `WD?`, sorted by `1000/parallax_mas`, plus the Sun. Component stars count individually; brown dwarfs and planets are excluded. Uncertain classifications are retained and marked. The boundary is 36 Oph B at approximately 19.414 light-years; 36 Oph C is the next excluded entry. This is a versioned catalogue selection, not a live 2026 census. Individual catalogue parallaxes are preserved, including small differences between members of the same system.

ICRS coordinates at their source epochs are rotated to mean J2000 ecliptic axes, using obliquity 23.439291111 degrees. Renderer axes are `(ecliptic X, ecliptic Z, -ecliptic Y)` in light-years. There is no epoch propagation or orbital simulation. Positions and distances are to scale; star sizes, halos and approximate spectral-class colours are symbolic. Missing measurements remain null. Estimated G magnitudes are distinguished from measured G.

## Repository layout

- `index.html`, `style.css`, `app.js`: original interface and rendering code.
- `stars.json`: selected catalogue and provenance metadata.
- `build_catalog.py`, `verify.py`: reproducible extraction and data checks.
- `tablea1.dat.gz`, `CDS-ReadMe.txt`: archived source data and schema.
- `three.module.js`, `three.core.js`, `OrbitControls.js`: pinned Three.js dependency.
- `ibm-plex-mono.woff2`: self-hosted font.
- `.github/workflows/pages.yml`: validation and deployment pipeline.

## Third-party notices

Three.js is distributed under MIT (`THREE-LICENSE.txt`); IBM Plex Mono under OFL (`FONT-LICENSE.txt`). Scientific data retain their original attribution. Solar spectral type reference: https://science.nasa.gov/sun/facts/.

Original design inspired by the typographic language of Gaia Mary / Project Hail Mary. No proprietary imagery, fonts or other assets from the reference site are reused.
