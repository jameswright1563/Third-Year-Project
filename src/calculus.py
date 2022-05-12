import urllib

import requests
import wolframalpha


class Calculus:
    def __init__(self):
        self.appid = "W7YJ9Q-85R328TAWQ"
        self.client = wolframalpha.Client(self.appid)

    def getData(self, query):

        query = urllib.parse.quote_plus(f"{query}")
        query_url = f"http://api.wolframalpha.com/v2/query?" \
                    f"appid=W7YJ9Q-85R328TAWQ" \
                    f"&input={query}" \
                    f"&scanner=Solve" \
                    f"&podstate=Result__Step-by-step+solution" \
                    "&format=plaintext" \
                    f"&output=json"

        r = requests.get(query_url).json()
        data = r["queryresult"]["pods"][0]["subpods"]
        result = data[0]["plaintext"]
        steps = data[1]["plaintext"]
        return result, steps

    def differentiation(self, values):
        if values["difforder"] == 1:
            res = self.client.query("d" + "/dx(" + values["diffeq"] + ")")
        else:
            res = self.client.query(
                "d^" + str(values["difforder"]) + "/dx^" + str(values["difforder"]) + "(" + values[
                    "diffeq"] + ")")
        return res

    def integration(self, values):
        try:
            high = int(values["integup"])
            low = int(values["integlow"])
            res = "Integrate[" + str(values["integeq"]) + ",{x," + str(low) + "," + str(high) + "}]"

        except ValueError:
            res = "Integrate[" + values["integeq"] + "]"
        return self.client.query(res)

