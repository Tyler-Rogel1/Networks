import subprocess
import graphviz

urls = ["google.com", "github.com", "reddit.com", "twitter.com", "facebook.com", "amazon.com", "microsoft.com", "apple.com", "wikipedia.org", "youtube.com"] 
def get_traceroute(url):
    tr = subprocess.Popen(["traceroute", url], stdout=subprocess.PIPE)
    hops = []
    while True:
        line = tr.stdout.readline().decode().strip()
        if not line:
            break
        # Extract the IP addresses from traceroute output (assuming they are in column 2)
        parts = line.split()
        if len(parts) > 1 and parts[1].count('.') == 3:  # Simple check for IP addresses
            hops.append(parts[1])
    return hops

def generate_graph(urls):
    dot = graphviz.Graph('Internet', strict=True)
    # Traverse each URL and add its hops to the graph
    for url in urls:
        hops = get_traceroute(url)
        prev_hop = None
        for hop in hops:
            dot.node(hop)  # Create a node for the hop
            if prev_hop:
                dot.edge(prev_hop, hop)  # Create an edge between consecutive hops
            prev_hop = hop
        dot.node(url, shape="doublecircle")  # Mark the final URL as a leaf node

    dot.render("traceroute_map", view=True)  # Render the graph


generate_graph(urls)