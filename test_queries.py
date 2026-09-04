from neo4j import GraphDatabase

uri = "bolt://localhost:7687"
auth = ("neo4j", "password123")

def runDiagnostics():
    driver = GraphDatabase.driver(uri, auth=auth)
    with driver.session() as session:
        # Check Node Distributions
        nodeCounts = session.run("""
            MATCH (n)
            RETURN labels(n)[0] AS NodeLabel, count(n) AS TotalCount
            ORDER BY TotalCount DESC
        """)
        
        print("\n--- Graph Database Summary ---")
        for record in nodeCounts:
            print(f"Label: {record['NodeLabel']:<12} | Count: {record['TotalCount']}")

        # Sample Integrity Check
        topQuestion = session.run("""
            MATCH (q:Question)
            RETURN q.title AS Title, q.view_count AS Views
            ORDER BY q.view_count DESC
            LIMIT 1
        """).single()
        
        if topQuestion:
            print(f"\nMost Viewed Question: '{topQuestion['Title']}' with {topQuestion['Views']} views.")

    driver.close()

if __name__ == "__main__":
    runDiagnostics()