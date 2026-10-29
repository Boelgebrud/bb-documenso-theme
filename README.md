# Documenso with Bølgebrud's look

This is the source of our change to [Documenso](https://github.com/documenso/documenso), which Bølgebrud F.M.B.A runs for contract signing at sign.boelgebrud.dk. It is offered under the GNU Affero General Public License v3 (section 13), the licence of Documenso.

The change is small and touches no Documenso source: the `Dockerfile` takes the official image (the version is on its `FROM` line) and adds one stylesheet, two fonts and favicons.

| | |
|---|---|
| `Dockerfile` | the official image plus the files below |
| `theme/bolgebrud.template.css` | the theme (Documenso's colour variables and a few replaced classes) |
| `theme/bolgebrud.css` | the template with colours filled in from `theme/tokens.css` (`python3 theme/build-theme.py`) |
| `theme/fonts/` | Epilogue and DM Sans, SIL Open Font License (licence texts included) |
| `theme/icons/` | Bølgebrud's favicons |

Build: `docker build -t bolgebrud/documenso .`

Each tag is exactly what ran on our server at that time (for example `v2.20.0-bb1` is built on Documenso v2.20.0). The Bølgebrud name, logo and favicons are ours and are not licensed for reuse; the rest follows the AGPL-3.0 in `LICENSE`.

Questions: bestyrelsen@boelgebrud.dk
