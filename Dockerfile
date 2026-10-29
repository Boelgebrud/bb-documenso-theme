# Documenso in Bølgebrud's look. The official image plus colours, fonts and favicons; no source is changed.
# Build (after `python3 theme/build-theme.py`):  docker build -t bolgebrud/documenso:v2.20.0 apps/documenso
# When the Documenso version changes, change the tag here AND in compose.yml, rebuild, and look at the pages.
FROM documenso/documenso:v2.20.0
USER root
# Documenso serves build/client (a copy of its public folder made at build time), so the files go there.
COPY theme/fonts/ /app/apps/remix/build/client/fonts/bolgebrud/
COPY theme/icons/ /app/apps/remix/build/client/
COPY theme/bolgebrud.css /tmp/bolgebrud.css
# The built stylesheet has a hashed name, so the theme goes at the end of it (later rules win).
# The build fails if there is not exactly one such file, so an upgrade that moves it cannot go unnoticed.
RUN set -eu; \
    set -- /app/apps/remix/build/client/assets/app-*.css; \
    [ "$#" = 1 ] && [ -f "$1" ] || { echo "expected one app-*.css, found $#" >&2; exit 1; }; \
    cat /tmp/bolgebrud.css >> "$1"; \
    rm /tmp/bolgebrud.css
USER 1001
