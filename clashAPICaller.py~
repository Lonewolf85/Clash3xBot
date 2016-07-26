import urllib3
import json
http = urllib3.PoolManager()
bearer_token = {
	"Accept": "application/json",
	"authorization": "Bearer token"
	}


#search clans based on clan name
def search_clans(name):
	url = "https://api.clashofclans.com/v1/clans?"
	search_token = "name="+name
	url = url + search_token
	r = http.request("GET",url,headers=bearer_token)
	json_string = r.data.decode('utf-8')
	clans_list = json.loads(json_string)["items"]
	return_str = ""
	for clan in clans_list[0:10]:
		return_str += "Clan name: {0} | Tag: {1}".format(clan['name'],clan['tag'])
		return_str +="\nWar wins : {0}\n".format(clan['warWins'])
	return return_str


#search clans based on clan tag
def search_clans_tag(tag):
	url = "https://api.clashofclans.com/v1/clans/"
	search_token = tag
	url = url + search_token
	r = http.request("GET",url,headers=bearer_token)
	json_string = r.data.decode('utf-8')
	clan = json.loads(json_string)
	return_str = ""
	return_str += "Clan name: {0} | Tag: {1}".format(clan['name'],clan['tag'])
	return_str +="\nWar wins : {0}\n".format(clan['warWins'])
	return return_str


#get members list of a clan based on clan tag
def get_clan_members(tag):
	url = "https://api.clashofclans.com/v1/clans/"
	search_token = tag
	url = url + search_token + "/members"
	r = http.request("GET",url,headers=bearer_token)
	json_string = r.data.decode('utf-8')
	members_list = json.loads(json_string)
	
	return_str = ""
	for member in members_list["items"]:
		return_str += "Member Name: {0} | Experience : {1} ".format(member['name'],member['expLevel'])
		return_str +=" \nClan Rank: {0} | Trophies: {1} | Role: {2}\n\n".format(member['clanRank'],member['trophies'],member['role'])
		
	return return_str


#get warlog list of a clan based on clan tag
def get_warlogs(tag):
	url = "https://api.clashofclans.com/v1/clans/"
	search_token = tag
	url = url + search_token + "/warlog"
	r = http.request("GET",url,headers=bearer_token)
	json_string = r.data.decode('utf-8')
	warlog = json.loads(json_string)
	return_str = ""
	for war in warlog["items"][0:5]:
		return_str += "Result: {0} vs {1} | End Date : {2} \n".format(war['result'],war['opponent']['name'],war['endTime'][6:8]+"/"+war['endTime'][4:6])
		return_str += "Result: {0} vs {1} \n\n".format(war['clan']['stars'],war['opponent']['stars'])
	return return_str


def main():
	#get_clan_members("%239L0QVRGY")
	get_warlogs("%239L0QVRGY")

if __name__ == "__main__":
	main()
