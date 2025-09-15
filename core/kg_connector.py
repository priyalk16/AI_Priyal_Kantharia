# core/kg_connector.py

import os
from neo4j import GraphDatabase

class KnowledgeGraphConnector:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def get_concept_data(self, concept_name: str) -> dict:
        """
        Queries the Knowledge Graph for a given concept and its relationships.
        """
        query = """
        MATCH (c:Concept {name: $name})-[r]-(n)
        RETURN c, r, n
        """
        with self.driver.session() as session:
            result = session.run(query, name=concept_name)
            # Convert the Neo4j result into a structured Python dictionary
            data = [
                {
                    "concept": record["c"]["name"],
                    "relationship": record["r"].type,
                    "related_node": record["n"]["name"],
                }
                for record in result
            ]
            return data
