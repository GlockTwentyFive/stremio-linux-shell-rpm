#!/bin/sh

# Use OpenGL renderer on NVIDIA systems
if [ -e /dev/nvidia0 ]; then
    export GSK_RENDERER=opengl
fi

export SERVER_PATH=/usr/libexec/stremio/server.js

exec /usr/libexec/stremio/stremio-linux-shell "$@"
