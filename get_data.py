import requests

url = "https://stack_overflow_queries.p.rapidapi.com/json_data"

headers = {
	"X-RapidAPI-Key": "c12a4fcf8emshf19712541926cdcp19ec27jsn683bd634421e",
	"X-RapidAPI-Host": "stack_overflow_queries.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers)


with open("data.xml", "w") as f:
	f.write(response.text)