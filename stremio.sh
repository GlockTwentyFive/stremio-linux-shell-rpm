#!/bin/sh

# Work around GTK/libmpv locale issues.
export LC_NUMERIC=C

# Tell the Rust frontend where the Node.js backend is located.
export SERVER_PATH=/usr/libexec/stremio/server.js

# NVIDIA systems render more reliably with the OpenGL renderer.
if [ -e /dev/nvidia0 ]; then
    export GSK_RENDERER=opengl
fi

exec /usr/libexec/stremio/stremio "$@"
