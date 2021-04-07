<a name="ds-cldfmetadatajson"> </a>

# Dictionary Sidaama dictionary

**CLDF Metadata**: [cldf-metadata.json](./cldf-metadata.json)

property | value
 --- | ---
[dc:bibliographicCitation](http://purl.org/dc/terms/bibliographicCitation) | Yri, Kjell Magne and Pepper, Steve. 2019. Sidaama dictionary. Dictionaria 6. 1-3578 (Available online at https://dictionaria.clld.org/contributions/sidaama)
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF Dictionary](http://cldf.clld.org/v1.0/terms.rdf#Dictionary)
[dc:creator](http://purl.org/dc/terms/creator) | Kjell Magne Yri and Steve Pepper
[dc:identifier](http://purl.org/dc/terms/identifier) | https://dictionaria.clld.org/contributions/sidaama
[dc:license](http://purl.org/dc/terms/license) | https://creativecommons.org/licenses/by/4.0/
[dcat:accessURL](http://www.w3.org/ns/dcat#accessURL) | git@github.com:dictionaria/sidaama
[prov:wasDerivedFrom](http://www.w3.org/ns/prov#wasDerivedFrom) | <ol><li><a href="git@github.com:dictionaria/sidaama/tree/c01fad8">git@github.com:dictionaria/sidaama v1.0-10-gc01fad8</a></li><li><a href="https://github.com/glottolog/glottolog/tree/v4.3-treedb-fixes">Glottolog v4.3-treedb-fixes</a></li></ol>
[prov:wasGeneratedBy](http://www.w3.org/ns/prov#wasGeneratedBy) | <ol><li><strong>python</strong>: 3.8.5</li><li><strong>python-packages</strong>: <a href="./requirements.txt">requirements.txt</a></li></ol>
[rdf:ID](http://www.w3.org/1999/02/22-rdf-syntax-ns#ID) | sidaama
[rdf:type](http://www.w3.org/1999/02/22-rdf-syntax-ns#type) | http://www.w3.org/ns/dcat#Distribution


## <a name="table-entriescsv"></a>Table [entries.csv](./entries.csv)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF EntryTable](http://cldf.clld.org/v1.0/terms.rdf#EntryTable)
[dc:extent](http://purl.org/dc/terms/extent) | 3578


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Language_ID](http://cldf.clld.org/v1.0/terms.rdf#languageReference) | `string` | References [languages.csv::ID](#table-languagescsv)
[Headword](http://cldf.clld.org/v1.0/terms.rdf#headword) | `string` | 
[Part_Of_Speech](http://cldf.clld.org/v1.0/terms.rdf#partOfSpeech) | `string` | 
`Construction` | `string` | 
`Entry_IDs` | list of `string` (separated by ` ; `) | References [entries.csv::ID](#table-entriescsv)
`Etymology` | `string` | 
`Gloss` | `string` | 
`Morpheme_Breaks` | `string` | 
`Morphological_Structure` | `string` | 
`Official_Orthography` | `string` | 
`Type` | `string` | 
`Variant_Form` | `string` | 

## <a name="table-sensescsv"></a>Table [senses.csv](./senses.csv)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF SenseTable](http://cldf.clld.org/v1.0/terms.rdf#SenseTable)
[dc:extent](http://purl.org/dc/terms/extent) | 3992


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Description](http://cldf.clld.org/v1.0/terms.rdf#description) | `string` | 
[Entry_ID](http://cldf.clld.org/v1.0/terms.rdf#entryReference) | `string` | References [entries.csv::ID](#table-entriescsv)
[Comment](http://cldf.clld.org/v1.0/terms.rdf#comment) | `string` | 

## <a name="table-examplescsv"></a>Table [examples.csv](./examples.csv)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF ExampleTable](http://cldf.clld.org/v1.0/terms.rdf#ExampleTable)
[dc:extent](http://purl.org/dc/terms/extent) | 1191


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Language_ID](http://cldf.clld.org/v1.0/terms.rdf#languageReference) | `string` | References [languages.csv::ID](#table-languagescsv)
[Primary_Text](http://cldf.clld.org/v1.0/terms.rdf#primaryText) | `string` | 
[Analyzed_Word](http://cldf.clld.org/v1.0/terms.rdf#analyzedWord) | list of `string` (separated by `\t`) | 
[Gloss](http://cldf.clld.org/v1.0/terms.rdf#gloss) | list of `string` (separated by `\t`) | 
[Translated_Text](http://cldf.clld.org/v1.0/terms.rdf#translatedText) | `string` | 
[Meta_Language_ID](http://cldf.clld.org/v1.0/terms.rdf#metaLanguageReference) | `string` | References [languages.csv::ID](#table-languagescsv)
[Comment](http://cldf.clld.org/v1.0/terms.rdf#comment) | `string` | 
`Corpus_Reference` | `string` | 
`Gloss_POS` | list of `string` (separated by `	`) | 
`Sense_IDs` | list of `string` (separated by ` ; `) | References [senses.csv::ID](#table-sensescsv)

## <a name="table-mediacsv"></a>Table [media.csv](./media.csv)

property | value
 --- | ---


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Language_ID](http://cldf.clld.org/v1.0/terms.rdf#languageReference) | `string` | References [languages.csv::ID](#table-languagescsv)
`Filename` | `string` | 
`URL` | `anyURI` | 
`mimetype` | `string` | 
`size` | `integer` | 

## <a name="table-languagescsv"></a>Table [languages.csv](./languages.csv)

property | value
 --- | ---
[dc:conformsTo](http://purl.org/dc/terms/conformsTo) | [CLDF LanguageTable](http://cldf.clld.org/v1.0/terms.rdf#LanguageTable)
[dc:extent](http://purl.org/dc/terms/extent) | 1


### Columns

Name/Property | Datatype | Description
 --- | --- | --- 
[ID](http://cldf.clld.org/v1.0/terms.rdf#id) | `string` | Primary key
[Name](http://cldf.clld.org/v1.0/terms.rdf#name) | `string` | 
[Macroarea](http://cldf.clld.org/v1.0/terms.rdf#macroarea) | `string` | 
[Latitude](http://cldf.clld.org/v1.0/terms.rdf#latitude) | `decimal` | 
[Longitude](http://cldf.clld.org/v1.0/terms.rdf#longitude) | `decimal` | 
[Glottocode](http://cldf.clld.org/v1.0/terms.rdf#glottocode) | `string` | 
[ISO639P3code](http://cldf.clld.org/v1.0/terms.rdf#iso639P3code) | `string` | 

