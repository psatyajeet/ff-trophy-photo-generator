import requests
from web3 import Web3

from trophy_generator import generate_gif_from_winners, read_json_from_file

w3 = Web3(Web3.HTTPProvider('http://127.0.0.1:8545'))
# w3 = Web3(Web3.WebsocketProvider('ws://127.0.0.1:8545'))
w3.isConnected()

class TrophyContract:
  def __init__(self):
    data = read_json_from_file('trophy_abi.json')
    contract_address = "0x6Ff7512C3EE412300Df94964D10A9f6D5D70B506"
    self.trophy = w3.eth.contract(address=Web3.toChecksumAddress(contract_address), abi=data['abi'])

  def get_contract(self):
    return self.trophy

  def get_league_name(self, token_id):
    league_name = self.trophy.functions.getLeagueName(token_id).call()
    return league_name

  def get_winners(self, token_id):
    years = self.trophy.functions.getYearsWithWinner(token_id).call()
    winners = [[str(year), self.trophy.functions.getWinnerName(token_id, year).call()] for year in years]

    return winners

  def generate_trophy_for_token_id(self, token_id):
    # league_name = self.trophy.functions.getLeagueName(token_id).call()
    # years = self.trophy.functions.getYearsWithWinner(token_id).call()
    # winners = [[str(year), self.trophy.functions.getWinnerName(token_id, year).call()] for year in years]
    league_name = self.get_league_name(token_id)
    winners = self.get_winners(token_id)

    generate_gif_from_winners(token_id, league_name, winners)

  # def get_all_events_since_block(self, from_block):
  #   events = self.trophy.events.WinnerNameSet.createFilter(fromBlock=from_block).get_all_entries()
  #   return events

  # def generate_new_trophy_for_new_WinnerNameSet(self, from_block):
  #   events = self.get_all_events_since_block(from_block)

  #   for event in events:
  #     token_id = event.args.tokenId
  #     token_uri = self.trophy.functions.tokenURI(token_id).call()
  #     r = requests.get(token_uri)
  #     print(r.json()['image'])
  #     self.generate_trophy_gif(event.args.tokenId)

  def get_metadata(self, token_id):
    league_name = self.get_league_name(token_id)
    winners = self.get_winners(token_id)
    metadata = {
        "image": f"https://1hzjyv5tlg.execute-api.us-west-1.amazonaws.com/trophy/image/{token_id}", 
        "league_name": league_name,
        "winners": winners
      }

    return metadata


