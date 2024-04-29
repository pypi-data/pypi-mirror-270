import requests


def GetInfo(channel_name : str) :
  youtube = requests.get(f"https://www.googleapis.com/youtube/v3/search?part=snippet&type=channel&q={channel_name}&key=AIzaSyDBfcnjBerpgTFI5VCk_f3Rh-T_bc9LbEQ")
  if youtube.status_code == 200 :
     #get channel
      getchannel = youtube.json()["items"][0]
    
      channel_name = getchannel["snippet"]["title"]
  
      channel_id = getchannel["snippet"]["channelId"]
  
      channel_description = getchannel["snippet"]["description"]
        
      channel_profile = getchannel["snippet"]["thumbnails"]["default"]["url"]
  #JSON
      json = {
    "name" : channel_name,
    "description" : channel_description,
    "id" : channel_id,
    "profile_url" : channel_profile
    
  }
  
      print(json)
  else :
       print("Failed To Search Result!!")

