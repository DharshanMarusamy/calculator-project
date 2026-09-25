from app import app


def test_home_page():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200


def test_calculator_addition():
    client = app.test_client()

    response = client.post(
        "/",
        data={
            "num1": "10",
            "num2": "20",
            "operation": "add"
        }
    )

    assert b"30" in response.data