## RPM packaging for Stremio Linux Shell.

Source:
https://github.com/Stremio/stremio-linux-shell

This repository contains only the packaging files used to build RPMs via Fedora COPR.

### Instructions to enable and download rpm package of stremio-linux-shell
- Enable the copr repo - `sudo dnf enable chronosxbt/stremio-linux-shell`
- Download the app - `sudo dnf install stremio-linux-shell`

### Troubleshooting
The app has been tested on Fedora 44 and it works without any issues, if the app fails to start for any reason then try opening it from the terminal by executing the command `stremio` and copy the logs and open an issue here if it fails.
