# Import the libraries needed
# !pip install tinydb
from tinydb import TinyDB, Query

# Initialize TinyDB and create a table named 'crypto_info', we will save the data here
db = TinyDB('crypto_info_db.json')
crypto_table = db.table('crypto_info')

# Here we create a dictionary with all the cryptocurrencies as keys and their respective data as values.
crypto_info = {
   "AAVE-USD": {"NIF": "AAVE-USD", "Smart_Contract": True, "name": "Aave", "Founder": "Stani Kulechov",
                "Date_Founded": "2020-11-25",
                "Consensus_Mechanism": "Delegated Proof of Stake", "Max_Supply": 16000000,
                "Circulating_Supply": 13089010,
                "Total_Supply": 16000000, "Market_Cap": 4533300000, "Website": "https://aave.com/",
                "Whitepaper": "https://aave.com/whitepaper.pdf",
                "Github": "https://github.com/aave/aave-protocol",
                "Reddit": "https://www.reddit.com/r/Aave_Official/"},


   "ADA-USD": {"NIF": "ADA-USD", "Smart_Contract": True, "Algorithm": "Ouroboros", "name": "Cardano",
               "Founder": "Charles Hoskinson", "Date_Founded": "2017-09-29",
               "Consensus_Mechanism": "Ouroboros", "Max_Supply": 45000000000, "Circulating_Supply": 33400788494,
               "Total_Supply": 45000000000, "Market_Cap": 57361439871, "Website": "https://www.cardano.org/",
               "Whitepaper": "https://www.cardano.org/en/academic-papers/",
               "Github": "https://github.com/input-output-hk/cardano", "Reddit": "https://www.reddit.com/r/cardano/"},


   "ALGO-USD": {"NIF": "ALGO-USD", "Smart_Contract": True, "Algorithm": "Algorand", "name": "Algorand",
                "Founder": "Silvio Micali", "Date_Founded": "2019-06-20",
                "Consensus_Mechanism": "Pure Proof of Stake", "Max_Supply": 10000000000,
                "Circulating_Supply": 6108289491,
                "Total_Supply": 10000000000, "Market_Cap": 7921753789, "Website": "https://www.algorand.com/",
                "Whitepaper": "https://www.algorand.com/resources/white-papers/",
                "Github": "https://github.com/algorand", "Reddit": "https://www.reddit.com/r/AlgorandOfficial/"},


   "AVAX-USD": {"NIF": "AVAX-USD", "Smart_Contract": True, "Algorithm": "Avalanche", "name": "Avalanche",
                "Founder": "Emin Gün Sirer", "Date_Founded": "2020-09-21",
                "Consensus_Mechanism": "Snowman", "Max_Supply": 720000000, "Circulating_Supply": 220078037,
                "Total_Supply": 720000000, "Market_Cap": 5169715677, "Website": "https://www.avax.network/",
                "Whitepaper": "https://www.avax.network/whitepapers",
                "Github": "https://github.com/ava-labs", "Reddit": "https://www.reddit.com/r/Avax/"},


   "BAT-USD": {"NIF": "BAT-USD", "Smart_Contract": True, "name": "Basic Attention Token", "Founder": "Brendan Eich",
               "Date_Founded": "2017-05-31",
               "Website": "https://basicattentiontoken.org/",
               "Whitepaper": "https://basicattentiontoken.org/whitepaper.pdf",
               "Github": "https://github.com/brave-intl", "Reddit": "https://www.reddit.com/r/BATProject/"},


   "BCH-USD": {"NIF": "BCH-USD", "Smart_Contract": False, "Algorithm": "SHA-256", "name": "Bitcoin Cash",
               "Founder": "Roger Ver", "Date_Founded": "2017-08-01",
               "Consensus_Mechanism": "Proof of Work", "Max_Supply": 21000000, "Circulating_Supply": 18962231,
               "Total_Supply": 21000000, "Market_Cap": 9773306195, "Website": "https://www.bitcoincash.org/",
               "Github": "https://github.com/bitcoincashorg/", "Reddit": "https://www.reddit.com/r/btc/"},


   "BNB-USD": {"NIF": "BNB-USD", "Smart_Contract": True, "Algorithm": "BFT", "name": "Binance Coin",
               "Founder": "Changpeng Zhao", "Date_Founded": "2017-07-25",
               "Consensus_Mechanism": "Delegated Byzantine Fault Tolerance", "Max_Supply": 170532785,
               "Circulating_Supply": 168137036,
               "Total_Supply": 170532785, "Market_Cap": 98432770066, "Website": "https://www.binance.org/",
               "Reddit": "https://www.reddit.com/r/binance/"},


   "BTC-USD": {"NIF": "BTC-USD", "Smart_Contract": False, "Algorithm": "SHA-256", "name": "Bitcoin",
               "Founder": "Satoshi Nakamoto", "Date_Founded": "2009-01-03",
               "Consensus_Mechanism": "Proof of Work", "Max_Supply": 21000000, "Circulating_Supply": 18796100,
               "Total_Supply": 21000000, "Market_Cap": 969752149505, "Website": "https://bitcoin.org/",
               "Whitepaper": "https://bitcoin.org/bitcoin.pdf",
               "Github": "https://github.com/bitcoin", "Reddit": "https://www.reddit.com/r/Bitcoin/"},


   "COMP-USD": {"NIF": "COMP-USD", "Smart_Contract": True, "Algorithm": "Solidity", "name": "Compound",
                "Founder": "Robert Leshner", "Date_Founded": "2018-09-27",
                "Consensus_Mechanism": "Delegated Proof of Stake", "Max_Supply": 10000000,
                "Circulating_Supply": 5358876,
                "Total_Supply": 10000000, "Market_Cap": 1793281440, "Website": "https://compound.finance/",
                "Whitepaper": "https://compound.finance/documents/Compound.Whitepaper.pdf",
                "Github": "https://github.com/compound-finance", "Reddit": "https://www.reddit.com/r/Compound/"},


   "CRV-USD": {"NIF": "CRV-USD", "Smart_Contract": True, "Algorithm": "Ethereum", "name": "Curve DAO Token",
               "Founder": "Michael Egorov", "Date_Founded": "2020-08-14",
               "Consensus_Mechanism": "Proof of Stake", "Max_Supply": 322812538,
               "Circulating_Supply": 282188810,
               "Total_Supply": 122812538, "Market_Cap": 858776120, "Website": "https://curve.fi/",
               "Github": "https://github.com/curvefi", "Reddit": "https://www.reddit.com/r/curvefi/"},


   "DOGE-USD": {"NIF": "DOGE-USD", "Smart_Contract": False, "name": "Dogecoin", "Founder": "Billy Markus",
                "Date_Founded": "2013-12-06",
                "Consensus_Mechanism": "Proof of Work", "Max_Supply": 131265366, "Circulating_Supply": 131265366,
                "Total_Supply": 131265366, "Market_Cap": 4609303425, "Website": "https://dogecoin.com/",
                "Github": "https://github.com/dogecoin/", "Reddit": "https://www.reddit.com/r/dogecoin/"},


   "DOT1-USD": {"NIF": "DOT1-USD", "Smart_Contract": True, "name": "Polkadot",
                "Founder": "Gavin Wood", "Date_Founded": "2020-05-26",
                "Consensus_Mechanism": "Nominated Proof of Stake", "Max_Supply": 108706476,
                "Circulating_Supply": 109713622,
                "Total_Supply": 108706476, "Market_Cap": 34022090646, "Website": "https://polkadot.network/",
                "Whitepaper": "https://polkadot.network/Polkadot-lightpaper.pdf",
                "Github": "https://github.com/paritytech/polkadot", "Reddit": "https://www.reddit.com/r/polkadot_market/"},


   "ETH-USD": {"NIF": "ETH-USD", "Smart_Contract": True, "Algorithm": "Solidity", "name": "Ethereum",
               "Founder": "Vitalik Buterin", "Date_Founded": "2015-07-30",
               "Consensus_Mechanism": "Ethash", "Circulating_Supply": 120504221, "Market_Cap": 562270864446, "Website": "https://ethereum.org/",
               "Whitepaper": "https://ethereum.org/en/whitepaper/",
               "Github": "https://github.com/ethereum", "Reddit": "https://www.reddit.com/r/ethereum/"},


   "FIL-USD": {"NIF": "FIL-USD", "Smart_Contract": True, "Algorithm": "Proof of Space", "name": "Filecoin",
               "Founder": "Juan Benet", "Date_Founded": "2017-07-19",
               "Consensus_Mechanism": "Proof of Replication", "Max_Supply": 2000000000,
               "Circulating_Supply": 95210831,
               "Total_Supply": 2000000000, "Market_Cap": 3158363078, "Website": "https://filecoin.io/",
               "Whitepaper": "https://filecoin.io/filecoin.pdf",
               "Github": "https://github.com/filecoin-project/", "Reddit": "https://www.reddit.com/r/filecoin/"},


   "LINK-USD": {"NIF": "LINK-USD", "Smart_Contract": True, "Algorithm": "Solidity", "name": "Chainlink",
                "Founder": "Sergey Nazarov", "Date_Founded": "2017-09-19",
                "Consensus_Mechanism": "Oraclized Polkadot", "Max_Supply": 1000000000,
                "Circulating_Supply": 464509553,
                "Total_Supply": 1000000000, "Market_Cap": 17211853560, "Website": "https://chain.link/",
                "Whitepaper": "https://link.smartcontract.com/whitepaper",
                "Github": "https://github.com/smartcontractkit", "Reddit": "https://www.reddit.com/r/chainlink/"},


   "LTC-USD": {"NIF": "LTC-USD", "Smart_Contract": False, "Algorithm": "Scrypt", "name": "Litecoin",
               "Founder": "Charlie Lee", "Date_Founded": "2011-10-07",
               "Consensus_Mechanism": "Proof of Work", "Max_Supply": 84000000, "Circulating_Supply": 67848315,
               "Total_Supply": 84000000, "Market_Cap": 10393749894, "Website": "https://litecoin.org/",
               "Github": "https://github.com/litecoin-project", "Reddit": "https://www.reddit.com/r/litecoin/"},


   "MKR-USD": {"NIF": "MKR-USD", "Smart_Contract": True, "Algorithm": "Solidity", "name": "Maker",
               "Founder": "Rune Christensen", "Date_Founded": "2015-12-17",
               "Consensus_Mechanism": "Proof of Stake", "Max_Supply": 1005578, "Circulating_Supply": 995579,
               "Total_Supply": 1005578, "Market_Cap": 4472297359, "Website": "https://makerdao.com/",
               "Whitepaper": "https://makerdao.com/whitepaper/",
               "Github": "https://github.com/makerdao", "Reddit": "https://www.reddit.com/r/MakerDAO/"},


   "OMG-USD": {"NIF": "OMG-USD", "Smart_Contract": True, "Algorithm": "Solidity", "name": "OMG Network",
               "Founder": "Jun Hasegawa", "Date_Founded": "2017-06-27",
               "Consensus_Mechanism": "Plasma", "Max_Supply": 140245398, "Circulating_Supply": 140245398,
               "Total_Supply": 140245398, "Market_Cap": 1567815084, "Website": "https://omg.network/",
               "Github": "https://github.com/omgnetwork/", "Reddit": "https://www.reddit.com/r/omise_go/"},


   "SNX-USD": {"NIF": "SNX-USD", "Smart_Contract": True, "Algorithm": "Solidity", "name": "Synthetix",
               "Founder": "Kain Warwick", "Date_Founded": "2017-03-01",
               "Consensus_Mechanism": "Ethereum", "Max_Supply": 217317950, "Circulating_Supply": 212408269,
               "Total_Supply": 217317950, "Market_Cap": 1170085134, "Website": "https://www.synthetix.io/",
               "Whitepaper": "https://www.synthetix.io/assets/Synthetix.io%20Litepaper.pdf",
               "Github": "https://github.com/Synthetixio", "Reddit": "https://www.reddit.com/r/synthetix_io/"},


   "SOL1-USD": {"NIF": "SOL1-USD", "Smart_Contract": True, "Algorithm": "Rust", "name": "Solana",
                "Founder": "Anatoly Yakovenko", "Date_Founded": "2020-03-20",
                "Consensus_Mechanism": "Proof of History", "Circulating_Supply": 489288547, "Market_Cap": 4696540927, "Website": "https://solana.com/",
                "Whitepaper": "https://solana.com/solana-whitepaper.pdf",
                "Github": "https://github.com/solana-labs", "Reddit": "https://www.reddit.com/r/solana/"},


   "UNI3-USD": {"NIF": "UNI3-USD", "Smart_Contract": True, "Algorithm": "Solidity", "name": "Uniswap",
                "Founder": "Hayden Adams", "Date_Founded": "2018-11-02",
                "Consensus_Mechanism": "Ethereum", "Max_Supply": 1000000000,
                "Circulating_Supply": 543217848,
                "Total_Supply": 1000000000, "Market_Cap": 11534016108, "Website": "https://uniswap.org/",
                "Whitepaper": "https://uniswap.org/whitepaper.pdf",
                "Github": "https://github.com/Uniswap", "Reddit": "https://www.reddit.com/r/UniSwap/"},


   "XLM-USD": {"NIF": "XLM-USD", "Smart_Contract": True, "Algorithm": "Stellar Consensus Protocol", "name": "Stellar",
               "Founder": "Jed McCaleb", "Date_Founded": "2014-07-31",
               "Consensus_Mechanism": "Federated Byzantine Agreement", "Max_Supply": 50001806857,
               "Circulating_Supply": 23890568305,
               "Total_Supply": 50001806857, "Market_Cap": 3989156879, "Website": "https://www.stellar.org/",
               "Whitepaper": "https://www.stellar.org/papers/stellar-consensus-protocol.pdf",
               "Github": "https://github.com/stellar", "Reddit": "https://www.reddit.com/r/Stellar/"},


   "XRP-USD": {"NIF": "XRP-USD", "Smart_Contract": False, "name": "XRP", "Founder": "Chris Larsen", "Date_Founded": "2012-04-18",
               "Consensus_Mechanism": "Proof of Correctness", "Max_Supply": 100000000000, "Circulating_Supply": 99991841584,
               "Total_Supply": 100000000000, "Market_Cap": 25362297829, "Website": "https://ripple.com/xrp/",
               "Github": "https://github.com/ripple/", "Reddit": "https://www.reddit.com/r/Ripple/"},


   "XTZ-USD": {"NIF": "XTZ-USD", "Smart_Contract": True, "Algorithm": "LPOS", "name": "Tezos",
               "Founder": "Arthur Breitman", "Date_Founded": "2018-09-17",
               "Consensus_Mechanism": "Liquid Proof of Stake", "Circulating_Supply": 872823528,"Market_Cap": 3519634653, "Website": "https://tezos.com/",
               "Whitepaper": "https://www.tezos.com/static/papers/white_paper.pdf",
               "Github": "https://gitlab.com/tezos/tezos", "Reddit": "https://www.reddit.com/r/tezos/"},


   "ZEC-USD": {"NIF": "ZEC-USD", "Smart_Contract": False, "name": "Zcash", "Founder": "Zooko Wilcox",
               "Date_Founded": "2016-10-28",
               "Consensus_Mechanism": "Equihash", "Max_Supply": 21000000, "Circulating_Supply": 13366406,
               "Total_Supply": 21000000, "Market_Cap": 679155826, "Website": "https://z.cash/",
               "Github": "https://github.com/zcash", "Reddit": "https://www.reddit.com/r/zec/"},


   "AAVE-USD": {"NIF": "AAVE-USD", "Smart_Contract": True, "Algorithm": "Solidity", "name": "Aave",
                "Founder": "Stani Kulechov", "Date_Founded": "2017-11-15",
                "Consensus_Mechanism": "Ethereum", "Max_Supply": 16000000, "Circulating_Supply": 12000000,
                "Total_Supply": 16000000, "Market_Cap": 4262912126, "Website": "https://aave.com/",
                "Whitepaper": "https://aave.com/AAVE_whitepaper.pdf",
                "Github": "https://github.com/aave/", "Reddit": "https://www.reddit.com/r/Aave/"},


   "EOS-USD": {"NIF": "EOS-USD", "Smart_Contract": True, "Algorithm": "C++", "name": "EOS.IO",
               "Founder": "Daniel Larimer", "Date_Founded": "2017-06-26",
               "Consensus_Mechanism": "Delegated Proof of Stake", "Circulating_Supply": 973041667, "Market_Cap": 5442480469, "Website": "https://eos.io/",
               "Github": "https://github.com/eosio", "Reddit": "https://www.reddit.com/r/eos/"},


   "LINK-USD": {"NIF": "LINK-USD", "Smart_Contract": True, "Algorithm": "Solidity", "name": "Chainlink",
                "Founder": "Sergey Nazarov", "Date_Founded": "2017-09-19",
                "Consensus_Mechanism": "Oraclized Polkadot", "Max_Supply": 1000000000,
                "Circulating_Supply": 464509553,
                "Total_Supply": 1000000000, "Market_Cap": 17211853560, "Website": "https://chain.link/",
                "Whitepaper": "https://link.smartcontract.com/whitepaper",
                "Github": "https://github.com/smartcontractkit", "Reddit": "https://www.reddit.com/r/chainlink/"},


   "SOL1-USD": {"NIF": "SOL1-USD", "Smart_Contract": True, "Algorithm": "Rust", "name": "Solana",
                "Founder": "Anatoly Yakovenko", "Date_Founded": "2020-03-20",
                "Consensus_Mechanism": "Proof of History",
                "Circulating_Supply": 489288547, "Market_Cap": 4696540927, "Website": "https://solana.com/",
                "Whitepaper": "https://solana.com/solana-whitepaper.pdf",
                "Github": "https://github.com/solana-labs", "Reddit": "https://www.reddit.com/r/solana/"},


   "UNI3-USD": {"NIF": "UNI3-USD", "Smart_Contract": True, "Algorithm": "Solidity", "name": "Uniswap",
                "Founder": "Hayden Adams", "Date_Founded": "2018-11-02",
                "Consensus_Mechanism": "Ethereum", "Max_Supply": 1000000000,
                "Circulating_Supply": 543217848,
                "Total_Supply": 1000000000, "Market_Cap": 11534016108, "Website": "https://uniswap.org/",
                "Whitepaper": "https://uniswap.org/whitepaper.pdf",
                "Github": "https://github.com/Uniswap", "Reddit": "https://www.reddit.com/r/UniSwap/"},


   "XLM-USD": {"NIF": "XLM-USD", "Smart_Contract": True, "Algorithm": "Stellar Consensus Protocol", "name": "Stellar",
               "Founder": "Jed McCaleb", "Date_Founded": "2014-07-31",
               "Consensus_Mechanism": "Federated Byzantine Agreement", "Max_Supply": 50001806857,
               "Circulating_Supply": 23890568305,
               "Total_Supply": 50001806857, "Market_Cap": 3989156879, "Website": "https://www.stellar.org/",
               "Whitepaper": "https://www.stellar.org/papers/stellar-consensus-protocol.pdf",
               "Github": "https://github.com/stellar", "Reddit": "https://www.reddit.com/r/Stellar/"},


   "XRP-USD": {"NIF": "XRP-USD", "Smart_Contract": False, "name": "XRP", "Founder": "Chris Larsen", "Date_Founded": "2012-04-18",
               "Consensus_Mechanism": "Proof of Correctness", "Max_Supply": 100000000000, "Circulating_Supply": 99991841584,
               "Total_Supply": 100000000000, "Market_Cap": 25362297829, "Website": "https://ripple.com/xrp/",
               "Github": "https://github.com/ripple/", "Reddit": "https://www.reddit.com/r/Ripple/"},


   "XTZ-USD": {"NIF": "XTZ-USD", "Smart_Contract": True, "Algorithm": "LPOS", "name": "Tezos",
               "Founder": "Arthur Breitman", "Date_Founded": "2018-09-17",
               "Consensus_Mechanism": "Liquid Proof of Stake", "Circulating_Supply": 872823528, "Market_Cap": 3519634653, "Website": "https://tezos.com/",
               "Whitepaper": "https://www.tezos.com/static/papers/white_paper.pdf",
               "Github": "https://gitlab.com/tezos/tezos", "Reddit": "https://www.reddit.com/r/tezos/"},


   "ZEC-USD": {"NIF": "ZEC-USD", "Smart_Contract": False, "name": "Zcash", "Founder": "Zooko Wilcox",
               "Date_Founded": "2016-10-28",
               "Consensus_Mechanism": "Equihash", "Max_Supply": 21000000, "Circulating_Supply": 13366406,
               "Total_Supply": 21000000, "Market_Cap": 679155826, "Website": "https://z.cash/",
               "Github": "https://github.com/zcash", "Reddit": "https://www.reddit.com/r/zec/"}
}


# The following line inserts the dictionary with the crypto information into the database
crypto_table.insert_multiple(crypto_info.values())

# Define a query to retrieve all data
query = Query()
all_crypto_data = crypto_table.all()

# Print all data
for data in all_crypto_data:
   print(data)

# Example: Retrieve data for a specific cryptocurrency by its NIF
specific_crypto = crypto_table.get(query.NIF == 'BTC-USD')
print("Data for BTC-USD:", specific_crypto)
