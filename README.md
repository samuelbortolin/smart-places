# Smart-Places

This repository contains the source code of the _Smart-Places_ platform.

This is web service for the management of places of interest (for example cities) and the association of sensors of various kinds.

## Setup and configuration

Please mark the `src` folder as source route.

The web service required Python version is `3.8` or higher.

### Required Python Packages

All required Python packages can be installed using the command:

```bash
pip install -r requirements.txt
```

### Environment variables

The Smart-Places web service allows to set the following environment variables:

- `WS_HOST`: the host where the web service is going to be available, can be set also using the argument `-wh` or `--host` (optional, the default value is `0.0.0.0`);
- `WS_PORT`: the port where the cloud webservice is going to be available, can be set also using the argument `-wp` or `--port` (optional, the default value is `12345`).

## Usage

### Web service

This service can be run with the command (from the `src` folder):

```bash
python smartplaces/ws/main.py
```
