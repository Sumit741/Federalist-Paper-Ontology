# Validation

## Competency Question Name
**Competency Question:** "1. Which essays are credited to person P, and in which sources?"

**Bridged Datasets:** authorship_records.ttl, authorship_credits.ttl

**SPARQL Query:**
```
PREFIX fed: <https://w3id.org/federalist-paper-ontology/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT DISTINCT ?person ?essay ?source

WHERE {  
	?record a/rdfs:subClassOf* fed:AuthorshipRecord;
  			fed:creditsPerson ?person;
     		fed:isAboutEssay ?essay;
       		fed:isRecordedIn ?source .
}
ORDER BY DESC(?essay)
LIMIT 5
```

**Results:**
| Header |
| :----: |
| Result |
| Result |
| Result |
| Result |
| Result |

## Competency Question Name
**Competency Question:** "2. Whom does source S credit as the author of essay E?  "

**Bridged Datasets:** dataset 1, dataset 2, ...

**SPARQL Query:**
```
SELECT * WHERE {
	?s ?p ?o .
}
```

**Results:**
| Header |
| :----: |
| Result |
| Result |
| Result |
| Result |
| Result |

## Competency Question Name
**Competency Question:** "What am I?"

**Bridged Datasets:** dataset 1, dataset 2, ...

**SPARQL Query:**
```
SELECT * WHERE {
	?s ?p ?o .
}
```

**Results:**
| Header |
| :----: |
| Result |
| Result |
| Result |
| Result |
| Result |