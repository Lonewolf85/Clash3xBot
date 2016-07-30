import urllib3
import json
http = urllib3.PoolManager()
bearer_token = {
	"Accept": "application/json",
	"authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6IjUyNjdiNTVhLTNlMGMtNDRkNS1iOGM4LTZhNDZlNTNlZGY3MCIsImlhdCI6MTQ2OTg3MDQ0Miwic3ViIjoiZGV2ZWxvcGVyLzlhYjRlMjc1LWZmZjQtYWQ5YS05OGJmLWY0NTBlOGVhMTdjYSIsInNjb3BlcyI6WyJjbGFzaCJdLCJsaW1pdHMiOlt7InRpZXIiOiJkZXZlbG9wZXIvc2lsdmVyIiwidHlwZSI6InRocm90dGxpbmcifSx7ImNpZHJzIjpbIjEwMy4yNTIuMjQuMjA1Il0sInR5cGUiOiJjbGllbnQifV19.sJdZYGaSu_sMAXmNG_Gf1sM3UkyDaJy9fz7Yxr-rrVCFHTOBXI2WPeBiEzBCAoWBsqw02AfGeVshulwWq1zpcw"
	}


#search clans based on clan name
def search_clans(name):
	try:
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
	except:
		return_str = "No clans found!"
	return return_str


#search clans based on clan tag
def search_clans_tag(tag):
	try:
		url = "https://api.clashofclans.com/v1/clans/"
		search_token = tag
		url = url + search_token
		r = http.request("GET",url,headers=bearer_token)
		json_string = r.data.decode('utf-8')
		clan = json.loads(json_string)
		return_str = ""
	
		return_str += "Clan name: {0} | Tag: {1}".format(clan['name'],clan['tag'])
		return_str +="\nWar wins : {0}\n".format(clan['warWins'])
	except:
		return_str = "No clans found!"
	return return_str


#get members list of a clan based on clan tag
def get_clan_members(tag):
	try:
		url = "https://api.clashofclans.com/v1/clans/"
		search_token = tag
		url = url + search_token + "/members"
		r = http.request("GET",url,headers=bearer_token)
		json_string = r.data.decode('utf-8')
		members_list = json.loads(json_string)
		
		return_str = ""
	
		for member in members_list["items"]:
			return_str += "Member Name: {0} | Experience : {1} \n".format(member['name'],member['expLevel'])
			#return_str +=" \nClan Rank: {0} | Trophies: {1} | Role: {2}\n\n".format(member['clanRank'],member['trophies'],member['role'])
	except:
		return_str = "No clans found!"
		
	return return_str


#get warlog list of a clan based on clan tag
def get_warlogs(tag):
	try:
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
	except:
		return_str = "No clans found!"


def main():
	#get_clan_members("%239L0QVRGY")
	print(get_clan_members("%239L0QVRGY"))

if __name__ == "__main__":
	main()
