![banner](https://raw.githubusercontent.com/teixeirazeus/validator-pizza-python/main/readme_assets/banner.png)[![Codacy Badge](https://app.codacy.com/project/badge/Grade/3d2350bb03a940419f857c8f89b90310)](https://www.codacy.com/gh/teixeirazeus/validator-pizza-python/dashboard?utm_source=github.com\&utm_medium=referral\&utm_content=teixeirazeus/validator-pizza-python\&utm_campaign=Badge_Grade)
[![License](https://raw.githubusercontent.com/teixeirazeus/validator-pizza-python/main/readme_assets/mit.svg)](http://opensource.org/licenses/MIT)

Validator Pizza Python is a library for http://validator.pizza which helps you verify if an email or domain is a disposable email service provider.

## Install

```bash
pip install validator-pizza-python
```

## Usage

```python
from validator_pizza_python import ValidatorPizza

PizzaValidator.validate("teixeira.zeus@gmail.com")
# EmailStatus(status=200, email='teixeira.zeus@gmail.com', domain='gmail.com', mx=True, disposable=False, alias=False, did_you_mean=None)

PizzaValidator.is_disposable("teixeira.zeus@gmail.com")
# False

PizzaValidator.is_disposable("gmail.com")
# False
```

### Async version

```python
from validator_pizza_python import AioPizzaValidator

pizza_client = AioPizzaValidator()
email_status = await pizza_cliente.validate("teixeira.zeus@gmail.com")
pizza_cliente.close()
```

## Developer

*   Thiago da Silva Teixeira

## License

Released under the [MIT License](http://opensource.org/licenses/MIT).
