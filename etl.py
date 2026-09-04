import os
import pandas as pd
from neo4j import GraphDatabase

uri = os.getenv("NEO4J_URI", "bolt://localhost:7687")
auth = (os.getenv("NEO4J_USER", "neo4j"), os.getenv("NEO4J_PASSWORD", "password123"))
batchSize = 500

def createConstraintsAndIndexes(session):
    """Ensure database schema rules and indexes are applied."""
    schemaStatements = [
        "CREATE CONSTRAINT IF NOT EXISTS FOR (u:User) REQUIRE u.uuid IS UNIQUE;",
        "CREATE CONSTRAINT IF NOT EXISTS FOR (q:Question) REQUIRE q.uuid IS UNIQUE;",
        "CREATE CONSTRAINT IF NOT EXISTS FOR (a:Answer) REQUIRE a.uuid IS UNIQUE;",
        "CREATE CONSTRAINT IF NOT EXISTS FOR (c:Comment) REQUIRE c.uuid IS UNIQUE;",
        "CREATE CONSTRAINT IF NOT EXISTS FOR (t:Tag) REQUIRE t.tag_id IS UNIQUE;",
        "CREATE INDEX IF NOT EXISTS FOR (q:Question) ON (q.view_count);"
    ]
    for statement in schemaStatements:
        session.run(statement)
    print("Schema constraints and indexes successfully initialized.")

def ingestBatch(session, cypherQuery, dataFrame, labelName):
    """Processes DataFrame in memory-friendly batches using UNWIND parameterization."""
    records = dataFrame.to_dict(orient="records")
    totalRecords = len(records)
    
    for i in range(0, totalRecords, batchSize):
        batch = records[i:i + batchSize]
        session.run(cypherQuery, rows=batch)
    print(f"Ingested {totalRecords} {labelName} nodes.")

def runEtl():
    driver = GraphDatabase.driver(uri, auth=auth)
    
    with driver.session() as session:
        createConstraintsAndIndexes(session)

        # Users
        usersDf = pd.read_csv("data/stackoverflow.nodes.User.csv").fillna("")
        cypherUsers = """
            UNWIND $rows AS row
            MERGE (u:User {uuid: row.uuid})
            SET u.user_id = row.user_id, u.display_name = row.display_name
        """
        ingestBatch(session, cypherUsers, usersDf, "User")

        # Tags
        tagsDf = pd.read_csv("data/stackoverflow.nodes.Tag.csv").fillna("")
        cypherTags = """
            UNWIND $rows AS row
            MERGE (t:Tag {tag_id: row.tag_id})
            SET t.name = row.name, t.link = row.link
        """
        ingestBatch(session, cypherTags, tagsDf, "Tag")

        # Questions
        questionsDf = pd.read_csv("data/stackoverflow.nodes.Question.csv").fillna("")
        cypherQuestions = """
            UNWIND $rows AS row
            MERGE (q:Question {uuid: row.uuid})
            SET q.question_id = row.question_id, 
                q.title = row.title, 
                q.view_count = toInteger(row.view_count), 
                q.answer_count = toInteger(row.answer_count),
                q.creation_date = row.creation_date, 
                q.link = row.link
        """
        ingestBatch(session, cypherQuestions, questionsDf, "Question")

        # Answers
        answersDf = pd.read_csv("data/stackoverflow.nodes.Answer.csv").fillna("")
        cypherAnswers = """
            UNWIND $rows AS row
            MERGE (a:Answer {uuid: row.uuid})
            SET a.answer_id = row.answer_id, 
                a.score = toInteger(row.score), 
                a.is_accepted = row.is_accepted, 
                a.link = row.link
        """
        ingestBatch(session, cypherAnswers, answersDf, "Answer")

        # Comments
        commentsDf = pd.read_csv("data/stackoverflow.nodes.Comment.csv").fillna("")
        cypherComments = """
            UNWIND $rows AS row
            MERGE (c:Comment {uuid: row.uuid})
            SET c.comment_id = row.comment_id, 
                c.score = toInteger(row.score), 
                c.link = row.link
        """
        ingestBatch(session, cypherComments, commentsDf, "Comment")

    driver.close()
    print("ETL pipeline executed successfully.")

if __name__ == "__main__":
    runEtl()