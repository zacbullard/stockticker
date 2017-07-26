# Stockticker Website

This project demonstrates the usage of Python to manipulate and present dynamically aquired data via an HTML interface. After inputting a stock symbol, the end-of-day stock price history for the previous month will be plotted. The finished website can be viewed at [http://zstockticker.herokuapp.com/](http://zstockticker.herokuapp.com/).

Major tools used include:
- Flask, a web framework for Python
- Pandas, a Python data structure library
- Bokeh, a Python plotting library with a focus web implementation
- Quandl, a source for API-culled market data
- Heroku, a cloud-based service for deploying web applications

For the Heroku deployment, a [conda buildpack](https://github.com/kennethreitz/conda-buildpack) was used, however all requirements can be manually placed into `requirements.txt` if you do not wish to use a buildpack.
