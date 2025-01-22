import subprocess
import graphviz # type: ignore
urls = ["google.com", "github.com", "reddit.com", "twitter.com", "facebook.com", "amazon.com", "microsoft.com", "apple.com", "wikipedia.org", "youtube.com",  "spotify.com", "chess.com", "chat.openai.com", "disneyplus.com", "tiktok.com", "netflix.com", "hulu.com", "play.max.com", "read.amazon.com",  "tftacademy.com"] 

dot = graphviz.Graph('Internet', strict=True)


for url in urls:
    tr = subprocess.Popen(["traceroute", url], stdout=subprocess.PIPE)

    previous_hop = None 
    leaf_node = url 

    while True:
        line = tr.stdout.readline().decode().strip()
        if not line:
            break
        parts = line.split()
        if len(parts) > 1 and parts[1].count('.') == 3:  # Simple check for IP addresses
            ip_address = parts[1]
            print(ip_address)         
            dot.node(ip_address)
            if previous_hop:
                dot.edge(previous_hop, ip_address)
            previous_hop = ip_address

    if previous_hop:
        dot.node(leaf_node)
        dot.edge(previous_hop, leaf_node) 

dot.render('traceroute_map', format='pdf', cleanup=True)