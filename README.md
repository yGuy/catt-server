# Docker Image to Connect Node-Red with ChromeCast devices

This image uses CATT to provide a simple HTTP API that Node-Red can connect to in order to control ChromeCast devices.

```bash
docker run -d --restart unless-stopped \
  -e CHROME_CAST_SERVER=192.168.0.42 \
  --name catt-server \
  ghcr.io/yguy/catt-server:latest
```

This is under MIT license Copyright (c) 2023 Sebastian Mueller (yWorks)
