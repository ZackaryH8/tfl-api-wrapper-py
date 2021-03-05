<p align="center">
    <img width="200" src="https://blog.tfl.gov.uk/wp-content/uploads/2018/05/cropped-logo_roundel-2.png" alt="TfL Logo">
    <h1 align="center">TfL API Wrapper</h1>
    <p align="center">An API wrapper for the TfL Unified API, made with Python.</p>
</p>

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![](https://img.shields.io/github/issues/ZackaryH8/tfl-api-wrapper-py)](https://github.com/ZackaryH8/tfl-api-wrapper-py/issues)


## Installation
```
pip install tflwrapper
```

## Contribute

There are many ways to contribute to this repo.
* [Submit bugs](https://github.com/ZackaryH8/tfl-api-wrapper-py/issues) and help us verify fixes as they are checked in.
* Review the [source code changes](https://github.com/ZackaryH8/tfl-api-wrapper-py/pulls).

## Example Usage

### StopPoint

```py
from tflwrapper import stopPoint

app_key = "YOUR_API_KEY_HERE"

stoppoint = stopPoint(app_key)
arrivals = stoppoint.getStationArrivals('940GZZLUAS')

print(arrivals)
```

## Disclaimer
This repository is not affiliated, associated, authorized, endorsed by, or in any way officially connected with Transport for London (TfL) or it's parent organisation Greater London Authority (GLA)
