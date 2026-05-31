import json

WALLET_FILE = "paper_wallet.json"


def get_balance():

    try:
        with open(
            WALLET_FILE,
            "r"
        ) as f:

            data = json.load(f)

            return data.get(
                "balance",
                0
            )

    except:

        return 0


def save_balance(
    balance
):

    with open(
        WALLET_FILE,
        "w"
    ) as f:

        json.dump(
            {
                "balance": balance
            },
            f
        )
