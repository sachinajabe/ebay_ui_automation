import requests
def test_get_description():
    try:
        response = requests.get("api.coindesk.com/v1/bpi/currentprice.json")
        assert response.status_code == 200
        actual = response.json()
        out= actual["bpi"]
        for item in out:
            if item == "GBP":
                assert "British Pound Sterling" == out[item]["description"]
    except Exception as e:
        print(f"test failed with the below exception {e}")