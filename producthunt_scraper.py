import requests
import json

ACCESS_TOKEN = "RFKvcNZMAXsxGl5SBE6KzTI2ZWeK832_vrBPwWviFb8"
url = "https://api.producthunt.com/v2/api/graphql"

query = """
{
  posts(order: VOTES, first: 10) {
    edges {
      node {
        name
        tagline
        votesCount
        commentsCount
        topics {
          edges {
            node {
              name
            }
          }
        }
      }
    }
  }
}
"""

headers = {
    "Authorization": f"Bearer {ACCESS_TOKEN}",
    "Content-Type": "application/json"
}

response = requests.post(url, headers=headers, json={"query": query})
raw_data = response.json()

if "data" in raw_data:
    posts = raw_data["data"]["posts"]["edges"]
    output = []
    for post in posts:
        node = post["node"]
        output.append({
            "name": node["name"],
            "tagline": node["tagline"],
            "upvotes": node["votesCount"],
            "comments": node["commentsCount"],
            "tags": [t["node"]["name"] for t in node["topics"]["edges"]]
        })

    with open("output.json", "w") as f:
        json.dump(output, f, indent=2)
    print("✅ Data saved to output.json")
else:
    print("❌ Failed. Response was:")
    print(json.dumps(raw_data, indent=2))
