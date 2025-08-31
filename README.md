# trust-monitor {#trust-monitor}

Our goal is to develop a prototype that uses AI to identify specific quality indicators within news stories within the newsroom environment. This AI Monitor will be tailored specifically for newsroom editors, helping them to identify issues such as a lack of sources, an excess of adjectives, or discrepancies in information that can be addressed using online tools such as Fact-Checker Explorer.

## Index {#index}

- [trust-monitor {#trust-monitor}](#trust-monitor-trust-monitor)
  - [Index {#index}](#index-index)
  - [Installation {#installation}](#installation-installation)
    - [Using UV {#using-uv}](#using-uv-using-uv)
    - [Using pip](#using-pip)
  - [Usage {#usage}](#usage-usage)
  - [Project Structure {#project-structure}](#project-structure-project-structure)
  - [Output Response {#output-response}](#output-response-output-response)

## Installation {#installation}

### Using UV {#using-uv}

Create virtual environment, install the package as a library, and download the required Spanish language model for spaCy:

```bash
uv sync

uv pip install -e .

uv run spacy download es_core_news_sm
```

### Using pip

Install the package and download the required Spanish language model for spaCy:

```bash
!pip install .

!python -m spacy download es_core_news_sm
```

## Usage {#usage}

Execute the main script to run the project.

``` bash
python main.py
```

Alternatively, you can try it in a Live Python Terminal, as follows:

``` bash
from trustmonitor.nlp import NLP

nlp = NLP('es', 'spacy')
doc = nlp.analyze("El presidente de la Cámara de Propietarios de la República Argentina aseguró...")
entities = nlp.extract_entities(doc)
entities_count = nlp.count_entities(doc)
adjectives = nlp.extract_adjectives(doc)
adjective_count = nlp.count_adjectives(doc)
adjective_type_counts = nlp.count_adjective_types(doc)
entity_type_counts = nlp.count_entity_types(doc)
entity_sentiments = nlp.extract_entity_sentiments(doc)
```

## Project Structure {#project-structure}

``` bash
/trustmonitor
    |-- nlp.py
    |-- import_utils.py
    |-- articles.py
/data
    |-- docs
    |-- manual
    |-- raw
|-- main.py
|-- requirements.txt
|-- setup.py
|-- README.md
```

## Output Response {#output-response}

[see doc.](./docs/Trust_API_Anotacion_Noticias_Documentacion.pdf)