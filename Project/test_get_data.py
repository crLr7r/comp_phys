import requests

url = "https://api.openalex.org/works"

params = {
    "filter": "publication_year:2024,primary_topic.field.id:31",
    "per-page": 10
}
response = requests.get(url, params=params)
data = response.json()

#response = requests.get(url)

# print(response.status_code)
#
# data = response.json()
#
# print(type(data))
# print(data.keys())
#
# papers = data["results"]
#
# print(type(papers))
# print(len(papers))
# paper = papers[0]
#
# print(paper.keys())

def reconstruct_abstract(inverted_index):

    if inverted_index is None:
        return None

    words = []

    for word, positions in inverted_index.items():
        for position in positions:
            words.append((position, word))

    words.sort()

    abstract = " ".join(word for position, word in words)

    return abstract

def is_target_physics(paper):

    topic = paper.get("primary_topic")

    if topic is None:
        return False

    field = topic.get("field")
    subfield = topic.get("subfield")

    if field is None or subfield is None:
        return False

    # Physics and Astronomy가 아니면 제외
    if str(field["id"]).split("/")[-1] != "31":
        return False

    # Astronomy and Astrophysics 제외
    if str(subfield["id"]).split("/")[-1] == "3103":
        return False

    return True

papers = [
    paper for paper in data["results"]
    if is_target_physics(paper)
]

for paper in papers:

    abstract = reconstruct_abstract(
        paper["abstract_inverted_index"]
    )

    print("=" * 80)
    print("TITLE:")
    print(paper["title"])

    print("\nABSTRACT:")
    print(abstract)

