# Currency Converter CLI

A simple command-line tool to convert currency amounts using real-time exchange rates from the [Frankfurter API](https://www.frankfurter.app/).

## Features

- Converts an amount from one currency to another using the latest rates.
- Simple command-line interface.
- Lists all the supported currencies.
- Can be run directly with Python or as a Docker container.

## Requirements

- Python 3.10+ (if running locally)
- Docker

### 1. Run with Docker

Clone the repo:
```sh
git clone https://github.com/vvvv5215/currency_converter_cli.git
```

Build the Docker image:
```sh
docker build -t currency-converter .
```

Run the container:
```sh
docker run --rm currency-converter <amount> <from_currency> <to_currency>
```

**Example:**
```sh
docker run --rm currency-converter 100 USD EUR
```

The above steps can be done with docker desktop too!

## Arguments

- `<amount>`: The amount of money to convert (e.g., `100`)
- `<from_currency>`: The currency code to convert from (e.g., `USD`)
- `<to_currency>`: The currency code to convert to (e.g., `EUR`)



## Working Screenshots
image.png


## Notes

- I have not used a seperate requirements.txt file as the only thing which I needed to install is *requests*, so directly gave the command in the Dockerfile.
- The tool uses the [Frankfurter API](https://www.frankfurter.app/) for up-to-date exchange rates.
- Only files needed for the build are included in the Docker image, thanks to `.dockerignore`.

