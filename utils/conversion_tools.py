import requests

class Conversion:
    """ currency converter using exchangerate-api """

    BASE_URL = "https://api.exchangerate-api.com/v4/latest/"

    def convert(self, amount: float, from_currency: str, to_currency: str):
        """ currency conversion """
        try:
            url = self.BASE_URL + from_currency.upper()
            res = requests.get(url)
            data = res.json()

            if to_currency.upper() in data["rates"]:
                rate = data["rates"][to_currency.upper()]
                result = amount * rate
                return f"{amount} {from_currency.upper()} = {result:.2f} {to_currency.upper()}"
            else:
                return f"Not support {to_currency}"
        except Exception as e:
            return f"error: {e}"

    def get_rate(self, base_currency: str, target_currency: str):
        """ exchange rate """
        try:
            url = self.BASE_URL + base_currency.upper()
            res = requests.get(url)
            data = res.json()

            if target_currency.upper() in data["rates"]:
                rate = data["rates"][target_currency.upper()]
                return f"1 {base_currency.upper()} = {rate:.4f} {target_currency.upper()}"
            else:
                return f"Not support {target_currency}"
        except Exception as e:
            return f"error: {e}"
