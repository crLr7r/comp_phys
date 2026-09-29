import requests
import pandas as pd

SUBFIELDS = {
    "3106": "Nuclear and High Energy Physics",
    "3107": "Atomic and Molecular Physics, and Optics",
    "3104": "Condensed Matter Physics",
    "3109": "Statistical and Nonlinear Physics",
    "3108": "Radiation",
    "3105": "Instrumentation",
    "3102": "Acoustics and Ultrasonics"
} # 천문학 제외

# abstract(초록)을 문장 형태로 변환
def reconstruct_abstract(inverted_index):
    if inverted_index is None:
        return None

    words = []

    for word, positions in inverted_index.items():
        for position in positions:
            words.append((position, word))

    words.sort()

    return " ".join(word for position, word in words)

#subfield_name 분야의 물리 논문을 [start_year, end_year]범위로 target_count개만큼 수집
def collect_subfield_papers(
        start_year,
        end_year,
        subfield_id,
        subfield_name,
        target_count=100,
        seed=42
):
    papers = []

    url = "https://api.openalex.org/works"

    year_count = (end_year - start_year + 1)
    year_target_count = year_count * [target_count // year_count]

    if target_count %  year_count != 0:
        for i in range(target_count - year_count * (target_count // year_count)):
            year_target_count[-(i+1)] += 1

    for i, year in enumerate(range(start_year, end_year + 1)):
        params = {
            "filter": (
                f"publication_year:{year},"
                f"primary_topic.subfield.id:{subfield_id},"
                f"has_abstract:true,"  # 초록이 있는 것만 받아옴
                f"language:en"
            ),
            "sample": year_target_count[i],
            "seed": seed,  # 랜덤으로 뽑겠다는 뜻
            "per-page": min(year_target_count[i], 200),  # 200개씩 받아옴(한 번에 5000개를 받아올 순 없음)
            "cursor": "*"
        }
        while len(papers) < sum(year_target_count[:i + 1]):
            response = requests.get(url, params=params)
            response.raise_for_status()

            data = response.json()

            for paper in data["results"]:

                abstract = reconstruct_abstract(
                    paper.get("abstract_inverted_index")
                )

                if abstract is None:
                    continue

                topics = [
                    topic["display_name"]
                    for topic in paper.get("topics", [])
                ]

                topics = " | ".join(topics)
                papers.append({
                    "id": paper["id"],
                    "year": paper["publication_year"],
                    "subfield_id": subfield_id,
                    "subfield": subfield_name,
                    "topics": topics,
                    "title": paper["title"],
                    "abstract": abstract
                })

            next_cursor = data["meta"].get("next_cursor")

            if not next_cursor:
                break

            params["cursor"] = next_cursor

    return papers[:target_count]

def collect_papers(start_year, end_year, n_per_subfield=100):

    all_papers = []

    for i, (subfield_id, subfield_name) in enumerate(SUBFIELDS.items()):

        print()
        print("Collecting:", subfield_name)

        papers = collect_subfield_papers(
            start_year=start_year,
            end_year=end_year,
            subfield_id=subfield_id,
            subfield_name=subfield_name,
            target_count=n_per_subfield,

            # 분야마다 다른 seed
            seed=42 + i
        )

        print("→", len(papers), "papers")

        all_papers.extend(papers)

    return all_papers

def save_papers(start_year, end_year, n_per_subfield=100):
    papers = collect_papers(start_year, end_year, n_per_subfield=n_per_subfield)

    df = pd.DataFrame(papers)

    df.to_csv(
        f"physics_{start_year}_{end_year}.csv",
        index=False,
        encoding="utf-8-sig"
    )

    print(df.head())

if __name__ == "__main__":
    save_papers(
        start_year=2000,
        end_year=2004,
        n_per_subfield=1000
    )

