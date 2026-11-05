from retriever import load_docs, retrieve
from generator import vanilla_answer, grounded_answer
from guardrail import InvalidQueryError, validate_query

def main():
    docs = load_docs()

    print("Welcome to the Mini-RAG Demo.")
    while True:
        try:
            query = validate_query(input("Ask a question: "))
            break
        except InvalidQueryError as error:
            print(f"Invalid input: {error}")

    print("\n--- Without Retrieval (Vanilla AI) ---")
    print(vanilla_answer(query))

    print("\n--- Retrieving Context ---")
    results = retrieve(query, docs)
    if not results:
        print("No relevant matches found.")

    print("\n--- With Retrieval (Grounded Answer) ---")
    print(grounded_answer(query, results))


if __name__ == "__main__":
    main()
