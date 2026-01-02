# Phase 1 - Data Collection Degine 

##Source Type 
The source type for this project would be websited 
The Data would be fetch from HTML pages and extracted using texts

Website sourcing act as real world application of this project
Type of webite that would be used : 
blogs, articles, documentation

Are you avoiding login-protected sites? Yes for Now 

##Scope 
The project would right now contain about 500-1000 data or documents
Each Document would have 1-2 link deep penetration of data

Language (English only)

##Storage Format 
SQLite 

##Reasoning
Websites are selected as the data source because they closely resemble real-world search engine inputs and help expose challenges such as noisy text, inconsistent formatting, and varied content quality. Limiting the dataset to 500–1000 documents keeps the system manageable during early development while still being large enough to evaluate indexing and ranking performance.

A crawl depth limit of 2 is chosen to maintain relevance and control over the dataset size. English-only content reduces complexity in early stages and allows focus on core information retrieval and ranking concepts.

SQLite is chosen as the storage format because it provides a structured schema, supports efficient querying, prevents data duplication, and scales well for the intended dataset size without requiring a full database server.