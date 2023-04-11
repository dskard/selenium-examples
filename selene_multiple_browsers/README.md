# Multiple Browsers with selene, selenium, pytest, and pytest-selenium

Example of running multiple web browsers at once. The web browsers are managed by the pytest-selenium plugin. The web browsers are shared with selene. Selene does not manage the web browsers, but is used to sends automation commands to the browsers.

Prereqs:
1. [pyenv](https://github.com/pyenv/pyenv#installation)
2. [docker compose](https://docs.docker.com/compose/install/linux/)
3. [direnv](https://direnv.net/docs/installation.html)
4. a VNC client, like [tigervnc-viewer](https://tigervnc.org/), or the `open` command if on macOS

Install:
```bash
make pyenv
make install
```

Running the example:
```bash
make test-env-up
shownode &
make test
make test-env-down
```

What you should see:
1. Two web browsers will launch.
2. The first web browser will navigate to a http://github.com.
3. The second web browser will navigate to a http://github.com.
4. The first web browser will navigate to a http://ddg.gg.
5. The second web browser will navigate to a http://ddg.gg.
6. Both web browsers will close.
