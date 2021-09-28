from web3 import Web3

from trophy_generator import generate_gif_from_winners, read_json_from_file

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
w3.isConnected()

class TrophyContract:
  def __init__(self):
    data = read_json_from_file('trophy_abi.json')
    contract_address = "0xCfEB869F69431e42cdB54A4F4f105C19C080A601"
    self.trophy = w3.eth.contract(address=Web3.toChecksumAddress(contract_address), abi=data['abi'])

  def generate_trophy_gif(self):
    token_id = 1

    years = self.trophy.functions.getYearsWithWinner().call()
    winners = [[str(year), self.trophy.functions.getWinnerName(token_id, year).call()] for year in years]

    generate_gif_from_winners(token_id, winners)
